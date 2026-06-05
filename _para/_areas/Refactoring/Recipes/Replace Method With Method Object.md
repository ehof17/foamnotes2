
# Replace Method With Method Object

## Problem
- You have a long method in which the local variables are so intertwined that you can't apply extract method

``` python
class order:
    def price(self):
        primary_base_price = 0
        secondary_base_price = 0
        tertiary_base_price = 0

        # Perform long computation

```


## Solution
- Transform the method into a separate class so that the local variables become fields of the class. Then you can split the method into several methods within the same class.


``` python
class Order:
    def price(self):
        return new PriceCalculator(self).compute()

class PriceCalculator:
    def __init__(self, order:Order):
        # copy from the order
        self.primary_base_price = 0
        self.secondary_base_price = 0
        self.tertiary_base_price = 0
    def compute(self):
        # Perform long computation

```
