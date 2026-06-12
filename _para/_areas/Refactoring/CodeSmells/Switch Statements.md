# Switch Statements
- You have a complex switch operator or sequence of if Statements

### Reasons for the problem
- Rare use of switch and case operators is a hallmark of object oriented code.
- Often code for a single switch statement can be scattered in different places in the program
- When a new condition is added, you have to find all the switch code and modify it

> If you see `switch` you should think of polymorphism
#### Recipe 1
Isolate the `switch` operator
You may need [[Extract Method]] and then [[Move Method]]
