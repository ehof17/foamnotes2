tests
- does dag load
- what does code do
- how it works within system

Import checks
- check loading works

Simulation checks
-  use dag.test() for a fast diagnostic loop

Unit tests
- verify graph and task logic separately

Coverage
- Add the next text where risk remains (external calls + partially completed work)

Step 1. Ensure airflow can load the Dag
Step 2. read errors
Step 3. Repair
Step 4. Prove (Reach 0 import errors)


### Dag.test vs scheduled
Dag.test()
- Fast local diagnostic loop
- Controlled logical date and Configuration
- Use inputs whos answer we already know

Scheduled tests
- Uses configured executor and airflow services
- Checks whether tasks can start and finish in that environment
