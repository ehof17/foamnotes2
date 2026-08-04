
# ES Writer Service

Acceptance Criteria: Service that can perform two operations against Elasticsearch
- Resolves the hot ES campus before every operation
- Both operations are idempotent
Add / update
- Accepts a listing ID plus the field set to write, including embSimilarItems when present
- On add, validates that all required fields are present; rejects with a clear error naming the missing fields, and does not partially write
- On update, writes only the supplied fields and leaves the rest of the document untouched
- Writes to the resolved hot campus index
Expire
- Reads the listing's embedding from ES before deletion
- Removes the listing from the ES index
- Writes the retrieved embedding to Redis under the expired-listing key with a 3-week TTL
- If the listing is absent from ES, completes without error and without writing to Redis

>Questions: 
> Required-field list for add:  needs to come from the Task 0 schema, not be defined here
> Behavior on add for a listing ID that already exists: overwrite, or reject as a duplicate
