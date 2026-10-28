# Timetable owns business-date rules
- Decides which intervals airflow creates
- Holiday check inside a task makes a different decision -> Wether a dag run should continue after it already exists


Example rules
- Normal workday: needs one interval
- Normal weekend: skip the day
- Holiday: Can fall on weekday or weekend


#### Prove exactly one intended run per business date
**Generate** the interval for a normal workday and compare it with expected dates
A second candidate for the same date would reveal a dupication problem
**Adjust** for the weekend check for expected skip or move. If the work is assigned to the wrong day that is a failure
**Apply** The holiday calendary
**Boundary** Test exact cutoff and the instance on either side. Look for missing interval or two candidates for same busineess day
**Result** Each day has the intended run



```python
def order_processing():
    @task.short_circuit # 
    def check_holiday():
        run = get_current_context()['dag_run']
        run_date = run.conf.get("run_date") or run.run_after.date().isoformat() # normally uses run schedule date from run after
        # but run configuration can try chosen date
        holidays = {"2026-09-07"}
        print(f"RUN_DATE={run_date}, HOLDAY={run_date in holidays}")
        return run_date not in holidays

    @task
    def dumb_task():
        print("this task will be skipped if short circuited")

    received = receive_orders() 
    # If check holiday is false, its defauly behaviro skips every downstream task regardless of the task trigger rule. Including notify and finish
    check_holiday() >> received 

```

# Never choose a schedule before defining the data interval it represents
