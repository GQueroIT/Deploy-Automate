# Problem: Deployment Scopes

## Scenario
You want a single deployment that both creates a brand new resource group AND deploys a storage account into it, rather than two separate manual steps.

## Your task
In solution.bicep:

1. Set targetScope = 'subscription' as the first line of the file.
2. Declare a resource that creates a new resource group (Microsoft.Resources/resourceGroups), using a parameter for its name and location.
3. Add a module call (reuse your storage.bicep from module 7) that deploys into the resource group you just created, using the scope: property pointed at the resource group's symbolic name.
4. Note in a comment which CLI command this file would need to actually deploy (it's not az deployment group create, this one needs a different command).

## Hints
- Hint 1: targetScope has to be the very first statement in the file if you use it at all, before any param or resource declarations.
- Hint 2: Since the resource group is created in this same file, you can point the module's scope: directly at the resource group's symbolic name rather than using the resourceGroup() function with a string name.
- Hint 3: az deployment sub create needs a --location flag that az deployment group create doesn't, because at subscription scope there's no resource group yet to imply a region.
