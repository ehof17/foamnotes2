
# Extract Variable

### Problem
- You have an expression that is hard to understand

```python
if ((platform.upper().get("MAC") > -1) and (browser.upper().IndexOf("IE") > -1) and self.wasInitialized() and resize > 0 ):
        pass
```

### Solution
- Place results of expression in separate, self explanatory variables

```python
isMacOs = platform.upper().get("MAC") > -1
isIE = browser.upper().get("IE") > -1
wasResized = resize > 0
if (isMacOs and isIE and self.wasInitialized() and wasResized):
    pass
 

```
