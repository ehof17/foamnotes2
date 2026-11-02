# What should allow the workflow to start?

### Time
- Recurring business window
- Check the tasks reads the right interval, even if it starts late

### Asset
- When another workflow must make data ready first
- Use partitioning scheduling when a consumer needs a particular part of the data

### Watcher
- When airflow needs to direct the arrival
- Must also recognize an arrival it already handled

### Push API
- When the source can notify airflow
- 


> Before enabling the workflow, check what should happen if delivery or processing stops partly through

Name the signal that starts the work
- ie. an interval ending or a file arriving

This tells us which even we are recovering

Save enough state to tell whether the event was detected, claimed, or fully processed

Assign a retry owner for event delivery and task execution.

Define recovery for affected event, run or partition

Every exernal trigger needs a clear signal, state, retry owner, and recovery plan.
Decide how to track completed work and recover what is unfinished. Keep the business date with the work so you can recover the intended batch without repeating completed steps
