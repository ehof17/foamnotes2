[[Object Orientation Abusers]]
# Temporary field
- fields that take on values only under certain circumstances. Outside of these circumstances, they are empty.
- Tough to understand. You want to see data in the field but often don't

### Reasons for the problem
- Often, an alg requires a lot of inputs. Instead of introducing a lot of params into the method, programmer decides to create fields for the data in the class. The fields are only used in the algorithm and are unused the rest of the time


#### Recipe 1
##### Extract Temporary Fields and related behaviors.
Temporary fields and all code operating on them can be put in a separate class via [[Extract Class]]. In other words, create a method object, getting the same result as you would if you performed [[Replace Method With Method Object]]

#### Recipe 2
##### Introduce Null Object
[[Introduce Null Object]] and integrate it when the conditional code was used to check the temporary field values for existence



[Object Orientation Abusers]: <Object Orientation Abusers.md> "Object Orientation Abusers"
[Extract Class]: <../Recipes/Extract Class.md> "Extract Class"
[Replace Method With Method Object]: <../Recipes/Replace Method With Method Object.md> "Replace Method With Method Object"

[Introduce Null Object]: <../Recipes/Introduce Null Object.md> "Introduce Null Object"
