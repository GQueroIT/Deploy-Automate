# Modules

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### What a module is
A module is a separate Bicep (or ARM JSON) file that another Bicep file deploys. It's how you break a large deployment into organized, reusable pieces instead of one giant file with everything in it.

```bicep
module storageModule 'storage.bicep' = {
  name: 'storageDeployment'
  params: {
    storageAccountName: 'stg${uniqueString(resourceGroup().id)}'
    location: resourceGroup().location
  }
}
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.


### The name property isn't the resource name
Inside a module block, name: is the name of the nested deployment operation itself, it's what shows up in your deployment history in the Azure portal. It has nothing to do with the actual names of resources created inside that module, those are controlled by whatever parameters the module itself defines and uses.

### Modules define their own interface
A module file (like storage.bicep above) has its own param() block at the top defining exactly what it accepts, the calling file has to supply values for those through the params: {} block, it can't just reach in and reference the module's internal variables directly.

### Modules can loop and be conditional too
Everything from module 6, if expressions and for loops, works exactly the same way on a module block as it does on a plain resource block.

### Sharing modules
For sharing modules across a team or multiple projects, you can publish them to a private Bicep module registry or use template specs. Bicep also has limited support for embedding non-Bicep artifacts like PowerShell scripts using loadTextContent() and loadFileAsBase64().

## Commands Used in This Lesson

- `resourceGroup()` — Bicep function, returns info about the current resource group, .location and .name. Example: `resourceGroup().location`

## Key Terms
See GLOSSARY.md. New here: Nested deployment (a deployment operation triggered from within another deployment, which is what a module call actually is under the hood).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/modules
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/file
