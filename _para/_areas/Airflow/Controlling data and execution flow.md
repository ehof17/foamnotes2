# Controlling data and execution flow

Dependencies tell tasks when to wait, but how does one task get a result from another?

How do we change a setting for one run or choose a different path?


> Pass small values between tasks
> Separate run settings from shared settings
> Use branches and triggered rules to control what runs


4 choices about what each task receives and which path runs next

1. XCom: Passes a small result, like a count to the next task
2. Configuration
   1. Param is for one run
   2. Variable is a setting many runs shared
   
3. Branching
- An input or earlier result determines which path should run
- Tasks can be skipped 

4. Joins
- One task waits on several upstream tasks. Its trigger rule looks at all their states and determine if it can run


When to use each thing?

| x  | Example | Size   | Use | Store   |
|---|---|---|---|---|
| Count  | 42  | Tiny   | Coordinate  |  Xcom |
| Status  | Approved | Tiny | Decide  | Xcom  |
|  Orders | Order Rows  | Large  |  Process | External  |
