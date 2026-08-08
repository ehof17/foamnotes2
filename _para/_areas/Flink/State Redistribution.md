> What happens if you change a job's parallelism?

Flink automatically distributes state.

[[Keyed State]]: Records are rehashed: same keys map to new set of subtasks

[[Operator State]]: Union or round robin redistribution, ensuring no state is lost


[Keyed State]: <Keyed State.md> "Keyed State"
[Operator State]: <Operator State.md> "Operator State"
