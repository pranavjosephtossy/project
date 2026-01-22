## Overview
The thesis follows a structured methodology to collect, analyse and forensically store social media content through APIs. The methododlogy will accquire online discorese on relevant topics based on key events or a sub-reddit. The acquisition invovlves quering for either and then based on the satisfaction of parameters which are unique to each use case, following the already established forensic collection of information and storing it until its verified. 442497

This approach to data quering, filtering, analysis and collection is meant to form a framework which can be repeated and modified accordingly for each use case. A key concept to remembere is how the filters are unique to a particular use case. The contexts are depended entierly on what the use case is and while they may not be qunique for each each use case needs its own relevent context.

This methodology doesnt initialy treat queried evidence as formal evidence. The initial stages aim to collect raw data before filtering them for obvious indicators. Only then if they meet necessary criteria is the data identified as digital evidence

## Preemtive Data Collection
Reasoning

    Given how vast and quick social media content are poseted, edited and deleted it is important to spot early manifestations of abuse and behaviour and collect it before it can be erased. This is also helpful in a two fold scenario where actions are recorded before a formal investion is even initiated. 
    Preemptive data collection thus allows the acquisition of data at its initial occurence. This helps maintain contextual integrity, not allowing the person the ability to change/alter this context.

    Preemtive Data Collection doesnt automaticaly equate to enforcement or surveillance. It is a responsibile way to preserve publicaly accessible information which may either later lead to an investigation or be used to fill in contexts.

Event-base vs sub-reddit based

    There are two type of methadology to collect data
    - Event Based
    - Account Based

    Event based collection focuses on acquisition of data which revolve around a real-worl event. This could be anything of significane from sporting events to disasters to insigificanse like a particular date or window of time. Depending on the context of the event, relevent keywords and timeframes are used to as parameters to filter the queried data. 

    Account based collection targets a particular account for posts,likes and comments left by the user. 

    While both adopt a similar methodology they used differnet query parameters. 

Timeframe

    Allowing for a variable selection of time can help expand the scope of the query helping aquire relevent information or establish a timeline or pattern. The methodology can primarily adopt two timeframe selctions:
    - Relative windows
    - Event-based windows

    Relative windows provides a fixed window for acquizition of  data bases on the initial request or query. These time frames typically invovlbe, last 24 hrs or last 30 days and so on. This is dynamically updated based on the cureent time of enquiery.

    Event-based windows are fixed windows revolving around the event. This could be before the event, during the event and after it.

    Placing restrictions usinf time frames ensures the quering of relevent data. This speeds up the process and dramatically reduces the initial sample size before filtering.

## Data Filtering
    - Keyword
    Initially you only want to query data regarding a) the event or b) the subreddit. This is the first stage of narrowing down the net so to speak. Then we filter out the queried data and look for predefined keywords which are specific to the context. 
    Keywords may be anything from a phrase associated with negative sterotypes to event identifiers. One example of this would be a common misogynistic pharese used to diminish women is "women☕". This ensure all relevent content are included 

    - False positives
    There can never be a guarentee that all the filtered content are infact harmful in nature. Some content may feature indicators of the particular case but may still not fit it.This could be a result of overlapping keywords, different contexts or even satire. This is why its important to not treat the data as digital evidence yet, even though they may have fit the initial parameter for it. This ensures that the data set is contextually relevent.

## Categorization
Categorization involves placing filtered content into groups based on context and intent. This is not to assign legal severity rather to organise data in a structured manner for review.

This helps differentiate content into groups based on if they are missinformation, abusive content or threats. This also might involve determining if its relevent or not. These categorizations are based on each use cases specific context. 

In adition to what the content is, catagorizing also determines how concerning/bad the content is. Depending on the context it might be important to document how severe it is, maybe even promting an immediate enquiery. This can help later in a formal investigation as it prioratized which ones should be looked at first. 
- What is it
- How bas is it

## Preservation and Integrity
Preserving data collected is a fundamental aspect in forensic methodology. Following Filtering andCatagorization it is important to store the relevent data from the dataset in a forensically secure manner to enure integrity and reproducibility. This is so much later down the line, if the data were to be needed in a formal enquiery, be it initiated by a private sector company or a court, the evidence is admissable.

Hashing is applied to each data item during storage. These values are way of ensuring integrity as each hash value is uique to the data. Every minute change alters the value as it is unique to each dataset. 


- Hashing
- Chain of Custody

## Evidence catagorization
- data vs evidence

## Ethical and Legal
- Privacy
- Censorship and Surveillance

## Limitations
- Shortfalls