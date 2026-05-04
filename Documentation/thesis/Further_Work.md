# Further Work
What we have done so far, works very well as a proof of concept. However, there is a lot more than can be done with the it. Some of these are extensions of what is already there. While others are gaps, we came across the way that would be useful filling in.

The most important and obvious addition would be to support more platforms. The collection module can be extended to pull data from X, Instagram or Reddit without having to make any changes to the analysis or storage parts. Each platform would require its own setup for the API, but the rest of the system would stay the same. This could open the framework to a much larger range of investigations.

Another approach was to move away from using a commercial LLM and to train our own system. GPT-4o-mini is primarily designed for general purposes and its guardrails are not designed for forensic purposes, which would make it too cautious in some areas and not enough caution being applied to other areas. A model that is trained on labelled hate speech and the sue case of specific language is most likely to do a better job. As well as this would be hosted locally, so no information would be sent out to third party host.

Along with hosting a local machine, we could also adjust its temperature settings. We purposefully kept the temperature at 0.3 to make the outputs as consistent as possible since we had provided the LLM no real training data. If we had a properly fine-tuned model with a bigger dataset to work from the temperature could be then raised so the model would be able to reason across more context without going off its guardrails. For now, we decided that consistency is more important.

A proper human review interface would also be big improvement. Due to the fact that the LLM will always come across a comment where it is not confident enough to commit to a rating. A simple human interface where an individual can manually check and go through these uncertain cases and give the final verdict would be able to close that gap.

Real time- monitoring is another crucial step. Right now, the system runs solely on one query and stops. A continuous system that would allow for a system to be updated in real time and continuously update and track things as they unfold would allow for the LLM to have a better idea on the context and therefore be able to make more accurate decisions.

Profiling accounts is also another decision that is worth integrating. Right now every comment is isolated on its own, but the account behind the comments is not flagged. When accounts are recently created and high severity comments are generated with little to no posting history, it can be a giveaway as to why the account was created in the first place (to spread hate). Flagging and monitoring these accounts can pick up a lot of information and help collect more information for the LLM.

Multi-language support is another step the system would benefit from, the current set up is built entirely based on English language content. Extending the support for multiple languages can help the filtering and analysis to handle other languages and therefore widen the scope for what the framework can be used for.

Lastly, going beyond text is a useful decision to implement. A lot of harmful content can be seen in memes, screenshots and gifs rather that written posts. So, applying image recognition by training the LLM’s CNN could catch a lot of content that an LLM can miss entirely.
