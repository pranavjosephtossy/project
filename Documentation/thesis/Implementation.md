# Initial Implementation
The process of comming up with a physical implementation of this methodology was a very itterative process. The initial basic thought process revolved around this pipeline:
Filtering->Collection->Analysis->Storage.
We would collect social media data throught an API, quering based on ceetain use cases. The use cases could range from filtering for sexist content to early indicators of crypto scams. Once the relevant data is colected we would analyse it and store data based on if it met the crieteria. If it did it would be stroed in a forensically sound manner.
This initial pipe line was itterated and improved until we formalized the following pipeline:
Filtering->Filtering->Analysis->Catagorization->Storage.
Following analysis each data set would be catagorized into three groups. The irrelevant ones, ie the one that do not meet the criteria, the relevant ones, ie they do meet the crietria and the grey area ones, ones we are unsure about. The relavents are passed through the storage module while the third catagorey would requier an human-in-loop reviewr to determine if it is pertinent or not.

Briefly speaking this pipeline would be implemented into three modules. The first one responsiblie for the collections of the data via the social media API. The second module would determine if the conent meets the use case and pass it along to the third module which would follow the digital forensic methodology of storing said data.

Since reddit provides its own proprietory API we can use that as the first module. They way it works is you register with reddit and use the assigned key to query information from them. The information is stored and passed as JSON which is super helpful. The second module would have to be our own program that goes through the queried data and matches set key words relevant to each specific use case. There would be two lists of keywords to be matched. One which are blatently obvious like slurs if the use case accounted for bigotry and a second that could be less obvious dog whistles or comments that could be "sarcastic". The second list is what would potentially need a human-in-loop review. The third module would also be proprietory program which would hash and forensically store relevant data.

# Final Implementation
Through out this process we had been thinking about how we could implement automation or AI into this pipeline so as to make it more relevant to modern day standards. Following a meeting with our supervisor we came up with an alternative pipeline which follows true modularity while implementing AI. The revised pipeline would look like this:

`
    Reddit API->
    Filtering and Collection Module->
    AI/LLM Analysis Module->
    Catagorization Module->
    Strorage Module
`


We query the data from the API using filters. Reddit offers extensive querying filters which can be manipulated accourdingly to fit the use case. Once queried we can pass the data into a LLM which then decideds how to catagorize it. It also assigns a priority level thereby pushing the more egregious use case matches forward. Once it has determined if the data fullfills the use case it passes it to the storage module. This in turn is a propretry program that forensically stores the data.

This implementation is proof of true modularity. While ideally, with appropriate resources you would want all three modules, ie collection, analysis and stoirage to be done by your own propreitory program so it can be hype specialized to your needs it can also be more economical sense by using third party services. In this implementaion we are going for a more balance approach by both using third party services like a social media's API and a LLM, and propritory code.

Ulitimately the methodology remains the same. Further the methodology remains the same irresepective of the use case which makes it very versitile. The same methodology can be used on other social media apis or multiple ones and by alteribg the filering and analysis module we can customize the use case range. Further for added complexity and dynamicism we can add on to the catagorization module to offere a tier structured priority and severity labels to conents. This is made possible by the LLM's ability to understand context.

# JSON STRUCTURE AND DATA EXTRACTION

