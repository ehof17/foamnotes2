https://arxiv.org/html/2301.04016v1
### Big question trying to be answered:
> Does recsys cause the purchase? Or would they purchase anyway?

Real world applications are driven by underlying causal mechanisms. Purely correlative learning without considering causation will lead to some issues. An example is with beer and diapers. Pure correlative learning will learn the strong correlation between beer and diapers, so recommend beer for users that bought diapers and vice versa. However, the underlying mechanism is that young fathers purchase beer and diapers together, and recommending beer or diapers without considering the underlying mechanism will cause confusion and further hurt user satisfaction. Therefore it is important to advance from correlative learning to causal learning.


> Causal Inference: Studying the relation between cause and effect, where cause takes responsibility of the effect.
- Drawing a conclusion that a specific treatment was the cause of the outcome that was observed

### Potential outcome
- Outcome for an individual under a possible treatment

Let X | X E {x1, x2, ... xn} debnote the treatment, where n is the total number of treatments.
Most often binary treatment, like taking medicine is X=1, not taking medicine is X=0. People that took meds are in treated group, people that did not are the control group.
The potential outcome of treatment with value xi, Y(X=xi) simplified to Y(xi). The average potential outcome of treatment with value can be denoted as E[Y(xi)]. For any individual, only one treatment can be applied while keeping other variables uncahnged, so only one outcome can be observed. Potential outcomes can be divided into obeserved outcomes and counterfactual outcomes.

In recsys, the outcome is a user behavior. Click, purchase, etc. Or it could be preference like rating. The treatment is exposure, in whcih the observed feedback Y can be modeled as the product of two unobserved variables exposure O and relevance R R(i.e, Y = O * R). Y=0 can be either negative samples (R=0) (Not relevant), or potential positive samples (R=1, O=0) (Relevant, not exposed) which lead to data bias in the recommendation. To achieve personal recs, models usually estimate potential outcome Y(u,v) for a certain user-item pair (Y(u,v) = O(u,v) * R(u,v)). By correctly estimating potential outcome, the designed model is able to acheive unbiased recommendation. 

Uplift-based rec models define the treatment as recommendation (1 for recommened, 0 for not). Therefore, it is a challenge of estimating the counterfactual outcome to calculate the uplift value for recommendation. To achieve fairness, the treatment can also be defined as the sensitive attribute [76](e.g., 1 for privileged group and 0 for disadvantaged group).

### Pre Treament variables
- variables that are not affected by the treatment, which are also named as background variables

### Post Treatment Variables
- variables that are affected by treatment

### Do - Operation
If X denotes treatment and Y denotes outcome, correlationan and causation pursue different probabilities. Correlation estimates the conditional probability P(Y|X) from observational data to determine the correlative relation between X and Y. Causal inference estimates P(Y|do(X=xi)) representing the outcome under a possible treatment xi, where do-operation denotes applying the treatment instead of observing the treatment.
The average outcome of applying treatment xi xan be represented as E[Y|do(X=xi)].  A specific probability P(Y=y|do(X=x)) can be simplified as P(y|do(x)).

Treatment is typically exposure in recsys. The results for a user-item pair (u,v) under exposure can be represented as P(Y|y,v,do(X=1)) where Y is the outcome and X is the exposure variable. If we define variable V as exposed items, then it can also be represented as P(Y|u,do(V=v)). Causal notation in uplift based recommendation and fairness for recommendation can also be expressed by do-opeations

Do iperation denotes applying the treatment, which can also be defined as the intervention on the treatment variable. Counterfactual is an important concept in both the potential outcome framework and structural causal model, which represents the difference with factual. Counterfactual represents a scenario that the treatment variable had a different value compared with the observed value in the factual world. For example, if treatment=taking drug, outcome=recovery.A patient who took drugs and recovered may wonder if he would have recovered if he hadn't taken the drugs. Factual = Took drugs and recovered. Counterfactual: Patient did not take drugs, and we wonder if he would recover.

Treatment = User recommended item in email. Outcome = user bought item. Counter factual world: User did not get the item in their email. Do they end up buying the item?


In the factual world, an item cannot be both recommended and not recommended. So its necessary to apply counterfactual inot recommendation.


Causal Graph has stronger assumption than potential outcomes framework.
If Y is the child of X, then X is the direct cause of Y. If Y is a descendant of X, then it's assumed X is the potential cause of Y.

