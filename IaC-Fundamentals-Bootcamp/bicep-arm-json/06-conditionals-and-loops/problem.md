# Problem: Conditionals and Loops

## Scenario
Your team wants network security groups deployed for a list of subnets, but only in environments where a "deploy NSGs" flag is turned on, some lightweight dev environments skip them entirely to save time.

## Your task
In solution.bicep:

1. Declare a boolean parameter deployNsgs.
2. Declare an array parameter nsgNames with at least 3 names in it, like ['nsg-web', 'nsg-app', 'nsg-data'].
3. Write a single resource block that deploys a network security group for each name in the array, using a for loop, and only deploys any of them at all if deployNsgs is true, combining if and for on the same resource.
4. Compile the file twice: once mentally with deployNsgs set to true (all three should appear), and once with it set to false (none should appear).

## Hints
- Hint 1: The if goes directly after the = sign, and the for goes inside the square brackets that follow it, both on the same resource declaration.
- Hint 2: Each looped NSG needs a unique name, that's what the loop variable (the item from nsgNames) is for, don't hardcode a single name inside the loop body or every instance will collide.
- Hint 3: If you're unsure whether your if and for are combined correctly, look at how Microsoft's own docs show the combined syntax, the loop syntax wraps the whole object, and the if sits just before the opening curly brace of that object.

## Expected Result
With deployNsgs set to true, compiling should show three separate NSG resources in the output, each with a distinct name matching an entry in your array. With it false, zero NSGs should appear.

## Cost & Cleanup
NSGs themselves are free, but clean up the resource group when you're done experimenting: az group delete --name <your-rg> --yes --no-wait.
