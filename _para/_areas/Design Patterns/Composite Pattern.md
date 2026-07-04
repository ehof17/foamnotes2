
# Composite Pattern
- Objects and containers same interface
- Like a tree structure

```python
class Organizable:
    def display(self):
        raise NotImplementedError

class Item(Organizable):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

class Container(Organizable):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, thing):
        self.children.append(thing)

    def display(self):
        print(f"Container: {self.name}")
        for child in self.children:
            child.display()
```
