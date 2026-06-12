[[Bloater]]
# Large Class

### Why? 
> Classes start small, but get bloated over time

##### Recipe 1
[[Extract Class]]

##### Recipe 2
[[Extract Subclass]]
> Helps if behavior of the large class can be implemented in different ways, or used in rare cases

##### Recipe 3
[[Extract Interface]]
> Helps if its necessary to have a list of operations and behaviors that the client can use

##### Recipe 4
- Separate Gui and domain data 
> It a large class is responsible for GUI, maybe move some of its data and behavior into a separate domain Object
[[Duplicate Observed Data]] lets us do this




[Extract Class]: <../Recipes/Extract Class.md> "Extract Class"
[Extract Subclass]: <../Recipes/Extract Subclass.md> "Extract Subclass"

[Extract Interface]: <../Recipes/Extract Interface.md> "Extract Interface"
[Duplicate Observed Data]: <../Recipes/Duplicate Observed Data.md> "Duplicate Observed Data"

[Bloater]: Bloater.md "Bloater"
