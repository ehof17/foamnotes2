# The Simpson’s Paradox in the Offline Evaluation of Recommendation Systems
https://dl.acm.org/doi/10.1145/3458509

### Offline Evals
Offline eval of recsys has 2 stages.
1. Gathering data
2. Empirically evaluate and compare different recsys models.
The first stage can be subject to different [[Confounders]]

For instance, users are more likely to interact with items that they have already been exposed to. This forms a [[Closed Loop Feedback]], the deployed recsys has a direct effect on collected feedback.

> Problem: Evaluations are ran in the basis of how well it can mimic the deployed model, rather than true user preferences

Another way to do it is using [[Open Loop]], where the deployed model makes random items shown to the users. With this we can be sure that the deployed model has no effect on the collected feedback dataset and can truly see what is good. Only problem is it would suck to get totally random items in your feed as a customer.

### Simpsons Paradox
- When a trend appears in several groups in observational data, but disappears or even reverses when the groups are bounded together.
- In recsys, this occurs when the association between exposrue (item) and outcome (user feedback) is looked at but both are influenced by a 3rd variable.

An example is treating kidney stones, two different treatments, and two different types of stones and recovery rate

Size    Treatment A  Treatment B  
< 2cm   93%             87%            
/> 2 cm 73%             69%
Both    78%             83%

So both individually, treatment A is better than treatment Big
But total, treatment B is better.

A majority of patients that got treatment A had large stones. A majority of treatment B has small stones. So when randomly selecting people that got A or B, the sampling process is not purely random,


Propensity score
- Tendency of the deployed model to expose item i E I to user u E u



[Confounders]: Confounders.md "Confounders"
[Closed Loop Feedback]: <Closed Loop Feedback.md> "Closed Loop Feedback"
[Open Loop]: <Open Loop.md> "Open Loop"
