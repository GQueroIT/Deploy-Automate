# Deployment Scopes

By the end of this module, you'll be able to write a subscription-scoped deployment that creates a resource group and deploys into it in one shot.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

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

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.


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

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.


This is how you create a resource group and immediately deploy resources into it in a single deployment, the resource group creation happens at subscription scope, then the module call drops down to resource group scope for everything inside it.

### Deployment commands differ per scope
A resource-group-scoped file deploys with az deployment group create. A subscription-scoped file uses az deployment sub create instead, and needs a --location flag since there's no resource group to imply one.

## Commands Used in This Lesson

- `az deployment group create` — Deploys a Bicep or ARM template into a specific resource group. Example: `az deployment group create --resource-group rg-name --template-file main.bicep`
- `az deployment sub create` — Deploys a subscription-scoped Bicep or ARM template. Example: `az deployment sub create --location eastus --template-file main.bicep`

## Troubleshooting

- az deployment sub create fails with a message about a missing --location. Subscription-scoped deployments need it explicitly, there's no resource group yet to imply a region.
- The module deploys before the resource group exists. Confirm the module's scope: property points at the resource group's symbolic name you declared in the same file.

## Key Terms
See GLOSSARY.md. New here: Scope hierarchy (tenant contains management groups, which contain subscriptions, which contain resource groups, which contain resources, each level down is a narrower scope).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-to-subscription
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-to-resource-group
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-to-management-group
