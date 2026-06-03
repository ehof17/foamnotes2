# Introduce Parameter Object

## Problem
- Your method contains a repeating group of parameters

``` python
def amount_invoiced_in(self, start:datetime, end:datetime):
    ...
def amount_received_in(self, start:datetime, end:datetime):
    ...
def amount_overdue_in(self, start:datetime, end:datetime):
    ...  
```
## Solution
- Replace these parameters with an Object
``` python
def amount_invoiced_in(self, date:dateRange):
    ...
def amount_received_in(self, date:dateRange):
    ...
def amount_overdue_in(self, date:dateRange):
    ...  
```
