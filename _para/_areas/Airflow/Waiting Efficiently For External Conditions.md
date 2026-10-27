
### Sensors
- Wait for a condition to become true
- File sensor can wait for file to be ready

### Deferral
- Lets a supported operator give up its worker slot during the wait
- A worker slot is the capacity Airflow uses to run one task

### Triggerer
- Separate Airflow service that runs triggers
- Watch for condition, like a file arriving


#### Inside or outside
Sensor waits inside a dag run that already exists
- One task may have finished preparing a destination, while another still needs an external file
- Sensor keeps the tasks that depend on that file from starting too early

Event scheduling
- Uses an event to start a new run
- Creates a dag run

### Waiting for a readiness file
- If a file tells you that a delivery is ready to use
- The file conection points to the shared marker folder

The sensor uses the connection, and the configured file path to find the readiness marker
configured
- where to look
- How often to check
- How long to wait

5 second interval asks sensor to check again after a short pause
Waiting limit decides when a missing delivery should become a fail to investigate

While waitiing, the marker is absent and the sensor stays in the running stays
In poke mode, it keeps the worker slot even between file checks

To continue, the required marker must become available


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
        poke_interval=5, # 5 seconds
        timeout=180, 
        deferrable=False #Sensor holds its worker slot for the whole wait, even between checks
    )

    @task
    def ready():
        print("delivery_ready")
        return "delivery_ready"
    
    wait_for_delivery >> ready()


```
