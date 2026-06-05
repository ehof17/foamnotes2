Overall goal: do different strategies at a given template/campaignID
Secondary goal: test things at a given template campaign id

Scoped redis key: Are we testing the provided campaign?
Scoped a/b test config: If we are testing the camapign, what are the strategies and ratio of testing




What to put in redis
- bool enabled

campaignID=xxxx

redis
xxxx = True

python
ScopedABTestConfig = if True, do location boosting

If dmk says its good:
- Will need to somehow get white listed campaigns/templateIds to use the new strat
- In the location boost case we will 100% need a new datafeed to start passing in location args.


If we want to do it on every req

redis
xxxx = location_boost

python 
ABTestConfig = read_redis

If dmk says everything is good
- flip redis to be 100% of the strategy

Then if dmk wants to use the location boost strategy again, the templateID/CampaignID needs to be added to the whitelist


#### Adding an arg instead
- If we add an arg to a datafeed per strategy, then dmk could just use the new datafeed
- Pro: DMK doesn't need to ask us every time to white list
- Con: Adding more datafeeds. Could mean a new datafeed per strategy
