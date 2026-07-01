
# Replace Inheritance with Delegation

If inheritance makes no sense and the subclass really does have nothing in common with the superclass, eliminate inheritance in favor of Replace Inheritance with Delegation.

### problem
- Superclass only uses a portion of the methods of its superclass (or its not possible to inherit superclass data)


```python
class Vector:
    def is_empty(self):
        pass

class Stack(Vector):
    pass
```

### Solution
- Create a field and put a superclass object in it, delegate methods to the superclass object, and get rid of inheritance

```python
class Vector:
    def is_empty(self):
        pass

class Stack:
    def __init__(self, vector:Vector):
        self.vector = vector
    def is_empty(self):
        return self.vector.is_empty()
```

