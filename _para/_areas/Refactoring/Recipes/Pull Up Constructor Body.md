
# Pull Up Constructor Body

### Problem
- Subclasses have constructors with mostly identical code

```python
class Employee:
    pass
class Manager(Employee):
    def __init__(self, name, id, grade):
        self.name=name
        self.id=id
        self.grade=grade
class Admin(Employee):
    def __init__(self, name, id, admin_id):
        self.name=name
        self.id=id
        self.admin_id=admin_id

```


### Solution
- Create a superclass constructor and move code thats the same in the subclasses to it. Call the superclass constructor in the subclass constructors
```python
class Employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id

class Manager(Employee):
    def __init__(self, name, id, grade):
        super().__init__(name, id)
        self.grade=grade
class Admin(Employee):
    def __init__(self, name, id, admin_id):
        super().__init__(name, id)
        self.admin_id=admin_id

```
