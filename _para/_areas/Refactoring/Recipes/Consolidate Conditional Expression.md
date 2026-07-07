
# Consolidate Conditional Expression

### Pronlem
- Multiple conditionals lead to same result or action

```python
def disability_amount(self):
    if self.seniority < 2:
        return 0
    if self.months_disabled > 12:
        return 0
    if self.is_part_time:
        return 0

    # compute disability..
    

```

### Solution
- Convert this to a single expression
```python
def disability_amount(self):
    if self.is_not_eligible_for_disability():
        return 0
    # compute disability..
    

```
