
# Paramaterize Method

### Problem
- Multiple methods perform similar actions that are different only in their internal values, numbers, or operations

```python
class Employee:
    def fivePercentRaise(self):
        ...
    def tenPercentRaise(self):
        ...
```
### Solution
- Combine methods by using a parameter

``` python
class Employee:
    def raise(self, percentage):
        ...
```
