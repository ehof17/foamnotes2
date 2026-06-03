### Bloaters
- Huge. Hard to work with
- Usually don't crop up at a time, but increase over time. Will only get worse

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
[[[_para/_areas/Refactoring/Refactoring/Recipes/extract_method.md]]]

###### Extract method

#### Recipe 2
[[_para/_areas/Refactoring/Refactoring/Recipes/Reduce Local Variables and Parameters Before Extracting a Method]]

#### Recipe 3
[[Replace Method With Method Object]]
