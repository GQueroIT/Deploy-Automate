# Problem: Array Loops for Multiple Resources

## Scenario
Your team needs three network security groups, one each for web, app, and data tiers, and you don't want three nearly-identical resource blocks sitting in your file.

## Your task
In solution.bicep:

1. Declare an array parameter nsgNames defaulting to ['nsg-web', 'nsg-app', 'nsg-data'].
2. Write a single resource block using a for loop that creates one network security group per name in that array.
3. Each NSG's name property must come from the loop item, not be hardcoded.
4. Add an output that returns an array of all three deployed NSG names, confirming the loop actually produced three distinct resources (a variable or output loop, looping over the same array again, will do this).

## Hints
- Hint 1: This is the exact pattern from module 6's conditionals-and-loops lesson, minus the if, reuse that shape directly.
- Hint 2: Referencing the loop item directly inside the block body (name: name if your loop variable is called name) is what makes each instance unique, don't accidentally reference the original nsgNames parameter instead of the loop variable.
- Hint 3: An output loop uses the same [for item in collection: expression] syntax, just on an output instead of a resource.
