# Data clumps
- Sometimes different parts of code contain identical groups of variables (Like db connection params). These should be made into their own classes

### Reasons
- Poor structure
- CopyPasta
- Quick test. Delete one of the data values, and if the other values DONT make sense, this is a sign that the variables should be combined into an object
- 
#### Recipe 1
[[Extract Class]]
If repeating data comprises the fields of a class, use this to move the fields into their own class

#### Recipe 2
[[Introduce Parameter Object]]
If the same data clumps are passed in the parameters of methods, use this to set them off as a class

#### Recipe 3
[[Preserve Whole Object]]
If some data is passed to other methods, think about passsing the entire data object to the method instead of just individual fields

#### Recipe 4
Look at the code used by these fields. It may be a good idea to move the code into data class


# When to ignore
- Passing entire object in the paramets of a method, instead of passing just its values (primitive types), may create undesirable dependency between the 2 classes.

[Extract Class]: <../Recipes/Extract Class.md> "Extract Class"
[Introduce Parameter Object]: <../Recipes/Introduce Parameter Object.md> "Introduce Parameter Object"

[Preserve Whole Object]: <../Recipes/Preserve Whole Object.md> "Preserve Whole Object.mb"