When querying YouTube’s API for videos, the results came back in a structured hierarchical format rather than a simple list. The outer layer is the search lists response for , which is a container for all of the results. Inside this is an items array where each element represents a single video and contains the core metadata ,(the video ID, the channel name, the publication stamp, the title and the description. When the comments are collected ina follow-up query, a separate commentThreads is returned for each video, where each item holds a topLevelComment object containing the comment, the author and the time that it was posted. One example of this can be seen down below
 
In theory a full API response for a single video would contain a large number of additional information depending on what was requested, covering everything from engagement statistics to content rating and reginal restrictions. However storing all of this would be unnecessary and it would just add noise into the dataset without increasing any real forensic value. Because of this reason only the fields that we considered to be forensically and analytically relevant were extracted and carried forward.
# FIELDS SELECTED FOR EXTRACTION

video_id: the unique identifier for each video assigned to by YouTube. This id prevent the same video from being queried multiple times. It is also the parameter used when querying comments for a specific video

channel_title: The name of the channel, this identifies the source of the content and it can be used for spotting patterns of behaviour linked to a specific creator or organisation over time.

Published_at: The exact timestamp of when the video was published. This si one of the most important fields as it allows data to be placed within a precise timeline and it can be used by the LLM to compare with real-world events.

title and description: the textual content that is associated with the video. The title acts as a headline and the description is the body of the record . Together they create the primary input to the LLM analysis module at the video level.

Video_url: a direct link to the video on Youtube. This is kept so that a reviewer can verify the content in its original context at a later stage. Which is crucial for maintaining integrity and availability.

Comment_author: Display name of the account that posted the comment. Retained for scenarios where the data is to be ever used in a formal investigation.

Comment_text: full text of the comment. The primary field that is analysed by the LLM at the comment level.

Comment_published_at: the timestamp  of when the comment was posted. Useful for making sure whether the comment was made in repose toa  specific event and for building an idea of how discussion developed over time

Everything ekse returned by the API is discarded at this stage. Keeping only the fields above ensures the dataset stays lean and straightforward for the LLM to process

# YouTube Data API
In order to access YouTube’s Data API, which is googles way of giving developers access to public YouTube content, we had to register a project on Google Cloud Console and generate an API key, which the is attached to every request. One thing we had to be aware of was the quota system. Each project gets 10,000 units per day on the free tier and not every request cost the same amount. A search query itself costs 100 units each time, meanwhile extracting comments only cost 1 unit. This gap can fill up very quickly as 10 searches can end up costing 1000 units. So, to run at a scale, we had to be precise and smart on how many queries can be run each session.

We used two endpoints. The first is youtube/v3/search, which queries the videos based on a search item. We then passed in the search query using the q parameter, set type=video to only return videos, and used maxResults to cap how many results came back to us. The second is youtube/v3/commentThreads, which takes a video ID from the search results and gives back the top-level comments (note. Replies within threads are not included, which is something we noted as a limitation of the current implementation.

# LLM ANALYSIS
After collecting the data, each record gets passed onto a large language model for analysis. The idea is that the model looks at the content and gives us the severity of the content and a short explanation as to why it was assigned that rating.

We decided to use OpenAI’s GPT-4o-mini model for this, since it is cheaper and faster than most of the larger models. For each record we decided we build a prompt from the extracted fields, and we asked the model to analyse the content against the use case that we are evaluating. The use case is a variable that can be found on the top of the script, so switching it from hate speech around a sports event to something like sexism in the workplace only requires changing that one line and nothing else in the code.

The model is instructed to return a JSON object with two fields. Severity gets rated as high, medium, low or none. The reasoning then gives a couple of sentences to explain the decision it made. The reasoning field is considered one of the more important fields as it allows a human reviewer to look at why the model flagged something rather than having to blindly trust the LLM at face value. This process was considered essential to prevent hallucinations. If the model has misread the text or the context, the reviewer can see that immediately find a remediation.
In order to get consistent results, we set the temperature of the LLM to 0.3, in this way since it is not a high temperature the LLM does not produce random information but stays true to its goal of accuracy. (note in further work we wanted to increase the temperature with increased training data in order to allow the LLM to think in different contexts)

Once the model responds, the severity and the reasoning fields gets added onto the record and the whole output gets written onto one single output JSON file. Everything goes into that file regardless of its severity and nothing gets discarded at this stage. We decided to do this as leaving an LLM to throw away data before a human review it would be the wrong call especially since we do not have full insight into the model’s internal decision-making process. This would also be essential in a forensic context where it might be essential to go back and reassess the full dataset later. Keeping the full dataset with the models reasoning attached would mean that the reviewer has the full picture and makes the final judgement themselves.

# Storage implemnttion
The storage module is tasked with taking the output from collection and analysis stages and creaking a forensic package that can be stored. In the implementation this is carried out by a python function that recieves four inputs: the raw json item, the analysis json which is the output of the analysis module and the collection  and analysis log created by the chain of custody function. The ducntion then performs a series of integrity checks to ensure the data isn't tampered with and finally a forensic package which contains the logs of the chain of custody, hashes, raw json and the llm analysis.

The first step is comparing the hashes of ...

Then generate the chain of custody log by calling the chain of custody function. We pass into it the action perforemed, ie storing data and the moduled it is performed by, ie the storage module. We finaklly compile all three logs, collection, analysis and storage into a single final log for the json item. 

Finally we create the forensic package which will hold the final output of the implementation. To maintain consistancy we will save it as a json file. It will hold the raw json, the anlysis output and chain of custody. The module will finally return this package to main interface.

# Chain of custody
The chain of custody system is intended to log the path/logic of the entire implementation. It is a simple python function into which each module will pass the action it performed and the module the action was performed by. Additionally inbuilt into the function is a timefunction that logs the exact time the logging took place. 

The purpose of having this system as a function is to ensure the reuability of it by various modules and reducing duplication of work. It is a set standard with the only variables being the action peroformed and the module it was performed by. Even then the variables are fixed and unique to each module. They are automated so even the variations are fixed. 
