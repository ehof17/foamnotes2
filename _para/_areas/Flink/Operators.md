
# Operators

Building blocks of computation
Takes one or more streams as input, transforming the data and putting it into another stream

There are different types of Operators
### Source Operators
> Purpose: Ingest data into Flink Job
- KafkaSource, FileSource

### Transform Operators
> Purpose: Apply logic to events
- map, filter, flatMap, keyBy, reduce, window

### Sink Operators
> Write processed results out
- KafkaSink, FileSink, JDBC FileSink

### Custom Operators
> Purpose: Implement domain-specific logic
- User defined functions (UDFs)

Operators can be chained (Fewer handoffs)
Operators can be parallel per operator, or global
