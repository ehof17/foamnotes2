# 5 contacts define a task boundary

They all have question, evidence, and failure owner

1. Purpose
- Question:  Why does it exist?
- Evidence: One observable result, suc as whether an order amount matches our rule
- Failure Owner Workflow author

2. Input
- Question:  What must arrive
- Evidence: Typed value or URI (Number or location)
- Failure Owner: Upstream task

3. Output
- Question:  What crosses to the next task?
- Evidence: Small Value or URI (should be small like count or location)
- Failure Owner: Task author

4. Observation
- Question: How is success proved?
- Evidence: Log, state, side effect
- Failure Owner: Operator

5. Retry
- Question: Can it repeat safely
- Evidence: Idempotent boundary
- Failure Owner: Service owner

A useful task boundary makes purpose, failure, and evidence explicit

> Publishing the result is a separate job, so we can repeat publishing without repeating the check
