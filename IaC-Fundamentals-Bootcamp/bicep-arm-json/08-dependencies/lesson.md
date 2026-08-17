# Dependencies: Implicit vs Explicit

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### Implicit dependency
Created automatically when one resource declaration references another resource's property in the same file. Bicep sees the reference and figures out the correct deploy order on its own, no extra syntax needed.

```bicep
resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: 'examplestorage'
  location: resourceGroup().location
  kind: 'StorageV2'
  sku: { name: 'Standard_LRS' }
}

resource fileService 'Microsoft.Storage/storageAccounts/fileServices@2023-05-01' = {
  name: 'default'
  parent: storage
}
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.


fileService is implicitly dependent on storage here because it references storage through the parent property. A nested/child resource also automatically depends on whatever resource contains it.

### Explicit dependency
Declared with the dependsOn property, which accepts an array of resource references, for cases where a real dependency exists but nothing in the code actually references the other resource's properties, so Bicep has no way to infer it on its own.

```bicep
resource dashboard 'Microsoft.Portal/dashboards@2020-09-01-preview' = {
  name: 'monitoring-dashboard'
  dependsOn: [
    appInsights
  ]
}
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.


### Prefer implicit, and here's why
Microsoft's own best-practices guidance is explicit: prefer implicit dependencies over explicit ones wherever it's usually possible to reference the other resource's properties instead. The reasoning: dependsOn doesn't document why resources are related (after deployment, there's no way to inspect it), and unnecessary explicit dependencies slow deployment down because Resource Manager can no longer deploy unrelated resources in parallel. If you catch yourself reaching for dependsOn, it's worth asking whether there's a property reference that would create the same dependency implicitly instead.

## Key Terms
See GLOSSARY.md. New here: Dependency graph (the full map of which resources must deploy before which others, built automatically from implicit and explicit dependencies together).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/resource-dependencies
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/best-practices
