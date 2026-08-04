
# Get Listing Details Service

- Recsys_data_prep gets listing details from a variety of sources. To help with the flink job, it would be nice to pull this logic out of recsys data prep and into its own standalone service. We can provide a listingID or batch of listingIDs, and the service gets all the columns requested from their original source.
