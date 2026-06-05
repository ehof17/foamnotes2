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
