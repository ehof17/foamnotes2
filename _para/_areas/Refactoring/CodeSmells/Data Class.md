[[Dispensables]]
# Data Class
A data class refers to a class that contains only fields and crude methods for accessing them (getters and setters). These are simply containers for data used by other classes. These classes don't contain any additional functionality and can't independently operate on the data that they own.

### Reasons for the Problem
It's a normal thing when a newly created class contains only a few public fields (and maybe even a handful of getters/setters). But the true power of objects is that they can contain behavior types or operations on their data.

#### Recipe 1
##### Encapsualte Field
If a class contains public fields, use [[Encapsulate Field]] to hide them from direct access and require that access be performed via getters and setters only.

[Dispensables]: Dispensables.md "Dispensables"