3 typical casual graphs
1. Chain
   - X->Z->Y
   - Item decides intrinsic item features and intrinsic item features decides user preference
2. Fork
   - X<-Z->Y
   - Item popularity is considered as a common cause of both item exposure and interaction probability.
3. Collider
    - X->Z<-Y
    - User click is the common outcome of both user interest and conformity.


[[Uplift Modeling]]
### Water and monster
- Traditionally, recsys recommend the items with the highest interaction probabilities. Most systems neglect the fact that the user may have taken the same action regardless. For example, if a recsys says that a user would buy a water bottle with 95% probability, and a monster 50%, typically it would recommend water bottle since it is more likely to be purchased from user. However, if the system does not recommend them water, they may have a 90% probability of being purchased, while the monster may have 20%. Recommending monster seems to be better choice because it has a higher lift of purchase probability, which may lead to more profit.



### Training with Uplift
Sampling method for observation data for an uplift-based optimization.
By observing purchase and recommendation logs for a given user, an item can either be purchased or not purchased, and recommended or not recommended. The proposed optimization samples positive and negative instances that are specific to the uplift task from the four class items. By taking the sampled labels for uplift task as ground truth, the  proposed optimization is able to learn the uplift value for user-item pairs.

A straightforward way to calculate uplift value is to estimate the counterfactual outcomes. Uses Tensor factorization with 3 dimensions as user, item, and treatment.
3d tensor with m users, n items and I treatemtns, y_m,i,t can be predicted as
pTuQi + pTudu + qtdi

pu, ui, dt are latent representation of user U, item I and treatment T

P^TQ + P^TD + Q^TD

Taking binary treatement setting as an example, the uplift value for user-item pair can be estimated by y^ u,i,t=1 - y^u,i,t=0

# Causal Effects
A basic causal effect is called the treatment effect. Its the outcome change if another treatment has been applied. The treatment effect can be measuerd at the population, treated group, subgroup, and individual levels.

[[Average Treatment Effect]] is at population. It can be used to evaluate explanations and estimate unbiased preference.
[[Average Treatment Effect on the Treated Group]] can be used to evaluate counterfacual fairness
[[Conditional Average Treatment Effect]]
[[Individual Treatment Effect]] is used to estimate uplift of recs


# Causal Estimation methods
### Random experiments
- Ideal world we would apply different treatment to the same group of individuals. Impractical in real world. The estimated [[Average Treatment Effect]] can be obained by the difference in average outcomes in two groups.
### Observational data
- Could be a shortcut for causal inference, but there are some issues.

#### Confounders
> Critical problem in observational data
[[Confounders]] are variables that affect both the treatment assignment and the outcome
- Can lead to spurious effects, like ice cream consumption and shark attacks having a relationship.
- Ice cream doesn't cause shark attacks, but both can be affected by weather
If item popularity is a confounder, it will lead to popularity bias.

The [[Simpsons Paradox]] is a phenomenon often caused by confounders. Consider this example of people taking drugs and recovered, split by gender

A/B recovered
        Drug            No Drug
Male    81/87 (93%)     234/270 (87%)
Female  192/263 (73%)   55/80 (69%)   
Total   273/350 (78%)   289/350 (83%)

In both male and female groups, If they took the drug, they have a higher recovery rate
But as a total, not taking the drug has a higher recovery rate

Compared to experimental data, observational data only provides the info about what occured, but the why a specifc treatment is token is unknown. The bias term cannot be eliminated or quantitatively measured. Therefore, bias caused by unknown treatment is a critical issue that should be handled in model design


[Simpsons Paradox]: <Simpsons Paradox.md> "The Simpson’s Paradox in the Offline Evaluation of Recommendation Systems"
[Average Treatment Effect]: <Average Treatment Effect.md> "Average Treatment Effect"
[Average Treatment Effect on the Treated Group]: <Average Treatment Effect on the Treated Group.md> "Average Treatment Effect on the Treated Group"
[Conditional Average Treatment Effect]: <Conditional Average Treatment Effect.md> "Conditional Average Treatment Effect"
[Individual Treatment Effect]: <Individual Treatment Effect.md> "Individual Treatment Effect"
[Confounders]: Confounders.md "Confounders"
[Uplift Modeling]: <Uplift Modeling.md> "Uplift Modeling"
