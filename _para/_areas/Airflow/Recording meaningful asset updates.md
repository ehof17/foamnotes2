# Publish an update only after readiness check pass
- an update tells the reporting workflow that it can use the data
- We need to check the result before making that announcement

Readiness check should cover what consumer needs
- freshness
- row count
- required columns

If validation fails, the task with the asset outlet must fail 
- Logging an error and returning normally would still count as a task success

We attach metdata that identifies the result, such as business date and how many rows passed
- Airflow records the source DAG and run on the event
Airflow records the asset update when the outlet task 
