
# Replace Conditional with Polymorphism

## Problem
- You have a conditional that performs various actions depending on an object type or properties


```python
class Bird:
    def get_speed(self):
        match type:
            case EUROPEAN:
                return getBaseSpeed()
            case AFRICAN:
                return getBaseSpeed() - getLoadFactor() * numberOfCoconuts

```

## Solution
- Create subclasses matching the branches of the conditional. In them, creaate a shared method and move code from the branched conditional into to. Then replace the conditional with the relevant method call

```python
@abstractclass
class Bird:
    @abstractmethod
    def get_speed(self):
       pass

class European(Bird):
    def get_speed(self):
        return self.getBaseSpeed()

class African(Bird):
    def get_speed(self):
        return self.getBaseSpeed() - getLoadFactor() * numberOfCoconuts

```
