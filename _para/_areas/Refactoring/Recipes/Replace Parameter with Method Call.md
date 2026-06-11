
# Replace Parameter with Method Call

Check what values are passed to parameters. If some of the arguments are just results of method calls of another object, use Replace Parameter with Method Call. This object can be placed in the field of its own class or passed as a method parameter.

### problem
- Calling a query method and passing its results as parameters of another method, while method could call query directly
```python
baseprice = quantity * itemprice
seasonal_discount = self.get_season_discount()
fees = self.get_fees()
final_price = discounted_price(baseprice, seasondiscount, fees)
```

### Solution
```python
base_price = quantity * item_price
final_price = discounted_price(base_price)

```
