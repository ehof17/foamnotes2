
# Extract Superclass

If inheritance is appropriate, get rid of unneeded fields and methods in the subclass. Extract all fields and methods needed by the subclass from the parent class, put them in a new superclass, and set both classes to inherit from it (Extract Superclass).

### Problem
- You have two classes with common fields and methods

```python
class Department:
    def getTotalAnnualCost(self):
        ...
    def getName(self):
        ...
    def getHeadCount(self):
        ...
class Employee:
    def getAnnualCost(self):
        ...
    def getName(self):
        ...
    def getID(self):
        ...

```
### Solution
- Create a shared superclass for them and move all identical fields and methods to it

```python
class Party:
    def getAnnualCost(self):
        ...
    def getName(self):
        ...
class Department(Party):
    def getAnnualCost(self):
        ...
    def getHeadCount(self):
        ...
class Employee:
    def getAnnualCost(self):
        ...
    def getID(self):
        ...

```
