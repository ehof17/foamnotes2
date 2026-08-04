
# RecSys NRT - Flink ES worker
RecSys NRT - Flink ES worker
There a few ways to set this worker up. There are 3 operations that will come through, add, update, and delete. Each one before performing a write operation will need to check which elastic campus is hot and only write to the hot campus

Add and update
These should be treat in much the same way where we update the ES payload with the new values

Delete
We will need to pull down the embSimilarItems and store this in redis under the listingId with a TTL of 3 weeks.

