[[Change Preventers]]
# Divergent Change
You find yourself having to change many unrelated methods when you make changes to a class. For example, when adding a new product type you have to change the methods for finding, displaying, and ordering products.
### Reasons for the problem
- copypasta programming, poor strucuture


#### Recipe 1
[[Extract Class]] to split up behaviors

#### Recipe 2
Combine Classes through Inheritance
If different classes have the same behavior, you may want to combine the classes through inheritance ([[Extract Superclass]] and [[Extract Subclass]]).



[Change Preventers]: <Change Preventers.md> "Change Preventers"
[Extract Class]: <../Recipes/Extract Class.md> "Extract Class"

[Extract Superclass]: <../Recipes/Extract Superclass.md> "Extract Superclass"
[Extract Subclass]: <../Recipes/Extract Subclass.md> "Extract Subclass"
