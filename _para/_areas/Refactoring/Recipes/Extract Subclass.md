
# Extract Subclass

## Problem
- Class has features that are only used in certain cases

JobItem
- getTotalPrice
- getUnitPrice
- getEmployee()

## Solution
- Create a subclass and use it in these cases


JobItem
- getTotalPrice
- getUnitPrice
- getEmployee()
      ^
      |
LaborItem
- getUnitPrice
- getEmployee

