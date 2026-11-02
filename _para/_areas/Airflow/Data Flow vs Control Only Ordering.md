### Data flow
- pass one task output to the next
- Airflow creates the dependency so the next task waits for the result.
- We will pass a small value, the order count. The order row stays in the database.
- Graph connects the task that produces the value to the one that uses It

### Control only ordering
- Use first wait >> second
- Connection passes no value
- The next task reads any data it needs separaetley.
- Use this when order alone matters


### Verify direction, fan out, and cycles
Arrow should lead from the task that must finish first to the one that waits for it. Check the direction so we dont make the wrong task wait
One task can feed many others (Fanout). They may run together when their other requirments are met and resources are available
Several tasks may lead into one task (Fan in) its trigger rule tells airflow which outcomes from those earlier tasks will allow it to start
Cycle (leads back to an earlier task). It gets fuggin cancelled because Dag is not cycled
Each edge needs a reason... 
