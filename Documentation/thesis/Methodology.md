## Overview
The thesis follows a structured methodology to collect, analyse and forensically store social media content through APIs. The methododlogy will accquire online discorese on relevant topics based on key events or topics. The acquisition invovlves quering from a social media platforms API for a specific scenario. Once the data has been queried it will be analysed to see if certain parameters based on the use cases context is fullfilled. Then the data is catagorized and relevent ones are stored in a forensicaly sound matter so they can be later be relied upon in court if recquiered.


This approach of data collection, analysis and storage is meant to form a framework which can be universally apllied. The methodology is meant to afford versility in both its application and actual implementation. A key concept to remembere is how the filters are unique to a particular use case. The contexts are depended entierly on what the use case is and while they may not be unique for each use case needs its own relevent context.

This methodology doesnt initialy treat queried data as formal evidence. The initial stages aim to collect raw data before filtering and catagorizing them based on indicators. Only then if they meet necessary criteria is the data identified and stored as digital evidence.

## Preemtive Data Collection
Reasoning

    Given how vast and quick social media content are posted, edited and deleted it is important to spot early manifestations of abuse and behaviour and collect it before it can be erased or altered. This is also helpful in a two fold scenario where actions are recorded before a formal investion is even initiated. 
    Preemptive data collection thus allows the acquisition of data at its initial occurence. This helps maintain contextual integrity, not allowing the person the ability to change/alter this context.

    Preemtive Data Collection doesnt automaticaly equate to enforcement or surveillance. It is a responsibile way to preserve publicaly accessible information which may either later lead to an investigation or be used to fill in contexts.

Event-base vs user based

    There are two type of methadology to collect data
    - Event Based
    - Account Based

    Event based collection focuses on acquisition of data which revolve around a real-worl event or topic. This could be anything of significane from sporting events to disasters to insigificanse like a video essay. Depending on the context of the event, relevent keywords and timeframes are used to as parameters to filter the queried data. 

    Account based collection targets a particular account for posts,likes and comments left by the user. This is a more in depth/micro approach as it focuses one user rather than multipe users around an event or topic. 

    While both adopt a similar methodology they used differnet query parameters. 

Timeframe

    Allowing for a variable selection of time can help expand the scope of the query helping aquire relevent information or establish a timeline or pattern. The methodology can primarily adopt two timeframe selctions:
    - Relative windows
    - Event-based windows

    Relative windows provides a fixed window for acquizition of  data bases on the initial request or query. These time frames typically invovlbe, last 24 hrs or last 30 days and so on. This is dynamically updated based on the cureent time of enquiery.

    Event-based windows are fixed windows revolving around the event. This could be before the event, during the event and after it.

    Placing restrictions using time frames ensures the quering of relevent data. This speeds up the process and dramatically reduces the initial sample size before filtering.

## Data Filtering
    - Keyword
    Initially you only want to query data regarding an event or topic. This is the first stage of narrowing down the net so to speak. Then we filter out the queried data and look for keywords which are specific to the context. 
    Keywords may be anything from a phrase associated with negative sterotypes to event identifiers. One example of this would be a common misogynistic pharese used to diminish women, "women☕". This ensures all relevent content are included 

    - False positives
    There can never be a guarentee that all the filtered content are infact harmful in nature. Some content may feature indicators of the particular case but may still not fit it.This could be a result of overlapping keywords, different contexts or even satire. This is why its important to not treat the data as digital evidence yet, even though they may have fit the initial parameter for it. This ensures that the data set is contextually relevent.

## Categorization
Categorization involves placing filtered content into groups based on context and intent. This is not to determine legal guilt or innocence rather to organise data in a structured manner. By grouping related content it becomes esier for us to distinguish between content pertinent for further analysis. Think of it as sorting out the content on three bases. The black and white ones, obviously distinguishible as relevant or not relevant. And the third one as greys. These would warrent further examination requiering a human-in-the-loop review. 

Further this can be fledged out by using it to differentiate content into groups based on if they are missinformation, abusive content, harassment or threats. Using the context of the content is key as it may be what diffrentiates an actual threath from a sarcastic comment or joke. 

In adition to what the content is, catagorizing also determines the severity or concern associated with a post or comment, maybe even promting an immediate enquiery. This can help later in a formal investigation as it prioratized which ones should be looked at first. While the methodology assigns no legal judgement, a foundational level severity catagorization may assist in prioritizing reviews.  

