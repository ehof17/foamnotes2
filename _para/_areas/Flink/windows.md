
# windows

Allow batches of a continous stream to be processed.

### Tumbling
> Fixed, non-overlapping intervals
- Use case
  - Click counts every 5 minutes
### Sliding
> Fixed size, overlapping windows (with slide)
- Use case
  - Tracking rolling 1 minute averages every 10 seconds
### Session
> Based on inactivity gaps instead of timedelta
- Use case
  - Group user activity sessions with 30s gaps, browsing sessions
### global
> Process entire stream (bounded or triggered)
- Use case
  - Full dataset aggregations
