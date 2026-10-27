# Improving workflow resilience and control
retries
- Give a failed task another attempt
- Use when repeating the work can resolve the problem
- Make sure partial otuput does not cause duplicate Writes

Deadlines
- Identify a delayed run
- Alert can report the delay while the workflow continues waiting

review
- Pauses work for an explicit decision
- Request needs enough context and clear choices so the person know what each answer means

Branches
- Connect a person to the path that should run
- Check both the selected path and the skipped one

Retries and execution timeouts answer two different questions
1. Can the task try again after a failure?
2. How long may each attempt run

Retries give a failed task another attempt
A temporary connection problem may clear when the next attempt runs
But, a bad input file may fail the task every time

Execution timeout
- Limits how long one attempt may run
- Airflow stops an attempt that exceeds the limit with the timeout failure
- A retry policy determines if a retry is allowed

Retry and timeout can apply to the same task


A task that recovers and a task that times out have different times out
- check recovery and execution limits separately
- Seperate timeout task intentionally leaves this Dag run failed

When a task fails, inspect error and attempt history
- Check wethter another attempt will resolve the cause
Check wether a later attempt succeeded to confirm that the task recovered

Inspect the output too, because an earlier attempt may have returned data before failing

Execution timeout puts a bound on each attempt, can limit a task to be 5-15 seconds


```python
with DAG(
    dag_id="recovery",
    schedule=None,
    start_date=datetime(2026,1,1,tzinfo=timezone.utc),
    catchup=False
):
    @task(
        retries=1,
        retry_delay=timedelta(seconds=10),
        retry_exponential_backoff=True
    )
    def recover_delivery():
        context = get_current_context()
        if context["ti"].try_number == 1:
            raise RuntimeError("First Attempt Only")
        record = {"run_id": context["run_id"], "delivery": "recovered", "records": 1}
        folder = Path(os.environ["AIRFLOW_DEMO_ROOT"]) / "data/output"
        folder.mkdir(parents=True, exist_ok=True)
        output = folder / ("recovery-" + context['run_id'] + '.json') # Uses run id in the output file, and replaces file so repeating the write is safe
        # If appended on each write, would not be safe to run
        output.write_text(json.dumps(record, indent=2), encoding="utf-8")
        print(json.dumps(record))
        return record
    
    @task(execution_timeout=timedelta(seconds=5), retrues=0)
    def bounded_wait():
        print("15 second work, 5 second limit")
        time.sleep(15)

    recover_delivery() # Goes up for retry after the first failure, tthen will suceed
    bounded_wait() # Will fail



```
