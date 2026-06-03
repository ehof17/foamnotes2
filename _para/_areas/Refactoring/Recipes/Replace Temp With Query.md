
# Replace Temp With Query

## Problem
- You place the result of an expression in a local variable for later use in your code

```python
def calculate_total():
    baseprice = quantity * itemprice
    if baseprice > 1000:
        return baseprice * .95
    else:
        return base_price * .98
```
## Solution
- Move the entire expression to a separate method and return the result from it. Query the method instead of using a variable. Incorportate the new method in other methods, if necessary

```python
def base_price():
    return quantity * item_price

    baseprice = quantity * itemprice
    if baseprice > 1000:
        return baseprice * .95
    else:
        return base_price * .98
def calculate_total()
    if base_price() > 1000:
        return base_price() * .95
    else:
        return base_price() * .98
