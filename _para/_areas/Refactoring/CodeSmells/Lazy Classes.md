[[Dispensables]]
# Lazy classes
Understanding and maintaining classes always costs time and money. So if a class doesn't do enough to earn your attention, it should be deleted.
### Reasons for the Problem
- After refactoring, a class became very small 
- Designed to support future development that was never done

### Recipe 1
#### Inline Class
Components that are near-useless should be given the [[Inline Class]] treatment.

### Recipe 2
#### Collapse Hierarchy
For subclasses with few functions, [[Collapse Hierarchy]]

### When to ignore
Sometimes a Lazy Class is created in order to delineate intentions for future development, In this case, try to maintain a balance between clarity and simplicity in your code.

[Dispensables]: Dispensables.md "Dispensables"
[Inline Class]: <../Recipes/Inline Class.md> "Inline Class"

[Collapse Hierarchy]: <../Recipes/Collapse Hierarchy.md> "Collapse Hierarchy"
