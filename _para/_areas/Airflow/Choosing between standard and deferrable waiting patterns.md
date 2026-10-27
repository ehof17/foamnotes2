Poke, reschedule or deferrable waiting
- Choice affects how airflow uses its resources while the file is missing

Poke
Worker use: Occupied
Wake up: Polling
Best Fit: Short waits when holding worker is acceptable
Requirement: Sensor

reschedule
Worker use: Released between checks
Wake up: Scheduled checks
Best Fit: Longer polling, polling delay acceptable
Requirement: Supported mode

Deferrable
Worker use: Released
Wake up: Trigger event
Best Fit: Many idle waits
Requirement: Operator and triggerer


Setting a limit and recovery action
- Sometimes an expected delivery does not arrive
- Need a limit on the waiti and recovery action for when that time runs outcome

Declare the readiness condition precisiely
- A named marker shoud tell us which delivery is ready so the snensor is checking the intended input
Set a waiting limit that fits the delivery expectation
Task should have a defined outcome when the condition remains unmet for too long
Choose a recovery action for that outcome
Decide who checks the missing delivery and what must happen before another attempt begins


Do not wait without a limit
- Could allow a much longer wait than expected

