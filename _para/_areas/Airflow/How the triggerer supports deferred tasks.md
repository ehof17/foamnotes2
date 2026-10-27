
Deferable sensor begins by running on a worker
Difference comes when the file is still missing and the sensor needs to wait
When the operator defers, it registers the trigger and saves the information needed to continue later
Task enters deferred state and releases worker slot


Triggerer observes the condition by running the trigger asynchronously
One triggerer can keep many waiting checks going at the same time without a worker slot for each one
Triggerer reports event when its condition is met

Once the event arrives, airflow can schedule the task to run again
The scheduler sends the work through the configured executor
The task may still need to wait for worker capacity so detecting the event does not promise an immediate finished

The worker then resumes the task by running the code provided for that step

# Responsibilites during a deferred wait
- Knowing which component handles each step helps us check why a task has not resumed
Trigger: defines the event to await
- File trigger will check for a configured file and wait for the file to be available
Triggerer: Runs triggers asynchronously, must be available for the waiting trigger to observe the condition and report 
Scheduler and worker: Resume the task and run its code

Deferred tasks and human input use distinct states
- Reading the state tells us which kind of response is still need

Deferred sensor
- waits for trigger event
- Task state is deferred
- Worker resumes after the event

Human input
- Waits for a review response
- Task state is awaiting input
- Explicit decision permits progress
