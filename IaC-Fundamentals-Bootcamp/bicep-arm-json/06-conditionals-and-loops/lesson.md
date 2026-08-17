# Conditionals and Loops

## Status
In progress

## Lesson

### Conditional deployment with if
Add an if expression directly on a resource or module declaration to deploy it only when a condition is true:

```bicep
param deployNsg bool

resource nsg 'Microsoft.Network/networkSecurityGroups@2023-09-01' = if (deployNsg) {
  name: 'nsg-web'
  location: resourceGroup().location
}
```

If deployNsg is false, this resource simply isn't deployed at all, nothing gets created and nothing errors.

### Loops with for
Use for inside square brackets to deploy multiple copies of a resource from a single block, iterating over an array:

```bicep
param nsgNames array = ['nsg-web', 'nsg-app', 'nsg-data']

resource nsgs 'Microsoft.Network/networkSecurityGroups@2023-09-01' = [for name in nsgNames: {
  name: name
  location: resourceGroup().location
}]
```

This functionality has been supported since Bicep v0.3.1 onward. Each loop instance is deployed in parallel by default, in no guaranteed order, unless you control it with @batchSize().

### Looping over key-value pairs
If your array is actually an object (dictionary-style) rather than a plain list, use items() to loop over its key-value pairs instead:

```bicep
param nsgValues object = {
  nsg1: { name: 'nsg-westus1', location: 'westus' }
  nsg2: { name: 'nsg-east1', location: 'eastus' }
}

resource nsg 'Microsoft.Network/networkSecurityGroups@2023-09-01' = [for nsg in items(nsgValues): {
  name: nsg.value.name
  location: nsg.value.location
}]
```

### Combining if and for
You can add a condition inside a loop to conditionally deploy only some of the collection.

### Controlling loop order with @batchSize
By default, looped resources deploy concurrently in a non-deterministic order. @batchSize(n) forces them to deploy in sequential batches of n at a time, useful when you're updating a production environment and don't want every instance changing simultaneously.

## Key Terms
See GLOSSARY.md. New here: Conditional deployment (a resource that only gets created if a condition is true), Iteration/Loop (deploying multiple similar resources from one block), Batch (a controlled group of loop instances deployed together).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/loops
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/file
