
# Extract Interface

## Problem:
- multiple clients are using the same part of a class interface
- Another case: part of the interface in two classes are the same

## Solution:
- Move the identical portion to its own interface

Employee
- getRate
- hasSpecialSkill
- getName
- getDepartment

Interface(Billable)
- getRate()
- hasSpecialSkill



multiple clients are using the same part of a class interface

super.getRate()
