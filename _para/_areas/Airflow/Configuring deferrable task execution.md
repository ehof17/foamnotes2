# Why Defer Execution
- Release the worker during a wait

### Before delivery
- A deferred sensor is waiting for its condition
- Triggerer must be running so it can check for the event

### Event arrives
- Trigger reports that the required file is available
- Airflow can schedule the tasks to resume

### Task Completion
- Sensor succeeds
- Check wether the dependent task ran and produced the expected result

```python
from datetime import datetime, timezone
from airflow.providers.standard.sensors.filesystem import FileSensor
from airflow.sdk import DAG, task

with DAG(
    dag_id="file_readiness",
    schedule=None,
    start_date=datetime(2026,1,1,tzinfo=timezone.utc),
    catchup=False
):
    wait_for_delivery = FileSensor(
        task_id="wait_for_delivery",
        filepath="standard.ready" #check standard ready marker
        fs_conn_id="local_files",
        mode="poke",
        poke_interval=5, # 5 seconds still checks 
        timeout=180, 
        deferrable=True #Sensor can now release worker slot while the triggerer waits for the file
    )
    # FileSensor supports dispose and resume
    # Adding deferrable=True to tasks without deferrable support does not not give it 

    @task
    def ready():
        print("delivery_ready")
        return "delivery_ready"
    
    wait_for_delivery >> ready()


```
