
# Move Field

### Problem
A field is used more in another class than in its own class.

```python
class Customer:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount


class Order:
    def __init__(self, customer, total):
        self.customer = customer
        self.total = total

    def final_price(self):
        return self.total - (self.total * self.customer.discount) # Orders have customers that have discounts


customer = Customer("Eli", 0.10)
order = Order(customer, 100)

print(order.final_price())
```


### Solution
- Create a field in a new class and redirect all users of the old field to it.


```python
class Customer:
    def __init__(self, name):
        self.name = name


class Order:
    def __init__(self, customer, total, discount):
        self.customer = customer
        self.total = total
        self.discount = discount

    def final_price(self):
        return self.total - (self.total * self.discount) # Orders have discounts


customer = Customer("Eli")
order = Order(customer, 100, 0.10)

print(order.final_price())  # 90.0

```
