
# Inline Class

### Problem
- A class does almost nothing and isn't responsible for anything, and no additional responsibilities are planned for it.

```python
class TelephoneNumber:
    def __init__(self, office_area_code, office_number):
        self.office_area_code = office_area_code
        self.office_number = office_number

    def get_telephone_number(self):
        return f"({self.office_area_code}) {self.office_number}"


class Person:
    def __init__(self, name, telephone_number):
        self.name = name
        self.telephone_number = telephone_number

    def get_telephone_number(self):
        return self.telephone_number.get_telephone_number()
```

### Solution
- Move all features from one class to another one


```python
class Person:
    def __init__(self, name, office_area_code, office_number):
        self.name = name
        self.office_area_code = office_area_code
        self.office_number = office_number

    def get_telephone_number(self):
        return f"({self.office_area_code}) {self.office_number}"

```
