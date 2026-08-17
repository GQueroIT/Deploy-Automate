# Array Loops for Multiple Resources

## Status
In progress

## Lesson

### The pattern, reinforced
Module 6 introduced for loops alongside conditionals. This module isolates that same syntax specifically for the most common real-world use case: deploying N nearly-identical resources from a single block instead of copy-pasting a resource declaration N times.

```bicep
param nsgNames array = ['nsg-web', 'nsg-app', 'nsg-data']

resource nsgs 'Microsoft.Network/networkSecurityGroups@2023-09-01' = [for name in nsgNames: {
  name: name
  location: resourceGroup().location
}]
```

### Index-based loops with range()
When you just need N copies and don't have specific named items, range(start, count) generates an array of sequential integers you can loop over instead:

```bicep
resource storageAccounts 'Microsoft.Storage/storageAccounts@2023-01-01' = [for i in range(0, 3): {
  name: 'stg${i}${uniqueString(resourceGroup().id)}'
  location: resourceGroup().location
  kind: 'StorageV2'
  sku: { name: 'Standard_LRS' }
}]
```

### Every instance needs a unique name
This is the single most common mistake with loops: forgetting that name: has to be different for every instance, usually built from the loop item or index. If every instance in a loop ends up with the same computed name, Bicep will fail or silently only create one.

## Key Terms
See GLOSSARY.md. Nothing new this module, this is reinforcement of Loop and Iteration from module 6, specifically applied to the resource-scaling use case.

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/loops
