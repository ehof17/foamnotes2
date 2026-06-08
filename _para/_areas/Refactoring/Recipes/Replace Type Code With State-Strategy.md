
# Replace Type Code With State/Strategy

## Problem:
You have a coded type that affects behavior but can't use subclasses to get rid of it

class employee
- engineer: int
- salesman: int
- type: int

## Solution
Replace type code with state object. If its necessary to replace a field value with type code, another state object is "Plugged In"

Employee -> EmployeeType

Engineer and Salesman are employee type
