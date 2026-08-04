RecSys NRT - Flink listing update router
This will be a flink job that reads a pulsar topic, checks if the columns updated from the webhook are important to recsys quits early if not, deduplicates listing_ids (should be rare, but needs to take the union of all columns changed), get listing_details from web's listing master index, get supplemental data from a few other endpoints, should all be done async at the same time, decide if the update is and add, update, or delete. If an add or update with gpu inference need write it to the gpu inferenc pulsar topic. If a delete or not in need of gpu resources we write to the ES write pulsar topic.

During this process we will also need to copy the quality filters from recsys_data_prep to not add junk listings to recsys
