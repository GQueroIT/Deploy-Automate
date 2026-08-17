# ARM JSON Anatomy

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### What an ARM template actually is
An ARM template is a JSON file that tells Azure Resource Manager what you want to exist. It's declarative: you describe the end state, not the sequence of clicks or commands it takes to get there. Azure Resource Manager reads the file and figures out the deployment order and dependencies on its own. Bicep, which you'll get into in module 2, is a friendlier language that compiles down into this exact same ARM JSON. Every Bicep file becomes one of these underneath, so understanding this shape first is what makes Bicep make sense later instead of feeling like magic.

### The core sections
A minimal ARM template has these top-level elements:

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": { },
  "variables": { },
  "resources": [ ],
  "outputs": { }
}
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.json) yourself rather than copy-pasting it. Read back through it and confirm you can name what each part is doing before moving on.


- $schema — a URL pointing to the schema version Azure uses to validate the structure of your file. You don't write this from memory, you copy the current one from Microsoft's docs.
- contentVersion — your own version label for the template file itself. It doesn't change what gets deployed, it's just metadata you control.
- parameters — values supplied at deploy time. Each parameter has a type (string, int, bool, object, secureString, secureObject, or array). If a parameter has a defaultValue, it's optional at deploy time. If it doesn't, whoever deploys the template has to supply it.
- variables — values computed or reused inside the template. Unlike parameters, nobody enters these at deploy time. They exist purely so you're not repeating the same expression five times in the file.
- resources — the array of actual Azure resources to create. This is the only section that's truly required beyond $schema and contentVersion. Each resource needs, at minimum, a type (like Microsoft.Storage/storageAccounts), an apiVersion, a name, and usually a location.
- outputs — values returned after the deployment finishes, like a resource ID or a generated endpoint name, that another script or template could consume.

### Why the resource type looks the way it does
A resource type string like Microsoft.Storage/storageAccounts has two parts: the resource provider namespace (Microsoft.Storage) and the resource type within that provider (storageAccounts). The apiVersion is a dated string, like 2023-01-01, that pins which version of that resource's schema you're targeting. Different api-versions can have different required properties, so this isn't a formality, it changes what fields are valid.

### Pointing an output back at a resource
You'll need this for the problem below. The full lesson on ARM template functions is module 5, but the output requirement in this module's problem needs one small piece of it now. The resourceId() function builds the full resource ID string for a resource you've declared, by referencing its type and name:

```json
"outputs": {
  "storageAccountId": {
    "type": "string",
    "value": "[resourceId('Microsoft.Storage/storageAccounts', parameters('storageAccountName'))]"
  }
}
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.json) yourself rather than copy-pasting it. Read back through it and confirm you can name what each part is doing before moving on.


Anything inside square brackets in ARM JSON is a function call being evaluated, not a literal string. resourceId() is the most common one you'll reach for in an output, it doesn't require the resource to have already deployed, ARM can compute a resource ID from its type and name alone.

## Commands Used in This Lesson

- `resourceId()` — ARM template function, builds the full resource ID for a resource from its type and name. Example: `resourceId('Microsoft.Storage/storageAccounts', parameters('name'))`

## Key Terms
See GLOSSARY.md at the repo root. This module leans on: JSON, ARM template, Resource provider, API version, Schema, Declarative.

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/data-types
