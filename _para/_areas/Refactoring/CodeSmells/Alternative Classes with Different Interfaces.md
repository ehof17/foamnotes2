[[Object Orientation Abusers]]
# Alternative Classes with different interfaces
- 2 classes perform identical functions but have different method names

### Reasons for the problem
- Lack of communication. One programmer didn't know another already made the functionality

#### Recipe 1
[[Rename Method]] to make them identical in all alternative classes

#### Recipe 2
Make Methods' Signatures and Implementation identical
[[Move Method]], [[Add Parameter]], and [[Paramaterize Method]] to make signature and implementation of methods the same


#### Recipe 3
Extract Only Identical Parts
If only part of the functionality is duplicated, try [[Extract Superclass]]. In this case, existing classes become subclasses

#### Recipe 4
Delete clones
- Remove one of the classes

#### Payoff
- You get rid of unnecessary duplicated code, making the resulting code less bulky.
- Code becomes more readable and understandable (you no longer have to guess the reason for creation of a second class performing the exact same functions as the first one).

#### When to ignore
Sometimes merging classes is impossible or so difficult as to be pointless.
One example is when the alternative classes are in different libraries that each have their own version of the class.


[Object Orientation Abusers]: <../CodeSmells/Object Orientation Abusers.md> "Object Orientation Abusers"
[Rename Method]: <../Recipes/Rename Method.md> "Rename Method"

[Move Method]: <../Recipes/Move Method.md> "Move Method"
[Add Parameter]: <../Recipes/Add Parameter.md> "Add Parameter"
[Paramaterize Method]: <../Recipes/Paramaterize Method.md> "Paramaterize Method"
[Extract Superclass]: <../Recipes/Extract Superclass.md> "Extract Superclass"
