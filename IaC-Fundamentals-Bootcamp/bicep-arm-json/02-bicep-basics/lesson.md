# Bicep Basics: JSON to Bicep

By the end of this module, you'll be able to write the same resource in Bicep instead of raw JSON, and compile it to confirm it produces the same thing underneath.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### Bicep is a shorthand for what you just wrote by hand
Everything in module 1's ARM JSON has a Bicep equivalent, just with less boilerplate and cleaner syntax. Bicep files use keywords instead of nested JSON objects: param, var, resource, output.

```bicep
param storageAccountName string
param location string = resourceGroup().location

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

output storageAccountId string = storageAccount.id
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.


Notice there's no $schema, no contentVersion, none of the JSON boilerplate from module 1. Bicep generates all of that automatically when it compiles.

### The resource declaration
resource <symbolic-name> '<type>@<apiVersion>' = { ... }. The symbolic name (storageAccount above) is just how you refer to this resource elsewhere inside your own Bicep file, it is not the actual Azure resource name, that's the name: property inside the block.

### Compiling Bicep to ARM JSON
Every Bicep file transpiles (compiles) into ARM JSON before it's actually deployed, that conversion happens automatically, but you can also trigger it yourself to see the output:

```bash
az bicep build --file solution.bicep
```

> **Try it now, Checkpoint 2**
> Run the command above yourself in your terminal before reading on, don't just read what it's supposed to do.


This produces a .json file. Comparing that output against the ARM JSON you hand-wrote in module 1 is exactly how you confirm Bicep isn't magic, it's just generating the same thing you already know how to read.

## Commands Used in This Lesson

- `az bicep build` — Compiles a .bicep file into the ARM JSON that actually gets deployed. Example: `az bicep build --file main.bicep`
- `resourceGroup()` — Bicep function, returns info about the current resource group, .location and .name. Example: `resourceGroup().location`

## Troubleshooting

- az bicep build fails with a parser error pointing at a line that looks fine. Check the line just above it, Bicep often reports the error one token after where the actual mistake is, like a missing comma or brace.
- The compiled JSON doesn't look anything like your hand-written module 1 template. Normal for structure and metadata, what should match is the substance, the parameters, resources, and outputs sections.

## Key Terms
See GLOSSARY.md. New here: Symbolic name (an internal reference name for a resource inside a Bicep file, not its actual Azure name), Transpile/Compile (converting Bicep source into the ARM JSON that actually gets deployed).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/file
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/learn-bicep
