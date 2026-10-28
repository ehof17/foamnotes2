# Catchup and Backfills


Catchup and backfill solve different problems.
Catchup when the scheduler should creates runs for missing intervals that are eligible under the DAG schedule
Catchup follows that schedule back to its start date

Don't use catchup for a few chosen missing dates
- Turning it on for a few chosen dates can create other missing scheduled runs too
- A backfill covers the range we request
Do not the skip the run preview, compare the candidate dates with existing run states and the reprocesisng policy before submitting
The checks determine which runs can actually be created

Do not use catchup to replace a controlled backfill
A backfill gives us range date and a concurrency limit so we can control how much historical work runs together


Before creating historical runs, preview the work so we can check which dates actually need processing

Request
- Command intent: Name the date range
- Creates work: No
- Evidence: Check the requested interval
- Decision: continue to preview

Preview
- Command intent: List candidate run
- Creates work: No
- Evidence: Compare the candidate runs with the existing runs
- Decision: Approve only gaps

Execute
- Command intent: Create approved runs
- Creates work: Yes
- Evidence: Check run ids and itervals to confirm that the missing periods are covered
- Decision: Verify no duplicates
