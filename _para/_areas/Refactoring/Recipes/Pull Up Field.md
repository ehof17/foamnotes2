
# Pull Up Field

### problem
- 2 classes have the same fields
``` python
class Unit:
    pass
class Soldier(Unit):
    health:int
class Tank(Unit):
    health:int
```

### Solution
- Remove the field from subclasses and move it to super
``` python
class Unit:
    health:int
class Soldier(Unit):
    pass
class Tank(Unit):
    pass
```
