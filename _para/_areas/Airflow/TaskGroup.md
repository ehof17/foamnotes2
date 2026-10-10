
## TaskGroup
- can group related tasks into a group, like validate_orders and check_quality into a group called validation


Uses a stable group id
Keep task state visibile

Incoming edge 
- connects to the indendended entry 
- Should connect to the task in the group that actually needs the earlier work.
- Then, no other task in the group waits for a reason we cannot se

Outgoing edge
- leaves terminal task
- does not change execution


Just for navigation, it doesnt rrun as a single task


