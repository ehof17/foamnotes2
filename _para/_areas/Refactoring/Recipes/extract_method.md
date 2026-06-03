# Extract Method
> Problem: You have a code fragment that can be grouped together.
```python
def print_owning(self):
    self.print_banner()

    # print details
    print("name: ", self.name)
    print("amount:", self.amount)

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
