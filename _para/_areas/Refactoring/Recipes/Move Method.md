
# Move Method

## Problem
- A method is used more in another class than its own class
```python
class Order:
    def calculate_total(self):
        total = 0

        for product in self.get_products():
            total += product.quantity * product.price

        return self.apply_regional_discounts(total)

    def apply_regional_discounts(self, total):
        match self.user.get_country():
            case "US":
                return total * 0.85
            case "RU":
                return total * 0.75
            case "CN":
                return total * 0.9
            case _:
                return total
```

## Solution
- Create a new method in the class that uses the method the most, then move code from the old method to there. Turn the code of the original method into a reference to the new method in the other class or remove it entirely

```python
class Order:
    def calculate_total(self):
        ...
        total = Discounts.apply_regional_discounts(total, user.getCountry())
        total = Discounts.applyCoupons(total)



class Discounts:
    def applyCoupons(total):
        ...

    def apply_regional_discounts(self, total, country):
        match country:
            case "US":
                return total * 0.85
            case "RU":
                return total * 0.75
            case "CN":
                return total * 0.9
            case _:
                return total
    
```



