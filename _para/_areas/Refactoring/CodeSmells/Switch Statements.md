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


#### Recipe 2
Get rid of Type Codes
If a `switch` statement is based on type code, such as when the program's runtime mode is switched, use [[Replace Type Code with Subclasses]] or [[Replace Type Code With State-Strategy]]

#### Recipe 3
Replace Conditional with polymorphism
After specifying the inheritance strucuture, use [[Replace Conditional with Polymorphism]]


#### Recipe 4
Replace Parameters `switch`ing with explicit methods
If there aren't many conditions in the operator, and they call the same method with different parameters, polymorphism is superfluous. Instead, break the method into smaller methods
[[Replace Parameter with Explict Methods]]


#### Recipe 5
Introduce null object
If one of the conditional options is null, use [[Introduce Null Object]]


### When to ignore
- When a switch operator is simple
- When a switch operator is used in Factory / Abstract factory


[Extract Method]: <../Recipes/Extract Method.md> "Extract Method"
[Move Method]: <../Recipes/Move Method.md> "Move Method"

[Replace Type Code with Subclasses]: <../Recipes/Replace Type Code with Subclasses.md> "Replace Type Code with Subclasses"
[Replace Type Code With State-Strategy]: <../Recipes/Replace Type Code With State-Strategy.md> "Replace Type Code With State/Strategy"

[Replace Conditional with Polymorphism]: <../Recipes/Replace Conditional with Polymorphism.md> "Replace Conditional with Polymorphism"
[Replace Parameter with Explict Methods]: <../Recipes/Replace Parameter with Explict Methods.md> "Replace Parameter with Explict Methods"

[Introduce Null Object]: <../Recipes/Introduce Null Object.md> "Introduce Null Object"
