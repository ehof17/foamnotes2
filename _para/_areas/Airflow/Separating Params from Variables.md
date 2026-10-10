
# Params express intent
# Variables hold Configuration


Params
- Express intent for one run
- Like minimal order amount without changing the code
- Schema can accept numbers and reject text. Chosen value will be saved at the run Configuration

Variable
- Shared settings
- Like where to publish result
- Several Dags can read that setting 
- Changing a varaible can affect later tasks that read it.
- THe new value can apply across runs even though the task code stays the same
- Only authorized owners should be able to update variables
