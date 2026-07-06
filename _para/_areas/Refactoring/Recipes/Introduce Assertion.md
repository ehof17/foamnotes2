
# Introduce Assertion

### Problem
- For a portion of code to work correctly, certain conditions or values must be true

```python
def get_limit():
    return expense_limit if expense_limit != NULL_EXPENSE else primary_project.get_member_expense_list()
```

### Solution
- Replace assumptions with assertion checks

```python
def get_limit():
    valid = expense_limit != NULL_EXPENSE or primary_project is not None
    if not valid:
        raise ValueError("not valid in this function")
        
    return expense_limit if expense_limit != NULL_EXPENSE else primary_project.get_member_expense_list()

```
