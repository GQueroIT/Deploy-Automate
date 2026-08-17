# Conditionals and Loops

By the end of this module, you'll be able to conditionally deploy a resource and deploy multiple copies of one from a single block.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### Conditional deployment with if
Add an if expression directly on a resource or module declaration to deploy it only when a condition is true:

```bicep
param deployNsg bool

resource nsg 'Microsoft.Network/networkSecurityGroups@2023-09-01' = if (deployNsg) {
  name: 'nsg-web'
  location: resourceGroup().location
}
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.


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

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.


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

> **Try it now, Checkpoint 3**
> Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.


### Combining if and for
You can add a condition inside a loop to conditionally deploy only some of the collection.

### Controlling loop order with @batchSize
By default, looped resources deploy concurrently in a non-deterministic order. @batchSize(n) forces them to deploy in sequential batches of n at a time, useful when you're updating a production environment and don't want every instance changing simultaneously.

## Commands Used in This Lesson

- `resourceGroup()` — Bicep function, returns info about the current resource group, .location and .name. Example: `resourceGroup().location`
- `items()` — Bicep function, loops over the key-value pairs of an object instead of a plain array. Example: `items(myObject)`

## Troubleshooting

- Your for loop deploys, but every instance has the same name and only one resource actually exists afterward. You referenced the original array parameter instead of the loop variable inside the block body.
- Combining if and for throws a syntax error. The if goes directly after the equals sign, the for goes inside the square brackets that follow it, mixing up the order breaks it.

## Key Terms
See GLOSSARY.md. New here: Conditional deployment (a resource that only gets created if a condition is true), Iteration/Loop (deploying multiple similar resources from one block), Batch (a controlled group of loop instances deployed together).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/loops
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/file

## See Also

- [Terraform module 08, count and for_each](../../terraform/08-count-and-for-each/lesson.md)
