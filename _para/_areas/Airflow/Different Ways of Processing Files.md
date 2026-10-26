## Different ways of processing files change how airflow tracks and retries that work

### Fixed task
- Dag code defines graph before run
- Work well when required stages are known
- Changing the number requires code change

### task loop
- several files inside one task instance
- Airflow sees one state for whole loop
- If the task fails on the last file, a retry task starts that task
- its code must handle any work completed

### [[mapped tasks]]
- each input has its own instance, state and attempt history
- If one file fails, all other files won't be treated
- Number of instances can change from run to run

### When to need runtime expansion?
- Ask question
- Does the input count change between runs?
  - For the order processing, the number of files processed changes day to day. So each file needs its own task outcome, so separate instances can help us see what files
- Can an upstream task find the files during the run,
