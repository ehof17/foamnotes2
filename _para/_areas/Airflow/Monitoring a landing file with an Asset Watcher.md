# A watcher creates one Airflow Event
AssetWatcher connects a file arrival to an asset update that can start intake


External signal
- flag file
- customer trigger moves it to a claimed path
- taking it out of the location being watched

The triggerer runs that trigger code
After moving the flag, the triggerer sends and event with the claimed path
Airflow records the asset update, and checks whether it can schedule intake

To check recorded result, follow the asset event into a successful intake run
Then list the folder to confirm that the claimed flag is get_current_context

Moving the flag prevents repeated detection
We also need to know whether intake finished processing it.
A claim marks the flag as taken. Processing can still stop afterward. The claim alone cannot guarantee the work finishes exactly once

Observe a new flag at the landing path that tells the watcher there is work to pick up

The trigger claims the flag by moving it, then sends the event
- If it stops between those actions, the file has moved, but the event may be missing
- Recovery must handle that gap
- When intake completes, it removes the claimed flag. We will add a fresh flag and check that it starts new work.


