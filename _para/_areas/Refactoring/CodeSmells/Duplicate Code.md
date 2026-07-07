[[Dispensables]]
# Duplicate code
- 2 code fragments look identical

# Reasons for the problem
- Multiple programmers working on diff parts of same program at same time
- Also subtle version, where 2 code look different, but does the same job. This is harder to find/fix
- Sometimes duplication is purposeful. Its often way faster to copy + paste working code and not declutter

#### Recipe 1
##### Same class: Extract method
If the same code is found in 2 or more methods in the same class, [[Extract Method]] and place the calls to the new method

#### Recipe 2
##### Subclasses: Extract method
If the same code is found in 2 subclasses of the same level, [[Extract Method]] for both classes, then [[Pull Up Field]] for fields used in method that is being pulled up

#### Recipe 3
##### Subclasses: Pull up constructor body
If the same code is found in 2 subclasses of the same level, and the duplicate code is inside a constructor [[Pull Up Constructor Body]]

#### Recipe 4
##### Subclasses: Form Template Method
If the same code is found in 2 subclasses of the same level: If the duplicate code is similar but not completely identical, use [[Form Template Method]]

#### Recipe 5
##### Subclasses: Substitute algorithm
If the same code is found in 2 subclasses of the same level: If the 2 methods do the same thing but use different algorithms, select the best one and apply [[Substitute Algorithm]]

#### Recipe 6
##### Different classes: Extract superclass
If the same code is found in 2 different classes: If they are not part of a hierarchy, use [[Extract Superclass]] to create a single superclass that maintains all the previous functionality

#### Recipe 7
##### Different Classes: Extract class
If the same code is found in 2 different classes: If it's difficult or impossible to create a superclass, use [[Extract Class]] in one class and use the new component in the other.

#### Recipe 8
##### Consolidate Conditional Expression + Extract Method
- If a large number of conditional expressions are present and perform the same code (Only differing in conditions), merge operators into a single condition using [[Consolidate Conditional Expression]] and use [[Extract Method]] to place the condition in a separate method with an easy to understand name

#### Recipe 9
##### Consolidate Duplicate Conditional fragments
If the same code is perfomed in all branches of conditional expression: place identical code outside of the condition using [[Consolidate Duplicate Conditional Fragments]]

### When to ignore
- If it makes code less intuitive and obvious..
[Dispensables]: Dispensables.md "Dispensables"
[Extract Method]: <../Recipes/Extract Method.md> "Extract Method"

[Pull Up Field]: <../Recipes/Pull Up Field.md> "Pull Up Field"
[Pull Up Constructor Body]: <../Recipes/Pull Up Constructor Body.md> "Pull Up Constructor Body"
[Form Template Method]: <../Recipes/Form Template Method.md> "Form Template Method"
[Substitute Algorithm]: <../Recipes/Substitute Algorithm.md> "Substitute Algorithm"
[Extract Superclass]: <../Recipes/Extract Superclass.md> "Extract Superclass"

[Extract Class]: <../Recipes/Extract Class.md> "Extract Class"
[Consolidate Conditional Expression]: <../Recipes/Consolidate Conditional Expression.md> "Consolidate Conditional Expression"

[Consolidate Duplicate Conditional Fragments]: <../Recipes/Consolidate Duplicate Conditional Fragments.md> "Consolidate Duplicate Conditional Fragments"
