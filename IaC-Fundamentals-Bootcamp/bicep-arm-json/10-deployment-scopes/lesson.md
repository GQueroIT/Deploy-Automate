# Deployment Scopes

## Status
In progress

## Lesson

### The four scopes
targetScope = 'resourceGroup' | 'subscription' | 'managementGroup' | 'tenant', declared at the very top of a Bicep file. If you omit it entirely, resourceGroup is the default, which is why everything you've built so far in this repo has worked without ever setting it.

- resourceGroup (default) — deploy resources into an existing resource group. This is what nearly all of your work so far has been.
- subscription — lets you create resource groups themselves, assign subscription-level policies, and deploy resources that live above the resource group level.
- managementGroup / tenant — organization-wide governance and policy assignment across multiple subscriptions. You likely won't touch these day to day, but it's worth knowing they exist and why: some things (like certain policy assignments) genuinely can't be scoped any lower.

```bicep
targetScope = 'subscription'

resource rg 'Microsoft.Resources/resourceGroups@2025-04-01' = {
  name: 'rg-example'
  location: 'eastus'
}
```

### Modules can target a different scope than their parent file
A subscription-scoped file can deploy a module into a specific resource group using the scope: property:

```bicep
targetScope = 'subscription'
param resourceGroupName string

module exampleModule 'module.bicep' = {
  name: 'exampleModule'
  scope: resourceGroup(resourceGroupName)
  params: {}
}
```

This is how you create a resource group and immediately deploy resources into it in a single deployment, the resource group creation happens at subscription scope, then the module call drops down to resource group scope for everything inside it.

### Deployment commands differ per scope
A resource-group-scoped file deploys with az deployment group create. A subscription-scoped file uses az deployment sub create instead, and needs a --location flag since there's no resource group to imply one.

## Key Terms
See GLOSSARY.md. New here: Scope hierarchy (tenant contains management groups, which contain subscriptions, which contain resource groups, which contain resources, each level down is a narrower scope).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-to-subscription
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-to-resource-group
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-to-management-group
