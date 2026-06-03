Have to find out if right now campaigns / templates passed in do additional behavior
Like campaign and templateID passed in don't soley filter for eventIDs, right

It does

## Solution
> Step 1: Get the campaign/templateID
- Currently, campaign/templateIDs are only passed in data feeds where its a paid seller template
- If we want to support scoped a/b test, we need to be able to pass in the campaign/templateID without filtering to the specfic paid seller/ campaign
- So we need to break it out
- Datafeeds that have campaign and templateID are going to need an additional arg
-  Datafeeds that didn't previously have campaign and templateID will be added
-  

> Current API when passed campaign/templateID will treat it as a filter

>Needed:
- TPP.API changes to accept an additional arg: "PaidSellerCampaign"
- Iterable - Update dataFeeds to pass "PaidSellerCampaign" where we currently pass Template/CampaignIDs
- Iterable - Update the datafeeds to pass in Template/CampaignIDs to all other data feeds
- Python API - Update request model to accept PaidSellerCampaign. Update the existing logic to only filter for eventID and accountCRMID if the new arg "PaidSellerCampaign=True" is passed in, so the current datafeeds are still being filtered.

Maybe I need to break it out. then If PaidSellerCampaign=True, do the existing logic
```python
- If PaidSellerCampaign:
# Search redis for paidseller template
# redis has the 'event_ids', 'seller_account_crmid'
# Then these args are passed to get_activity_vector_db_args
# then the elasticSearchActivitySearcher will add to filter the eventIDs
# and then accountCRMID
```
- Nit: make paid_seller_params an object, and pass paid_seller_params into VectorDBArgs.get_activity_vector_db_args
- Looks like event_ids and seller_account_crmid can both be nullabe

> Step 2: Check if AB Test enabled using the newly provided campaign/templateID
- If NOT PaidSellerCampaign, we instead check if A/B test is enabled for the specific campaign/templateID
- Redis... Just like how we would have checked campaign and templateID in redis for the paid seller campaign, we instead check if a/b test enabled
- Only allowing one a/b test at a time

- If we are good with only one a/b test at a time, we can just store a bool in redis if a/b testing on
- If we want multiple, the key in redis needs to have additional info, like what is the a/b test
- 
- Do we forsee DMK being like A/B test location for these campaigns, and categoryID for these campaigns
- ab_test:{campaign_id} = 'location_boost'
- ab_test:{other_campaign_id} = 'rerank_categories'

- 
Check global flag. 
Then check the campaign level flag.
If both are true, do the global A/B test
If global flag is off, skip everything


If we want to a/b test only this campaign
A/B test needs to be enabled
Then if campaignID/TemplateID in new redis, run the scoped A/B test
If the campaignID/TemplateID is NOT in redis, do we run the scoped A/B test config against everything?
I think not. So I think the redis key needs to have additional context of what is being tested
So if a/b testing enabled
- Need a global isScopedABTestEnabled
- 
- if campaignId/templateId in new redis: run scoped a/b test

We want to a/b test this feature against a subset of campaigns
Not test against everything



> Step 3: Start A/B Test
- Think DMK handles starting the paidseller campaign somehow
  - I really gotta figure out how they do it
  Create Marketing Email App
  L made note on 5/4 saying how working on premium Email and not previewing in recsys
  In the app, on 5/4 it got all the way up to Create and Finalize Email Step
  Email Analysis step has EventID(s), CRMID and TemplateIDs input
  The task was sent back 4 times because an EventID wasn't provided
  My guess is that the email analysis test will send out
- Alternatively. They tell us what campaigns/templates to try on
https://sandhills.snowcloud.com/Tasks/Details/820a2320-5de6-44dc-a544-ce61bb5c1ba8
- We have PaidSellerEmailCampaign.Save
- https://devops.sandhills.int/tfs/SandhillsSoftware/API/_versionControl?path=%24/API/BuyerIntelligence.API/Trunk/BuyerIntelligence.API/Controllers/PaidSellerCampaignController.cs

So my guess is the sno task step hits that API, but not 100%

So we would need sno changes

If the number of A/B tests is less than the number of premium emails



questions
- How many ab testing requests are we gonna get
- Should we just handle it? 
- So DMK just lets us know and then we update it
- If we want DMK to be able to set it or not we need sno change

> Step 4: Visualizing results. 
- Now we have the data to see viewing
