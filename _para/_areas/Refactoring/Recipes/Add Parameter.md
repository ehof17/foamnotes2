
# Add Parameter

### Problem
- Method doesn't have enough data to do something
```python
class Customer:
    def getContact(self):
        ...
```
### Solution
- Create a new parameter to pass the necessary data
```python
class Customer:
    def getContact(self, date):
        ...
```
