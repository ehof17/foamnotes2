
# Encapsulate Field

### Problem
- You have a public field
``` python
class Employee:
    def __init__(self, salary):
        self.salary=alary
```

### Solution
- Make it private and set access methods

```python
class Employee:
    def __init__(self, salary):
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value

```
