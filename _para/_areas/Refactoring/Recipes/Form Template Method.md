
# Form Template Method

### Problem
- Subclasses implement algs that contain similar steps in the same order

```python
class Site:
    pass
class ResidentialSite(Site):
    def get_billable_amount(self):
        base = self.units * self.rate
        tax = base * TAX_RATE
        return base + tax
class LifelineSite(Site):
    def get_billable_amount(self):
        base = self.units * self.rate * .5
        tax = base * TAX_RATE * .2
        return base + tax

``` 
### Solution
- Move the algorithm structure and identical steps into a superclass, leave different implementations on the different steps in the subclass
```python
class Site:
    def get_billable_amount(self):
        return self.get_base_amount() + self.get_tax_amount()

    @abstractmethod
    def get_base_amount(self):
        raise NotImplementedError()

    @abstractmethod
    def get_tax_amount(self, base):
        raise NotImplementedError()
    
class ResidentialSite(Site):
    def get_base_amount(self):
        return self.units * self.rate
    
    def get_tax_amount(self, base):
        return base * TAX_RATE

class LifelineSite(Site):
    def get_base_amount(self):
        return self.units * self.rate * .5
    
    def get_tax_amount(self, base):
        return  base * TAX_RATE * .2


``` 
