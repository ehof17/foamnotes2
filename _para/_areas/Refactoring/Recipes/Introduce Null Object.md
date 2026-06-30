
# Introduce Null Object

## Problem
- Since some methods return null instead of real objects, you have many checks for null in your code.


``` python
if not customer:
    plan = BillingPlan.basic()
else:
    plan = customer.getPlan()
```

## Solution
- Instead of `null` return a null object that exhibits the default behavior

```python
class NullCustomer(Customer):
    @override
    def isNull(self):
        return True

    @override
    def getPlan(self):
        return NullPlan()

customer = order.customer if order else NullCustomer()
plan = customer.getPlan()
```




