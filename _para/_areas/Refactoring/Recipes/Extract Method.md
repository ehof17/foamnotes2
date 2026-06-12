# Extract Method
> Problem: You have a code fragment that can be grouped together.
```python
def print_owning(self):
    self.print_banner()

    # print details
    print("name: ", self.name)
    print("amount:", self.amount)

```

```python
def printProperties(users):
    for i, user in enumerate(users):
        res = ""
        res += user.name
        res += " "
        res += user.age
        print(res)
```

> Solution: Move the code into a separate new method (or function) and replace the old code with a call to the method

```python
def print_owning(self):
    self.print_banner()
    self.print_details

def print_details(self):
    print("name: ", self.name)
    print("amount:", self.amount)
```

```python
def printProperties(users):
    for i, user in enumerate(users):
        print(getProperties(user))
def getProperties(user):
    return user.name + " " + user.age


```


```python
class Order:
    def calculate_total(self):
        total = 0
        for product in self.get_products():
            total += product.quantity * product.price
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



