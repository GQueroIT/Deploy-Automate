# Expressions and Built-In Functions

## Status
In progress

## Lesson

### String interpolation
Drop a variable's value directly inside a string using ${}:

```bicep
var storageName = '${resourcePrefix}${uniqueString(resourceGroup().id)}'
```

### resourceGroup() and subscription()
These return objects describing the current deployment context. resourceGroup().location, resourceGroup().name, subscription().subscriptionId are common ways to avoid hardcoding values that should come from wherever the template is actually being deployed.

### uniqueString()
Generates a deterministic hash string based on whatever you pass into it, same inputs always produce the same output, every time. This matters a lot for resource types like storage accounts that require a globally unique name across all of Azure, not just your subscription:

```bicep
var storageAccountName = 'stg${uniqueString(resourceGroup().id)}'
```

Using resourceGroup().id as the input means the generated name stays the same every time you redeploy into that same resource group (which matters for idempotency, redeploying shouldn't create a brand new randomly-named resource every time), while still being distinct from anyone else's resource group.

### Why hardcoded names break
A hardcoded storage account name like 'mystorageaccount' will fail to deploy the moment anyone else in the world has already taken that name, storage account names are globally unique across all of Azure, not scoped to your subscription. This is exactly the kind of failure uniqueString() is designed to prevent.

## Key Terms
See GLOSSARY.md. New here: Expression (a computed value evaluated at deployment time, built from functions, variables, and operators), Deterministic function (same input always produces the same output, as opposed to something random).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-scope
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-functions
