[[Dispensables]]
# Comments
- Method filled with explanatory Comments
- 
### Reasons for the problem
- Good intentions, when author realizes code isn't obvious or intuitive. This is like putting deodorant on fishy code smell.
> Best comment is a good name for a method or class
- If a code fragment cannot be understood without comments, change the code structure in a way that makes the comments unnecessary.
- 
#### Recipe 1
##### Extract Variable
- If a comment is intended to explain a complex expression, the expression should be split into understandable subexpressions using [[Extract Variable]]


#### Recipe 2
##### Extract Method
- If a comment explains a section of code, section can be turned into a separate method via [[Extract Method]]. The name of the new method can probably be taken from the comment text
[Dispensables]: Dispensables.md "Dispensables"

#### Recipe 3
##### Rename Method
- If comments are necessary to explain what a method does but it has already been extracted, give it a self explanatory name via [[Rename Method]]

#### Recipe 4
##### Introduce Assertion
- If you need to assert rules about a state that's necessary for the system to work, use [[Introduce Assertion]]

#### When to ignore
- When comments explain WHY something is being implemented in a particular way
- When explaining complex algorithms (When all other methods for simplifying the algorithm have been tried and come up short)


[Extract Variable]: <../Recipes/Extract Variable.md> "Extract Variable"
[Extract Method]: <../Recipes/Extract Method.md> "Extract Method"

[Rename Method]: <../Recipes/Rename Method.md> "Rename Method"
[Introduce Assertion]: <../Recipes/Introduce Assertion.md> "Introduce Assertion"
