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

# API
## Reddit's API
# LLM
# Hashinf/storage implemnttion