The structured catagorization improves the efficiency of later stages of analysis by reducing human requiered review of non pertinent content. Thereby leaving higher priority reviews for reviews.

## Forensic methodology
Within digital forensics, forensic methodology is a seris to steps used to aid in acquiring, handling and preserving information that can be later relied on in court. There is a special emphasis on accountability, integrity and reproducability. Typically these guidlines are used in investigations related to seized electrnic devices and storage devices however, the underling principles can also be applied in relation to more modern mediums like online environments. The prevelence of internet in our day to day like be it through social media or online mediums of data storage expands the scope of forensic methodology.

In this thesis this forensic methodology serves as an esential backbone ensuring the appropriate handeling of social media data. It is vital to remmember that athe api queried content is not legal evidence automatically. That is a decision beyond the scope of this methodology. They are however treated as such. The methodology this thesis covers higlights the ira that the content is treated as data and not evidence. This is similar to the the real world implementation of digital forensices where this seperation prevents prematurely assigning legal significance to unverified or out of context material. This makes the tool as a structures system for organising and preserving relevant information instead of an automated investigative tool.

This is why the following of a forensic methodology is esential as it is the only way to assure the integrity of it. 

Social media content is particulary volatile as posts can be edited, altered or deleted. A forensci methodology hence ensure a trustwothy snapshot of what existed at the time of collection. An importat foundation of this methodology is traceablility. Each stage from collection to storage happens at a specific time. Having a record of this ensures that when later scrutanized there is  a documented explanation of the "path" the evididence took. This aligns with the forencis concept of chain of custody, ensuring accountability of data integrity.

Due to how varied and dynamic social media data is from platfor to platform, this methodology ensures the framework is standardized yet versitile enpugh to be adaptable to differing API formats while still being forensically valid. This methodology does not seek to constrict the tecninal mechanisms on its implemetation, rather a general guiedline that can be followed to ensure accountability and integrity that any implementation can follow. This enables the application of this methodology across platforms and use cases while still folowwing a recognised and sound forensic path.
## Preservation and Integrity
Preserving data collected is a fundamental aspect of digital forensic methodology. Following Collection and Catagorization it is important to store the relevent data from the dataset in a forensically secure manner to enure integrity and reproducibility. This is to ensure that the collected data remains unaltered and reproducible if it is later required for formal investigations or as evidence in court.

Proper preservation allows investigators to demonstrate that stored data has not been altered, so they can stand behind it. The system should therefore not recorde just the data itself, but also the associated metadata such as timestamps, user info and hashes of the content itself.

Hashing is applied to each content following collection. This is done so to reduce the widow of potential alteration. Once the hases are recordeed, the content is catagorized.
By generating and recording the hashes it becomes possible to later verify that the stored data wasn't altered

The concept of chain of custody referes to documenting how digital evidence is handled throughout its life cycle. Although the system does not constitue a full investigative chain of custody, by logging the time of collection, the source of data and the actions performed it follows a similar policy. 

## Evidence catagorization
- data vs evidence
This methodology distinguished between data and digital evidence. Not all content collected qualifies as evidence, rather as raw data that may contain information or behaviour relevent to each specific use case. Only afteer the data is categorized and a human-review can it be potentially be considered as digital evidence. Even then we are not assigning legal distiction of evidence or not, only treating it as such in case it does becomee.

By maintaing a clear seperation between data and digital evidence the methodolofy avoids prematurely assigning legal significane to non-pertinent content. This ensures the system does not work as an automated investigtive authority.

## Limitations
One major limitation of the proposed methodology is the reliance on keyword-based filtering to collect data. While practicle nor narrowing large datasets it cannot capture all the complexity of online discouse as langualge on social media platforns often involve sarcasme, code or ever evolving slang. 

As a result the process is likely to generate a lot of false positives and false negatives. Like with most cases while false positves can be rectified by review false negatives are a much major short comming. There may be pertinent or even really very sevier cases that may be ignored simply because we "fished in the worng spot". This can happen by either missing necessasry keywords or searchin in the wrong place.

Another limitation is the focus on a single platform for data collection. This limits the general aplicability of the framework across othr social media environment. The system is dependent on the capabilities of the platforms API. Restrictions like rate limits and missing hostorical content affects the completeness of the dataset.