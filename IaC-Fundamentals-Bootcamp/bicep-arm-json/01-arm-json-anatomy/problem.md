# Problem: ARM JSON Anatomy

## Scenario
A new project team needs a storage account provisioned for file drops. Before you touch Bicep at all, you're hand-writing the raw ARM JSON so you actually understand what's happening underneath it once Bicep starts hiding this from you.

## Your task
Write an ARM template by hand in solution.json that:

1. Declares one parameter for the storage account name, type string, with no default value (it should be required at deploy time).
2. Declares a second parameter for the Azure region, type string, with a default value so it's optional.
3. Declares exactly one resource: a storage account (Microsoft.Storage/storageAccounts), using both parameters for its name and location.
4. Adds an output that returns the storage account's resource ID after deployment.

You are not deploying this yet, that comes once you've got Bicep and the Azure CLI workflow down in a later module. The goal here is getting the raw shape of a template into your fingers before Bicep abstracts it away.

## Hints
- Hint 1: Look up the current apiVersion and required properties for Microsoft.Storage/storageAccounts in Microsoft's ARM template reference rather than guessing. Storage accounts also require a sku and a kind, those aren't optional.
- Hint 2: A parameter with a defaultValue is optional at deploy time. One without a defaultValue is required, whoever runs the deployment has to supply it.
- Hint 3: Outputs typically use the resourceId() function or a reference() expression to point back at a resource you already declared in the resources array.
