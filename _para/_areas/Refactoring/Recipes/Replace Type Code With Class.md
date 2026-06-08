
# Replace Type Code With Class

## Problem
A class has a field that contains type code. The values of this type aren't used in operator conditions and don't affect the behavior of the program


class Person
- O: int
- A: int
- B: int
- AB: int
- bloodgroup: int

## Solution
Create a new class and use its objects instead of the type code values

class bloodgroup
- O: bloodgroup
- A: bloodgroup
- B: bloodgroup
- AB: bloodgroup
