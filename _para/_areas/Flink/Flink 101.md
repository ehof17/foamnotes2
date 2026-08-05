# What is flink?

Distributed stream processing framework, handling [[Unbounded streams]] and [[Bounded Stream]]

Supports stateful computations: Remembers past events while processing new ones

Where flink fits:
- The middle of the modern data pipeline

Injests data from sources: Kafka, files, socke
Process data using operators, keyed state, windows
Then sends the data to sinks, like kafka, database, object store

In short, flink is the engine that transforms raw event streams into actionable insight

### How does flink work
1. Define business logic using one of Flink APIs
2. Flink executes your code in a flink cluster




[Unbounded streams]: <Unbounded streams.md> "Unbounded streams"
[Bounded Stream]: <Bounded stream.md> "Bounded stream"
