
# Consolidate Duplicate Conditional Fragments

### Problem
- Identical code in all branches of conditional
```python
if is_special_deal:
    total = price * .95
    self.send()

else:
    total = price * .98
    self.send()
```


### Solution
- Move it outside
```python
if is_special_deal:
    total = price * .95
else:
    total = price * .98
self.send()
```
