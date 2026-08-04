
#  New Flink Listing Update Router
Reads events from a pulsar topic
For each event, it checks if an update is needed, and what type using the [[Listing Update Determiner]].
If a change is needed, we get the data from source via the [[Get Listing Details Service]]
> Question: If this Flink Listing update router will have events that include the field updated, could we instead just pull the supplemental fields from ES itself?
After getting the listing details, the quality filters from recsys_data_prep need to be applied to not add junk listings to recsys

We then pass the listing details and update to the respective topic, listing_es_update or listing_gpu_inference

[Listing Update Determiner]: <Listing Update Determiner.md> "Listing Update Determiner"
[Get Listing Details Service]: <Get Listing Details Service.md> "Get Listing Details Service"
