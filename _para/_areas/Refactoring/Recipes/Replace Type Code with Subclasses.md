
# Replace Type Code with Subclasses

## Problem
You have a coded type that directly affects program behavior
Ie values of this field trigger various code in conditionals

class employee
- engineer: int
- salesman: int
- type: int
- 


## Solution
Create subclasses for each value of the coded type. Then extract the relevant behaviros from the original class to these subclasses. Replace the control flow code with polymorphism

Engineer extends employee
salesman extends employee
