
# Listing Update Determiner

Goal: Given a listing update payload, the service determines whether the update requires:
Nothing 
- An update to the listings embedding (GPU)
- An update to the listings payload in ES (nonGPU)

Acceptance Criteria:
1. Return NoOp for irrelevant fields
- Given the payload contains only fields that the recommendation system does not use
2. Return NoOp when relevant values have not changed
- Given the payload contains fields used by the recommendation system
- And the submitted field values match the current values stored in Elasticsearch
3. Return GPU for if fields provided affect the embedding
- Given the payload contains at least one field classified as a GPU update field
- And the submitted value differs from the current value stored in Elasticsearch
4. Return nonGPU for changed non-GPU fields
- Given the payload contains at least one field classified as a non-GPU update field
- And the submitted value differs from the current value stored in Elasticsearch
- And the payload contains NO GPU Fields

