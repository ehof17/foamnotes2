
# Preserve Whole Object.mb

## Problem
- You got several values from an object then pass them as parameters to a method

```python
low = day_range.get_low()
high = day_range.get_high()
within_plan = plan.within_range(low, high)
```

## Solution
- Pass the whole object
```python
within_plan = plan.within_range(day_range)
```
