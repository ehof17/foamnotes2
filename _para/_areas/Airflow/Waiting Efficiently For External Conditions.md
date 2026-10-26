
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

Event scheduling needs
