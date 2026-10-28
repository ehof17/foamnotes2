A scheduled run needs a clear period of data to process


Schedule tells airflow when it can create a run
Which period of data that run covers is a separate decision

For time, the logical date assigned to the run is different than the time its task actually starts

To fill gaps in history, we can let catchup create missing scheduled runs or request a backfill for selected dates

A custom timetable lets us contain business rules like skipping weekends and holidays


### The schedule creates runs, the interval defines the work

With a data interval time table, each run also gets a start and end period of what it should process

Schedule: 
- Purpose: Run Eligibility
- Time reference: Configured Timezone
- Data Interval: Timetable Rules
- Responsible component: Scheduler

Run: 
- Purpose: One execution
- Time reference: Actual Execution Times
- Data Interval: Assigned Interval
- Responsible component: Airflow

EAch run records its assigned interval and actual execution times
A late start does not change the period it was meant to process

Data: 
- Purpose: Rows to process
- Time reference: Interval bounds
- Data Interval: Start inclusive, end exclusive
- Responsible component: Task

Before enabling the schedule. let us check which business day it will process
The UTC settigns, next run, and business window need to agree
We want to catch a shifted date before processing any rows
Configure
- Recurrence
- Date bounds
- catchup settigns

Inspect sample data interval
- DAG stays paused so we will calculate that interval with a short command

Prove - check the interval covers the intended business window

### One run carries for time concepts
When can airflow create the run
- Schedule trigger answers that question
- With a data interval timetable, the period must end before its scheduled run can be created

The logical date is assigned by the timetable
- With a data interval timetable, it makes the start of the period the run represents

Which row belongs in this run
- Data interval gives us the start and end that task code can use to select them

Execution time tells us when the task actually runs
- Even if it starts the next day, it should still process the assigned interval

> 2 schedules can use the same clock rule but assign different data windows, the type of timetable makes the Difference

A trigger style schedule starts a run at a chosen time, like 6 am every morning
With its default zero length interval, that time also becomes the logical date
Does not automatically mean the previous business day
A trigger timetable can have an explicit interval, so check how it is configured


If the timetable doesn't supply the range we need, task code must define which rows to read

Datetime interval schedule assigns a start and end for a daily interval
Airflow normally creates a run after the day ends, so the task can process the whole day
The logical day stays with the interval
A late start or retry still refers to the same period
Reaed the interval from the task context and use it in the query
Use the same period in the output name so the result is easier to Identify

What if some earlier periods still need processing?
[[Catchup and Backfills]]
