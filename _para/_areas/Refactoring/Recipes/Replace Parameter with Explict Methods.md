
# Replace Parameter with Explict Methods

## Problem
- Method is split into parts, each of which is run depending on the value of a parameters


```python
def setValue(self, name, value):
    if name == 'height':
        self.height = value
        return
    if name == "width":
        self.width = value
        return
```

## Solution
- extract individual parts into their own method and call them instead of the original
```python
def setHeight(self, value):
    if name == 'height':
        self.height = value
        return
def setWidth(self, value):
    self.width  = value
    return
```

