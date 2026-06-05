
# Decompose Conditional
Conditional operators and loops are a good clue that code can be moved to a separate method.
For conditionals, use Decompose Conditional. If loops are in the way, try [[Extract Method]].

## Problem: You have a complex conditional (if-then/else or switch).
```python
if (date < SUMMER_START or date > SUMMER_END):
    charge = quantity * winterRate + winterServiceCharge;
else:
  charge = quantity * summerRate;
```
## Solution: Decompose the complicated parts of the conditional into separate methods: the condition, then and else.
```python
if is_summer(date):
  charge = SummerCharge(quantity)
else:
  charge = WinterCharge(quantity)
```

[Extract Method]: <Extract Method.md> "Extract Method"
