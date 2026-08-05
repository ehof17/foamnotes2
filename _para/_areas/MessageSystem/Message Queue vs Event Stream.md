# Message Queue vs event stream

## Message Queue
- Task distribution
- Like a todo list where tasks are picked up by different workers
- One to One message consumption
- Short term storage, auto deleted
- Good for request response, job queue
- Use message queue when jobs need to be distrubted across multiple workers, like processing orders in ecommerce

## Event stream
- continuous data stream
- Live feed of events
- One to many broadcasting, multiple consumers can read the same event independently
- Retain history for replay
- Event driven architectures, log processing
- Use event stream when processing real time events like tracking user activity
