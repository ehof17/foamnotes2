[[Change Preventers]]
Whenever creating a subclass for a class, you find yourself nreeding to create a subclass for another class
# Reasons for the problem
- More classes being added makes changes harder and harder

#### Recipe 1
##### Merge Class Hierarchies (If possible)
- May be able to deduplicate class hierarchies in two steps.
- 1. Make instances of one hierarchy refer to instances of another hierarchy
- 2. Remove the hierarchy in the referred class, by using [[Move Method]] or [[Move field]]

#### When to ignore
- Sometimes parallel class hierarchies are just a way to avoid a bigger mess with program architecture.
- If you find that yor attempts to de duplicate make it worse/uglier, just revert everything and get used to it buddy

[Change Preventers]: <Change Preventers.md> "Change Preventers"
[Move Method]: <../Recipes/Move Method.md> "Move Method"
[Move field]: <../Recipes/Move Field.md> "Move Field"
