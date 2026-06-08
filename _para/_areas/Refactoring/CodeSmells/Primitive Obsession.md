# Primitive Obsession
Use of primitives instead of small objects for simple tasks

Use of constants for coding information
like USER_ADMIN_ROLE = 1 for referring to users with USER_ADMIN_ROLE

Use of string constants as field names for use in data arrays


#### Recipe 1
Replace Set of Fields with Object
[[Replace Data Value with Object ]]

#### Recipe 2
Primitive Fields in Method parameters.
If the values of primitive fields are used in method parameters, go with [[Introduce Parameter Object]] or [[Preserve Whole Object]]


#### Recipe 3
Get rid of type codes
When complicated data is coded in variables, use [[Replace Type Code With Class]], [[Replace Type Code with Subclasses]], or [[Replace Type Code With State-Strategy]]

If type code doesn't affect behavior, replace it with class.
If type affects program behavior, try to use subclasses.
If cannot use subclasses, state strat



[Replace Data Value with Object ]: <../Recipes/Replace Data Value with Object .md> "Replace Data Value with Object"
[Introduce Parameter Object]: <../Recipes/Introduce Parameter Object.md> "Introduce Parameter Object"
[Preserve Whole Object]: <../Recipes/Preserve Whole Object.md> "Preserve Whole Object.mb"

[Replace Type Code With Class]: <../Recipes/Replace Type Code With Class.md> "Replace Type Code With Class"
[Replace Type Code with Subclasses]: <../Recipes/Replace Type Code with Subclasses.md> "Replace Type Code with Subclasses"
[Replace Type Code With State-Strategy]: <../Recipes/Replace Type Code With State-Strategy.md> "Replace Type Code With State/Strategy"
