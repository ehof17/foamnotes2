If data comes from outside airflow, like a file being dropped into a folder

We need a way to handle repeated signals and interrupted work

External revents require clear owenership and Replay
- When an external event starts our work, part of the job belongs to another system
- We need to agree on who handles each part

Boundary
- Decide: Does source send notifcation? Does Airflow check for new data?

Watcher
- NEeds to detect a new arrival without starting more work every time it finds the same file

partition
- identifies part of the data such as one business day
- That key helps us select the same data when we need to process it again

Operations
- Decide who handles delivery failure, duplicate events, and unfinished work

### Comparing push and pull triggers trade different responsibilities
> A new file arrives. Can its source **push** a notifcation to airflow, or does airflow need to **pull** by checking for the file

Push Trigger
- External system delivers the event
- Authenticated api can deliver event promptly
- Sender owns the retries and deduplication

Pull Watcher
- Airflow observes the condition
- It can detect a file in a landing folder, even when the source cannot send a notifcation
- The connection goes outbound from airflow. When pulling, choose how often to check based on the delay and load you expect
- Watcher needs a recovery policy too. If it stops after detecting a file, it must be able to check wether the arrival was reported or still needs handling

>Before choosing either approach, check how it will handle delivery and interrrupted work
**Push** depends on delivery.
Can the source
- Authenticate
- Send the event
- Retry if it loses the response?

**Pull** depends on observation.
Can airflow
- Find the arrival later and tell if it was already handled

Both **Push** and **Pull** need a recovery plan.
We identify the event and check how far its work got. Then decide which system retries delivery or continues order_processing

We do not check an ordinary dag task for every file check, we will send one arrival at a time and wait for intake to finish before sending another
