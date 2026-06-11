# Long Parameter list
- More than 3 or for per method

#### Reasons for the problem
- If several algs are merged into a single method
- Byproduct of making classes more independent. For example if code was moved from one class to another, the new class needs additional info passed in. So dependency has decreased. If several of these are created, all of them will require their own parameters, making a big list
- Instead of a long list of params, method can use data of its own object. If current object doesn't contain necessary data, a new object can be passed as parameters


#### Recipe 1
[[Replace Parameter with Method Call]]
- Check what values are passed to parameters. If some args aare just results of method calls to another object, use this recipe. The object can be placed in the field of its own class or passed as a method parameters

#### Recipe 2
[[Preserve Whole Object]]
- Instead of passing group of data from another object as parameters, pass the object itself


#### Recipe 3
[[Introduce Parameter Object]]
- But if all these parameters are coming from different sources, you can pass them as single parameter object 
- 


[Replace Parameter with Method Call]: <../Recipes/Replace Parameter with Method Call.md> "Replace Parameter with Method Call"
[Preserve Whole Object]: <../Recipes/Preserve Whole Object.md> "Preserve Whole Object.mb"

[Introduce Parameter Object]: <../Recipes/Introduce Parameter Object.md> "Introduce Parameter Object"
