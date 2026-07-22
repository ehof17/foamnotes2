[[Dispensables]]
# Data Class
A data class refers to a class that contains only fields and crude methods for accessing them (getters and setters). These are simply containers for data used by other classes. These classes don't contain any additional functionality and can't independently operate on the data that they own.

### Reasons for the Problem
It's a normal thing when a newly created class contains only a few public fields (and maybe even a handful of getters/setters). But the true power of objects is that they can contain behavior types or operations on their data.

#### Recipe 1
##### Encapsualte Field
If a class contains public fields, use [[Encapsulate Field]] to hide them from direct access and require that access be performed via getters and setters only.

#### Recipe 2
##### Encapsualte Collection
Use [[Encaspulate Collection]] for data stored in collections like arrays

#### Recipe 3
##### Move Client Code Closer to the Data
- Review the client code that uses the class, in it you may find functionality that would be better located in the data class itself. If this is the case, [[Move Method]] and [[Extract Method]] to migrate the functionality to the data class

#### Recipe 4
##### Get rid of old data access methods
- After the class has been filled with well thought-out methods, you may want to get rid of old methods for data access that give overly broad access to the class data. For this, [[Remove Setting Method]] and [[Hide Method]] may be helpful.

#### Payoff
- Improves understanding and organization of code. Operations on particular data are now gathered in a single place, instead of haphazardly throughout the code.
- Helps you to spot duplication of client code.

[Dispensables]: Dispensables.md "Dispensables"
[Encapsulate Field]: <../Recipes/Encapsulate Field.md> "Encapsulate Field"
[Encaspulate Collection]: <../Recipes/Encaspulate Collection.md> "Encaspulate Collection"

[Move Method]: <../Recipes/Move Method.md> "Move Method"
[Extract Method]: <../Recipes/Extract Method.md> "Extract Method"

[Remove Setting Method]: <../Recipes/Remove Setting Method.md> "Remove Setting Method"
[Hide Method]: <../Recipes/Hide Method.md> "Hide Method"
