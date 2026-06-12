[[Bloater]]
### Long method
- Too Many lines
> In c# context: Any method that is longer than 10 lines should make you start asking questions

#### Reason
- Hotel California. Something is always being added to a method but nothing is ever taken out. Its easier to write code than read it, the smell is unnoticed.

- But its a see saw. SInce its harder to create a new method than to add an existing other_thing

Hardness
Add To method < Create new method 


#### Treatment
- IF you need to comment on something in a method, the code should be its own method
- Since trhe method name will describe it

##### Recipe 1
[[Extract Method]]

###### Extract method

#### Recipe 2
[[Reduce Local Variables and Parameters Before Extracting a Method]]

#### Recipe 3
[[Replace Method With Method Object]]
#### Recipe 4
[[Conditionals and Loops]]
Conditional operators and loops are a good clue that code can be moved to a separate method.
For conditionals, use [[Decompose Conditional]]. If loops are in the way, try [[Extract Method]].





[Replace Method With Method Object]: <Recipes/Replace Method With Method Object.md> "Replace Method With Method Object"
[Conditionals and Loops]: <Recipes/Conditionals and Loops.md> "Conditionals and Loops"

[Extract Method]: <Recipes/Extract Method.md> "Extract Method"
[Reduce Local Variables and Parameters Before Extracting a Method]: <Recipes/Reduce Local Variables and Parameters Before Extracting a Method.md> "Reduce Local Variables and Parameters Before Extracting a Method"

[Decompose Conditional]: <Recipes/Decompose Conditional.md> "Decompose Conditional"
[Bloater]: Bloater.md "Bloaters"
