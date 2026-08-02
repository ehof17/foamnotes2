
# Encaspulate Collection

## Problem
- Class contains a collection filed and a simple getter and setter for working with the collection

```python
class Person:
    self._courses:set = {}
    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, value:set):
        self._courses = value

```
## Solution
- Make getter returned value read only and create methods for adding/deleting elements of the collection
```python
class Person:
    self._courses:frozenset = frozenset({})
    
    @property
    def courses(self):
        return self._courses

    def addCourse(self, value:Course):
        ...
    def removeCourse(self, value:Course):
        ...

```
