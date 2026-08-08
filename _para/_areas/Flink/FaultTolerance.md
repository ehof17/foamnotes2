Flink supports
- Periodic checkpoints
- Savepoints: manual snapshots for updates/migrations
- On failure: restore to a consistent barrier across the DAG

### Exactly Once processing
- Means every record in the stream is processed once and only once, even in the presence of failures
- STRONGEST guarantee that flink provides

Checkpoint snapsho operator state periodically
If a failure occurs, go back to the last checkpoints
For sinks, there is a 2 phase commit (e.g. Kafka) or idempotent writes


