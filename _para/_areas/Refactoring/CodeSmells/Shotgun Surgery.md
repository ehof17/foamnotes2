[[Change Preventers]]
# Shotgun Surgery

Making any modifications requires a ton of small changes everywhere.
Like a friggin shotgun and its pellets
### Reasons for the problem
- A single responsibility has been split up among a large number of classes
- Lost in the sauce with [[Divergent Change]]

#### Recipe 1
##### Consolidate responsibility into single class
[[Move Field]] and [[Move Method]] to move behaviors around. Create a new class if needed.


#### Recipe 2
##### Remove Redundant Classes
If moving code to the same class makes some classes almost empty, use [[Inline Class]] to remove redundancy

#### Payoff
- Better organization
- Less code duplication
- Easier maintenance
[Change Preventers]: <Change Preventers.md> "Change Preventers"
[Divergent Change]: <Divergent Change.md> "Divergent Change"

[Move Method]: <../Recipes/Move Method.md> "Move Method"
[Move Field]: <../Recipes/Move Field.md> "Move Field"

[Inline Class]: <../Recipes/Inline Class.md> "Inline Class"
