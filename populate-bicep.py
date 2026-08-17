#!/usr/bin/env python3
"""
Populates every module in the bicep-arm-json/ section of IaC-Fundamentals-Bootcamp
with real lesson and problem content, sourced from Microsoft Learn.
Overwrites lesson.md and problem.md in each module folder. Safe to re-run.
"""

from pathlib import Path

REPO_NAME = "IaC-Fundamentals-Bootcamp"
SECTION = "bicep-arm-json"

MODULES = {}

MODULES["01-arm-json-anatomy"] = {
"lesson": """# ARM JSON Anatomy

## Status
In progress

## Lesson

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

Anything inside square brackets in ARM JSON is a function call being evaluated, not a literal string. resourceId() is the most common one you'll reach for in an output, it doesn't require the resource to have already deployed, ARM can compute a resource ID from its type and name alone.

## Key Terms
See GLOSSARY.md at the repo root. This module leans on: JSON, ARM template, Resource provider, API version, Schema, Declarative.

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/data-types
""",
"problem": """# Problem: ARM JSON Anatomy

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
"""
}

MODULES["02-bicep-basics"] = {
"lesson": """# Bicep Basics: JSON to Bicep

## Status
In progress

## Lesson

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

Notice there's no $schema, no contentVersion, none of the JSON boilerplate from module 1. Bicep generates all of that automatically when it compiles.

### The resource declaration
resource <symbolic-name> '<type>@<apiVersion>' = { ... }. The symbolic name (storageAccount above) is just how you refer to this resource elsewhere inside your own Bicep file, it is not the actual Azure resource name, that's the name: property inside the block.

### Compiling Bicep to ARM JSON
Every Bicep file transpiles (compiles) into ARM JSON before it's actually deployed, that conversion happens automatically, but you can also trigger it yourself to see the output:

```bash
az bicep build --file solution.bicep
```

This produces a .json file. Comparing that output against the ARM JSON you hand-wrote in module 1 is exactly how you confirm Bicep isn't magic, it's just generating the same thing you already know how to read.

## Key Terms
See GLOSSARY.md. New here: Symbolic name (an internal reference name for a resource inside a Bicep file, not its actual Azure name), Transpile/Compile (converting Bicep source into the ARM JSON that actually gets deployed).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/file
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/learn-bicep
""",
"problem": """# Problem: Bicep Basics: JSON to Bicep

## Scenario
You've got the raw ARM JSON storage account template from module 1. Now rewrite the same thing in Bicep, and prove to yourself that compiling it produces the same result.

## Your task
1. In solution.bicep, recreate the exact same storage account you hand-wrote in module 1's solution.json: a required storageAccountName parameter, a location parameter with a default, the storage account resource itself, and an output for the resource ID.
2. Run az bicep build --file solution.bicep to compile it to JSON.
3. Open the generated JSON and compare it section by section against your hand-written module 1 solution.json. They won't be identical (Bicep adds its own metadata and generates a languageVersion), but the parameters, resources, and outputs sections should match in substance.
4. Note at least two differences you noticed between what you wrote by hand and what Bicep generated for you automatically.

## Hints
- Hint 1: resourceGroup().location is a common default for a location parameter, it pulls the location from the resource group you're deploying into rather than forcing you to hardcode a region.
- Hint 2: The symbolic name you choose (storageAccount, stg, whatever) has zero effect on the deployed resource's actual name, don't confuse the two.
- Hint 3: If az bicep build errors, read the specific line number and property it's complaining about, Bicep's compiler errors are usually precise about what's missing or malformed.
"""
}

MODULES["03-parameters-and-variables"] = {
"lesson": """# Parameters and Variables

## Status
In progress

## Lesson

### Parameter syntax and decorators
@<decorator>(<argument>)
param <parameter-name> <parameter-data-type> = <default-value>

Decorators are optional annotations placed directly above a param or var line that add validation rules or documentation without changing the deployment logic itself.

- @description('...') documents the parameter, this text shows up as a tip when someone deploys through the Azure portal.
- @allowed([...]) restricts the parameter to a specific list of values, deployment fails immediately if someone passes something outside that list.
- @secure() marks a parameter as sensitive, Azure hides the value from logs, deployment history, and CLI output. Valid only on string or object type parameters (this lines up with secureString and secureObject in ARM JSON).

```bicep
@description('The environment to deploy to')
@allowed(['dev', 'test', 'prod'])
param environment string = 'dev'

@secure()
param adminPassword string
```

Bicep allows a maximum of 256 parameters per file, and parameter names can only contain letters, digits, and underscores (no periods, unlike ARM JSON).

### Variables
var <variable-name> = <variable-value>, type is usually inferred from the value rather than declared explicitly. Variables can also use decorators, and you're limited to 512 variables per file.

```bicep
var resourcePrefix = 'app'
var instanceCount = environment == 'prod' ? 5 : 2
```

That ternary (condition ? valueIfTrue : valueIfFalse) is a common pattern for computing a variable based on a parameter.

## Key Terms
See GLOSSARY.md. New here: Decorator, Sensitive value (data that shouldn't be exposed in logs or output, like a password).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameters
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/variables
""",
"problem": """# Problem: Parameters and Variables

## Scenario
You're standardizing how your team parameterizes deployments across dev, test, and prod, and you need to make sure nobody can accidentally typo an environment name or leak a password into deployment logs.

## Your task
In solution.bicep:

1. Declare an environment parameter (string), restricted with @allowed to only 'dev', 'test', or 'prod', with a @description explaining what it's for.
2. Declare an adminPassword parameter (string), marked @secure(), with no default value.
3. Declare a variable resourcePrefix that computes a different prefix string depending on the environment parameter (for example, 'dev-app', 'test-app', 'prod-app'), using a ternary or similar expression.
4. Add a resource of any type (reuse the storage account from module 2 if you want) that uses resourcePrefix as part of its name.

## Hints
- Hint 1: @allowed takes a literal array as its argument, written directly in the decorator, ['dev', 'test', 'prod'].
- Hint 2: @secure() only works on parameters typed string or object, if you try it on an int or bool parameter it won't be valid.
- Hint 3: For the ternary, environment == 'prod' ? 'prod-app' : 'nonprod-app' is the basic shape, you can nest more conditions if you want three distinct prefixes instead of two.
"""
}

MODULES["04-outputs"] = {
"lesson": """# Outputs

## Status
In progress

## Lesson

### Basic syntax
output <name> <type> = <value>

Outputs return a value after a deployment finishes, for another script, pipeline, or nested template to consume. Common examples: a resource's ID, a generated endpoint URL, a connection string.

```bicep
output storageAccountId string = storageAccount.id
output blobEndpoint string = storageAccount.properties.primaryEndpoints.blob
```

Referencing a resource's symbolic name with .id or drilling into its .properties gives you access to values Azure generates or assigns at deploy time, values you couldn't have known before deployment.

### Secure outputs
With recent Bicep versions, you can mark string or object outputs with @secure(), the same decorator you used on parameters in module 3. This prevents the value from being logged or displayed in deployment history, the Azure portal, or CLI output.

```bicep
@secure()
output generatedPassword string = someSecretValue
```

### Why this is a real gotcha
Outputs are visible in deployment history by default. If you output something sensitive without marking it @secure(), that value sits there in plain text in your deployment history for anyone with read access to see. This is an easy way to accidentally leak a secret even when you were careful about the parameter itself.

## Key Terms
See GLOSSARY.md. No new terms this module beyond what's already covered, this one is mostly application of concepts from module 3.

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/outputs
""",
"problem": """# Problem: Outputs

## Scenario
Another team needs to consume information about the storage account you're deploying, they need the resource ID and the blob endpoint URL, but nothing sensitive should ever show up in deployment history.

## Your task
Working from your module 2 or 3 storage account solution.bicep:

1. Add an output returning the storage account's resource ID.
2. Add an output returning the storage account's primary blob endpoint.
3. Add a third, fake output for a variable called adminPassword (just a placeholder string value is fine), first WITHOUT @secure(), and deploy or compile it to see how it looks in the output.
4. Now add @secure() to that same output and compile again, compare the difference in how it's represented.

## Hints
- Hint 1: A resource's resource ID is available via its symbolic name's .id property, no function call needed.
- Hint 2: The blob endpoint lives nested under .properties.primaryEndpoints.blob on a storage account resource, you'll need to drill into the property path correctly.
- Hint 3: @secure() on an output only works for string or object typed outputs, same restriction as parameters.
"""
}

MODULES["05-expressions-and-functions"] = {
"lesson": """# Expressions and Built-In Functions

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
""",
"problem": """# Problem: Expressions and Built-In Functions

## Scenario
Your module 2 storage account solution has a name that was either fully hardcoded or passed in as a required parameter every time, which means either it'll collide with someone else's globally, or you have to remember to type something unique every single deployment.

## Your task
Fix it in solution.bicep:

1. Remove any hardcoded storage account name.
2. Build the storage account name from a short prefix combined with uniqueString(resourceGroup().id), using string interpolation.
3. Replace any hardcoded region/location value with resourceGroup().location instead.
4. Compile the file and confirm the generated name is a valid storage account name (lowercase letters and numbers only, no dashes, no uppercase, under 24 characters total).

## Hints
- Hint 1: uniqueString() returns a fixed-length string of lowercase letters and numbers, that's exactly the character set storage account names require, which is part of why it's the standard tool for this.
- Hint 2: Storage account names cannot contain dashes or uppercase letters, if your prefix has either, the deployment will reject it even though the uniqueString() portion is fine.
- Hint 3: Because uniqueString(resourceGroup().id) is deterministic, redeploying this same file into the same resource group will always compute the exact same name, that's a feature, not a bug, it's what keeps redeployments idempotent instead of creating duplicates.
"""
}

MODULES["06-conditionals-and-loops"] = {
"lesson": """# Conditionals and Loops

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
""",
"problem": """# Problem: Conditionals and Loops

## Scenario
Your team wants network security groups deployed for a list of subnets, but only in environments where a "deploy NSGs" flag is turned on, some lightweight dev environments skip them entirely to save time.

## Your task
In solution.bicep:

1. Declare a boolean parameter deployNsgs.
2. Declare an array parameter nsgNames with at least 3 names in it, like ['nsg-web', 'nsg-app', 'nsg-data'].
3. Write a single resource block that deploys a network security group for each name in the array, using a for loop, and only deploys any of them at all if deployNsgs is true, combining if and for on the same resource.
4. Compile the file twice: once mentally with deployNsgs set to true (all three should appear), and once with it set to false (none should appear).

## Hints
- Hint 1: The if goes directly after the = sign, and the for goes inside the square brackets that follow it, both on the same resource declaration.
- Hint 2: Each looped NSG needs a unique name, that's what the loop variable (the item from nsgNames) is for, don't hardcode a single name inside the loop body or every instance will collide.
- Hint 3: If you're unsure whether your if and for are combined correctly, look at how Microsoft's own docs show the combined syntax, the loop syntax wraps the whole object, and the if sits just before the opening curly brace of that object.
"""
}

MODULES["07-modules"] = {
"lesson": """# Modules

## Status
In progress

## Lesson

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

### The name property isn't the resource name
Inside a module block, name: is the name of the nested deployment operation itself, it's what shows up in your deployment history in the Azure portal. It has nothing to do with the actual names of resources created inside that module, those are controlled by whatever parameters the module itself defines and uses.

### Modules define their own interface
A module file (like storage.bicep above) has its own param() block at the top defining exactly what it accepts, the calling file has to supply values for those through the params: {} block, it can't just reach in and reference the module's internal variables directly.

### Modules can loop and be conditional too
Everything from module 6, if expressions and for loops, works exactly the same way on a module block as it does on a plain resource block.

### Sharing modules
For sharing modules across a team or multiple projects, you can publish them to a private Bicep module registry or use template specs. Bicep also has limited support for embedding non-Bicep artifacts like PowerShell scripts using loadTextContent() and loadFileAsBase64().

## Key Terms
See GLOSSARY.md. New here: Nested deployment (a deployment operation triggered from within another deployment, which is what a module call actually is under the hood).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/modules
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/file
""",
"problem": """# Problem: Modules

## Scenario
Your main.bicep file is getting cluttered with every resource inline. You want the storage account logic pulled out into its own reusable file that any future project could call.

## Your task
1. Create a new file storage.bicep (inside this module's folder is fine for the exercise) containing just the storage account resource from earlier modules, with its own param() block for storageAccountName and location, and its own output for the resource ID.
2. In solution.bicep, write a module block that calls storage.bicep, passing in a computed name (using uniqueString() from module 5) and resourceGroup().location.
3. Reference the module's output (the storage account ID) in an output of your main solution.bicep file, to prove data can flow back out of a module.

## Hints
- Hint 1: The module's own params must be satisfied inside the params: {} block of the module call, you can't skip a required one without a default just because it "should" be obvious.
- Hint 2: To reference a module's output from the calling file, use moduleSymbolicName.outputs.outputName, not just the output name by itself.
- Hint 3: The path in module storageModule 'storage.bicep' = { is relative to the calling file's location, keep both files in the same folder for this exercise to keep the path simple.
"""
}

MODULES["08-dependencies"] = {
"lesson": """# Dependencies: Implicit vs Explicit

## Status
In progress

## Lesson

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

### Prefer implicit, and here's why
Microsoft's own best-practices guidance is explicit: prefer implicit dependencies over explicit ones wherever it's usually possible to reference the other resource's properties instead. The reasoning: dependsOn doesn't document why resources are related (after deployment, there's no way to inspect it), and unnecessary explicit dependencies slow deployment down because Resource Manager can no longer deploy unrelated resources in parallel. If you catch yourself reaching for dependsOn, it's worth asking whether there's a property reference that would create the same dependency implicitly instead.

## Key Terms
See GLOSSARY.md. New here: Dependency graph (the full map of which resources must deploy before which others, built automatically from implicit and explicit dependencies together).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/resource-dependencies
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/best-practices
""",
"problem": """# Problem: Dependencies: Implicit vs Explicit

## Scenario
You need a storage account and a file share inside it, and the file share obviously has to wait for the storage account to exist first. You want to prove you can express that relationship without ever touching dependsOn.

## Your task
In solution.bicep:

1. Declare a storage account resource.
2. Declare a file service resource as a child of that storage account (Microsoft.Storage/storageAccounts/fileServices), using the parent property to link it, not dependsOn.
3. Declare a file share resource as a child of the file service (Microsoft.Storage/storageAccounts/fileServices/shares), again using parent, not dependsOn.
4. Confirm your finished file contains zero dependsOn entries, and that the dependency chain is still fully correct through parent references alone.

## Hints
- Hint 1: The parent property takes the symbolic name of the containing resource, not a string, reference the actual resource you declared above it.
- Hint 2: Nesting three levels deep (storage account, then file service, then share) means each one's parent is the resource declared directly above it, not the original storage account every time.
- Hint 3: If you're tempted to add dependsOn "just to be safe," that's the exact instinct Microsoft's best-practices guidance is warning against, trust the parent reference, it's already creating the dependency.
"""
}

MODULES["09-array-loops-multiple-resources"] = {
"lesson": """# Array Loops for Multiple Resources

## Status
In progress

## Lesson

### The pattern, reinforced
Module 6 introduced for loops alongside conditionals. This module isolates that same syntax specifically for the most common real-world use case: deploying N nearly-identical resources from a single block instead of copy-pasting a resource declaration N times.

```bicep
param nsgNames array = ['nsg-web', 'nsg-app', 'nsg-data']

resource nsgs 'Microsoft.Network/networkSecurityGroups@2023-09-01' = [for name in nsgNames: {
  name: name
  location: resourceGroup().location
}]
```

### Index-based loops with range()
When you just need N copies and don't have specific named items, range(start, count) generates an array of sequential integers you can loop over instead:

```bicep
resource storageAccounts 'Microsoft.Storage/storageAccounts@2023-01-01' = [for i in range(0, 3): {
  name: 'stg${i}${uniqueString(resourceGroup().id)}'
  location: resourceGroup().location
  kind: 'StorageV2'
  sku: { name: 'Standard_LRS' }
}]
```

### Every instance needs a unique name
This is the single most common mistake with loops: forgetting that name: has to be different for every instance, usually built from the loop item or index. If every instance in a loop ends up with the same computed name, Bicep will fail or silently only create one.

## Key Terms
See GLOSSARY.md. Nothing new this module, this is reinforcement of Loop and Iteration from module 6, specifically applied to the resource-scaling use case.

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/loops
""",
"problem": """# Problem: Array Loops for Multiple Resources

## Scenario
Your team needs three network security groups, one each for web, app, and data tiers, and you don't want three nearly-identical resource blocks sitting in your file.

## Your task
In solution.bicep:

1. Declare an array parameter nsgNames defaulting to ['nsg-web', 'nsg-app', 'nsg-data'].
2. Write a single resource block using a for loop that creates one network security group per name in that array.
3. Each NSG's name property must come from the loop item, not be hardcoded.
4. Add an output that returns an array of all three deployed NSG names, confirming the loop actually produced three distinct resources (a variable or output loop, looping over the same array again, will do this).

## Hints
- Hint 1: This is the exact pattern from module 6's conditionals-and-loops lesson, minus the if, reuse that shape directly.
- Hint 2: Referencing the loop item directly inside the block body (name: name if your loop variable is called name) is what makes each instance unique, don't accidentally reference the original nsgNames parameter instead of the loop variable.
- Hint 3: An output loop uses the same [for item in collection: expression] syntax, just on an output instead of a resource.
"""
}

MODULES["10-deployment-scopes"] = {
"lesson": """# Deployment Scopes

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
""",
"problem": """# Problem: Deployment Scopes

## Scenario
You want a single deployment that both creates a brand new resource group AND deploys a storage account into it, rather than two separate manual steps.

## Your task
In solution.bicep:

1. Set targetScope = 'subscription' as the first line of the file.
2. Declare a resource that creates a new resource group (Microsoft.Resources/resourceGroups), using a parameter for its name and location.
3. Add a module call (reuse your storage.bicep from module 7) that deploys into the resource group you just created, using the scope: property pointed at the resource group's symbolic name.
4. Note in a comment which CLI command this file would need to actually deploy (it's not az deployment group create, this one needs a different command).

## Hints
- Hint 1: targetScope has to be the very first statement in the file if you use it at all, before any param or resource declarations.
- Hint 2: Since the resource group is created in this same file, you can point the module's scope: directly at the resource group's symbolic name rather than using the resourceGroup() function with a string name.
- Hint 3: az deployment sub create needs a --location flag that az deployment group create doesn't, because at subscription scope there's no resource group yet to imply a region.
"""
}

MODULES["11-what-if-and-validation"] = {
"lesson": """# What-If and Validation Workflow

## Status
In progress

## Lesson

### az deployment group validate
Checks that your template will deploy successfully without actually creating anything, a syntax-and-schema level check. Good as a fast first pass, but it doesn't tell you what would actually change in your environment.

```bash
az deployment group validate \\
  --resource-group myResourceGroup \\
  --template-file main.bicep \\
  --parameters @params.json
```

### az deployment group what-if
Goes further than validate: it shows you exactly what would happen, which resources would be created, modified, or deleted, and which specific properties would change, without applying anything. This is your actual safety net before running a deployment against an environment that already has real resources in it.

```bash
az deployment group what-if \\
  --resource-group myResourceGroup \\
  --template-file main.bicep
```

Reading what-if output: + means create, - means delete, ~ means modify in place. Anything you didn't expect to see change is exactly what you want to catch here, before you type yes on a real deployment.

### ValidationLevel
Recent versions of Azure CLI (2.76.0+) and Azure PowerShell (13.4.0+) introduced a ValidationLevel switch on deployment commands, giving you control over how thoroughly Resource Manager checks the template during validation, worth knowing exists if you hit validation behavior that seems more or less strict than expected.

## Key Terms
See GLOSSARY.md. New here: Dry run (a preview that shows what would happen without actually doing it, what-if is Bicep/ARM's version of this concept).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli
- https://learn.microsoft.com/en-us/cli/azure/bicep
""",
"problem": """# Problem: What-If and Validation Workflow

## Scenario
Before you run the subscription-level deployment from module 10 for real, you want to confirm it's only going to create things, and nothing you didn't expect.

## Your task
1. Using the solution.bicep from module 10, write out the exact az deployment sub what-if command you'd run to preview it (include the required --location flag).
2. In a comment or a short written note in solution.bicep, describe what you would expect the what-if output to show: how many resources, and whether they should all be marked as Create (+) and nothing else.
3. If you have Azure CLI and an Azure account available, actually run it and compare the real output against your prediction. If not, reason through it carefully based on what you know is in the template.

## Hints
- Hint 1: what-if needs the same --template-file and --location flags as the real deployment command would, just swap create for what-if in the command itself.
- Hint 2: Since this is a brand new resource group and a brand new storage account inside it, every resource in the what-if output should show a + (create), if you see a ~ or a - anywhere, something in the template isn't behaving the way you think it is.
- Hint 3: what-if output can be verbose, focus on the summary section first, which lists each resource and its action, before digging into the detailed property-level diff.
"""
}

MODULES["12-decompile-arm-to-bicep"] = {
"lesson": """# Decompiling ARM to Bicep

## Status
In progress

## Lesson

### The command
az bicep decompile <file.json> converts an existing ARM JSON template into Bicep. Useful when you inherit old ARM templates someone else wrote, or when you export a resource's current live configuration from the Azure portal and want to bring it into Bicep going forward.

```bash
az bicep decompile main.json
```

### Best-effort, not guaranteed
Microsoft is explicit about this: decompiling is a best-effort process, there's no guarantee of a perfect, direct mapping from ARM JSON back to Bicep. You'll typically need to review the output and manually fix warnings or errors it flags. This isn't a bug in the tool, ARM JSON is more flexible and less structured than Bicep, so some patterns don't translate cleanly.

### VS Code's paste-as-Bicep shortcut
Visual Studio Code has a feature that lets you paste raw ARM JSON directly into a .bicep file, and it automatically runs the decompile process for you behind the scenes, no separate CLI command needed for quick one-off conversions.

### Closing the loop on this whole section
Think about what you've actually done across this section of the repo: hand-wrote ARM JSON from scratch (module 1), wrote the equivalent in Bicep and compiled it back to JSON to compare (module 2), and now you're decompiling JSON back into Bicep. You've gone in both directions across the exact same conversion, which is the fastest way to actually understand that Bicep isn't a separate system, it's a syntax layer over the same ARM engine.

## Key Terms
See GLOSSARY.md. New here: Best-effort conversion (a tool does its best to translate automatically, but the output isn't guaranteed correct or complete without review).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile
""",
"problem": """# Problem: Decompiling ARM to Bicep

## Scenario
You want to close the loop on this entire section by converting your own hand-written ARM JSON back into Bicep, and comparing it against the Bicep you originally hand-wrote for the same resource.

## Your task
1. Take the solution.json you hand-wrote back in module 1.
2. Run az bicep decompile solution.json against it.
3. Open the resulting .bicep file and compare it, property by property, against the solution.bicep you hand-wrote in module 2 for what should be the same storage account.
4. List at least two differences between the decompiled version and your hand-written version, naming conventions, extra comments, structural choices, anything that stands out.
5. Clean up the decompiled file so it matches your own coding style from module 2, this is the manual review step Microsoft's docs explicitly call out as expected.

## Hints
- Hint 1: Expect the decompiler to generate its own symbolic names for resources, often less readable than what you'd choose by hand, that's normal, rename them to match your own convention.
- Hint 2: Watch for warning comments the decompiler inserts directly into the output, these flag spots it wasn't fully confident about, read every one of them rather than deleting them without looking.
- Hint 3: If az bicep decompile errors out entirely instead of producing warnings, it usually means something in the source JSON doesn't have a known Bicep equivalent yet, note what triggered it rather than assuming you did something wrong.
"""
}

# --- Full repo scaffold (creates the whole IaC-Fundamentals-Bootcamp skeleton) ---
# Included so this script can be run standalone, on an empty folder, and still
# produce a complete, valid repo. Only fills in files that don't already exist,
# so it never overwrites content another one of these scripts already populated.

GLOSSARY_CONTENT = """# General IaC Concepts

**Infrastructure as Code (IaC)** - writing your servers, networks, and cloud resources as text files instead of clicking through a portal, so the setup can be saved, reused, and tracked like any other code.

**Declarative** - you describe what the end result should look like, and the tool figures out how to get there. This is how Bicep, ARM, and Terraform work.

**Imperative** - you write out every step in order to make something happen. This is how a PowerShell script works.

**State** - a record of what infrastructure already exists right now, so the tool knows what to change instead of rebuilding everything from scratch every time.

**Idempotent** - running the same thing twice gives you the same result the second time as the first. No duplicate resources, no surprise side effects.

**Provider** - the plugin that lets a tool talk to a specific platform. Terraform's azurerm provider is how Terraform talks to Azure.

**Resource** - a single thing being created or managed: a VM, a storage account, a virtual network.

**Module** - a reusable, packaged chunk of code you call instead of rewriting the same block over and over.

**Deployment** - the actual act of running your code against the cloud and creating or changing real resources.

# PowerShell

**Cmdlet** - pronounced "command-let." A built-in PowerShell command, always named Verb-Noun, like Get-Process or New-Item.

**Pipeline** - the | symbol. Takes the output of one cmdlet and feeds it straight into the next one as input.

**Object** - everything that comes out of a cmdlet in PowerShell is a structured object with properties, not plain text. That's what makes Get-Member and Where-Object work.

**Parameter** - a named input you pass into a cmdlet or function, like -Name or -Path.

**Variable** - a named container holding a value, always starts with $, like $name.

**Script** - a saved .ps1 file containing a sequence of PowerShell commands.

**Function** - a named, reusable block of code inside a script that you call with parameters.

# JSON and ARM

**JSON (JavaScript Object Notation)** - a plain text format for storing structured data as key-value pairs. ARM templates are written in this format.

**ARM template** - a JSON file describing the Azure resources you want deployed. Azure Resource Manager reads it and builds them.

**Resource provider** - the Azure service responsible for a resource type, written like Microsoft.Compute or Microsoft.Storage.

**API version** - a dated version string, like 2023-09-01, that tells Azure which version of a resource's schema you're using.

**Schema** - the shape a JSON file is supposed to follow: which fields are required, what type each value should be.

# Bicep

**Bicep** - a simpler language that compiles down into ARM JSON. You write Bicep, Azure still deploys ARM JSON underneath it.

**Decorator** - a tag starting with @ placed above a parameter to add a rule, like @allowed([...]) or @secure().

**Scope** - where a deployment targets: resource group, subscription, or management group.

**Interpolation** - dropping a variable's value directly inside a string using ${} syntax.

**Compile** - turning a .bicep file into the ARM JSON that actually gets deployed (az bicep build).

**Decompile** - the reverse: turning an existing ARM JSON template back into Bicep (az bicep decompile).

# Terraform

**HCL (HashiCorp Configuration Language)** - the language Terraform files are written in, ending in .tf.

**Resource block** - the chunk of HCL defining one piece of infrastructure to create.

**State file** - a JSON file Terraform keeps (terraform.tfstate) tracking what it has already built, so it knows what's real versus what's just in your code.

**Plan** - a preview of what Terraform would change, generated with terraform plan, before anything actually happens.

**Apply** - the command that takes the plan and actually creates or changes the real resources.

**Data source** - a way to pull in information about something that already exists, without Terraform managing or creating it.

**count / for_each** - meta-arguments that let one resource block create multiple copies of itself from a number or a list.
"""

SCAFFOLD_SECTIONS = [
    (
        "powershell",
        "PowerShell",
        [
            ("01-variables-and-output", "Variables, Data Types, and Output", "ps1"),
            ("02-control-flow", "Control Flow: If/Else, Switch, Loops", "ps1"),
            ("03-functions", "Functions: Params, Return Values, Scope", "ps1"),
            ("04-arrays-and-hashtables", "Arrays and Hashtables", "ps1"),
            ("05-the-pipeline", "The Pipeline: Where-Object, Sort-Object, Select-Object", "ps1"),
            ("06-string-manipulation", "String Manipulation and Formatting", "ps1"),
            ("07-error-handling", "Error Handling: Try/Catch/Finally", "ps1"),
            ("08-files-and-csv", "Files: Get-Content, Set-Content, CSV Import/Export", "ps1"),
            ("09-json-in-powershell", "JSON in PowerShell: ConvertTo-Json / ConvertFrom-Json", "ps1"),
            ("10-script-structure", "Script Structure: Params Blocks, Comment-Based Help", "ps1"),
            ("11-az-powershell-basics", "Az PowerShell Module Basics", "ps1"),
        ],
    ),
    (
        "bicep-arm-json",
        "Bicep, ARM, and JSON",
        [
            ("01-arm-json-anatomy", "ARM JSON Anatomy", "json"),
            ("02-bicep-basics", "Bicep Basics: JSON to Bicep", "bicep"),
            ("03-parameters-and-variables", "Parameters and Variables", "bicep"),
            ("04-outputs", "Outputs", "bicep"),
            ("05-expressions-and-functions", "Expressions and Built-In Functions", "bicep"),
            ("06-conditionals-and-loops", "Conditionals and Loops", "bicep"),
            ("07-modules", "Modules", "bicep"),
            ("08-dependencies", "Dependencies: Implicit vs Explicit", "bicep"),
            ("09-array-loops-multiple-resources", "Array Loops for Multiple Resources", "bicep"),
            ("10-deployment-scopes", "Deployment Scopes", "bicep"),
            ("11-what-if-and-validation", "What-If and Validation Workflow", "bicep"),
            ("12-decompile-arm-to-bicep", "Decompiling ARM to Bicep", "bicep"),
        ],
    ),
    (
        "terraform",
        "Terraform",
        [
            ("01-iac-concepts-and-providers", "IaC Concepts, Providers, Resource Blocks", "tf"),
            ("02-core-workflow", "Core Workflow: Init, Plan, Apply, Destroy", "tf"),
            ("03-variables-and-outputs", "Variables and Outputs", "tf"),
            ("04-state", "State: What It Is and Why It Matters", "tf"),
            ("05-azurerm-provider", "The azurerm Provider", "tf"),
            ("06-resource-dependencies", "Resource Dependencies", "tf"),
            ("07-data-sources", "Data Sources", "tf"),
            ("08-count-and-for-each", "count and for_each", "tf"),
            ("09-modules", "Writing and Calling Modules", "tf"),
            ("10-remote-state-basics", "Remote State Basics (HCP Terraform)", "tf"),
            ("11-lifecycle-blocks", "Lifecycle Blocks", "tf"),
            ("12-plan-output-and-state-commands", "Reading Plan Output and terraform state Commands", "tf"),
        ],
    ),
]

def _stub_lesson(title: str) -> str:
    return f"""# {title}

## Status
Not started

## Lesson
(To be filled in when you start this module.)

## Key Terms
See GLOSSARY.md at the repo root for terms used in this module.
"""

def _stub_problem(title: str) -> str:
    return f"""# Problem: {title}

(Problem to be added when you start this module.)
"""

def _stub_solution(ext: str) -> str:
    comment = "#" if ext in ("ps1", "tf") else "//"
    return f"{comment} Solution - write your work here\n"

def _write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content)
    return True

def scaffold(base: Path):
    """Creates the full repo skeleton: all 3 sections' stub folders, README.md,
    GLOSSARY.md. Never overwrites a file that already exists, so it's safe to
    call even after other sections have already been populated for real."""
    base.mkdir(exist_ok=True)
    _write_if_missing(base / "GLOSSARY.md", GLOSSARY_CONTENT)
    _write_if_missing(base / "ENVIRONMENT-SETUP.md", ENVIRONMENT_SETUP_CONTENT)

    readme_lines = [
        "# IaC Fundamentals Bootcamp",
        "",
        "Hands-on bootcamp covering PowerShell, Bicep/ARM/JSON, and Terraform in one repo.",
        "Each module has a lesson.md, a problem.md, and a solution file. Work modules in any order.",
        "See GLOSSARY.md for terminology.",
        "",
    ]
    for folder, title, modules in SCAFFOLD_SECTIONS:
        section_path = base / folder
        section_path.mkdir(exist_ok=True)
        readme_lines.append(f"# {title}")
        readme_lines.append("")
        for slug, mod_title, ext in modules:
            module_path = section_path / slug
            module_path.mkdir(exist_ok=True)
            _write_if_missing(module_path / "lesson.md", _stub_lesson(mod_title))
            _write_if_missing(module_path / "problem.md", _stub_problem(mod_title))
            _write_if_missing(module_path / f"solution.{ext}", _stub_solution(ext))
            readme_lines.append(f"- [ ] {slug}: {mod_title}")
        readme_lines.append("")
    _write_if_missing(base / "README.md", "\n".join(readme_lines))

# --- Environment setup (written once at repo root, alongside README/GLOSSARY) ---

ENVIRONMENT_SETUP_CONTENT = """# Environment Setup

This assumes nothing is installed yet. Do this once, in order, before starting module 1 of any section. Both Windows and RHEL/Linux are covered in full for every tool, pick whichever machine you're on, both work equally well for everything in this repo.

## If a Microsoft package install has failed on RHEL before
Every Microsoft Linux tool below has a way to install as a single downloaded file, no repository registration step at all. Where that applies, it's called out explicitly, use that path first if the dnf-repo method has given you trouble before.

## PowerShell 7

**Windows (winget):**
```powershell
winget install --id Microsoft.PowerShell --source winget
```
Installs the current PowerShell 7 release side by side with the built-in Windows PowerShell 5.1, both can coexist.

**RHEL / Linux, Option A, single RPM, no repo registration (start here if you've had trouble before):**
```bash
sudo dnf install https://github.com/PowerShell/PowerShell/releases/download/v7.6.5/powershell-7.6.5-1.rh.x86_64.rpm
```
Installs directly from one downloaded package. Does not register Microsoft's repository on your system, nothing for subscription-manager to conflict with.

**RHEL / Linux, Option B, tar.gz binary, no root required:**
```bash
curl -L -o /tmp/powershell.tar.gz https://github.com/PowerShell/PowerShell/releases/download/v7.6.5/powershell-7.6.5-linux-x64.tar.gz
mkdir -p ~/powershell
tar -xzf /tmp/powershell.tar.gz -C ~/powershell
~/powershell/pwsh
```
Unpacks into your own home directory. Nothing system-wide, nothing to register, works without sudo.

**RHEL / Linux, Option C, Microsoft's package repository (registers a new repo, most likely to hit prior friction):**
```bash
source /etc/os-release
curl -sSL -O https://packages.microsoft.com/config/rhel/$VERSION_ID/packages-microsoft-prod.rpm
sudo rpm -i packages-microsoft-prod.rpm
sudo dnf install powershell -y
```
Microsoft's documented preferred method, and the one that registers a full repo, the exact step that's caused registration problems before. Use A or B instead if this fails.

**Verify (either OS):** `pwsh --version`

## Azure CLI
Needed for PowerShell module 11, and for every deployment in the Bicep/ARM/JSON section.

**Windows (winget):**
```powershell
winget install --exact --id Microsoft.AzureCLI
```

**Windows (MSI, alternative):**
Download and run the installer from `https://aka.ms/installazurecliwindows`, close and reopen your terminal afterward.

**RHEL / Linux, Option A, universal install script:**
```bash
curl -L https://aka.ms/InstallAzureCli | bash
```
Detects your distro and installs without you manually configuring a repo.

**RHEL / Linux, Option B, dnf with Microsoft's repo (same registration step as PowerShell Option C above):**
```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install -y https://packages.microsoft.com/config/rhel/$(source /etc/os-release; echo $VERSION_ID)/packages-microsoft-prod.rpm
sudo dnf install azure-cli
```

**Either OS, Option C, Azure Cloud Shell, zero install:**
portal.azure.com has a Cloud Shell icon in the top bar, a browser-based terminal with Azure CLI, Bicep, and PowerShell already installed. Nothing local to configure, a good fallback while sorting out a local install.

**Verify (either OS):** `az --version`
**Sign in (either OS):** `az login`

## Bicep CLI
Usually nothing to install separately on either OS. Azure CLI 2.20.0+ installs its own self-contained Bicep CLI automatically the first time you run a command that needs it.
```bash
az bicep version
```
If it's missing:
```bash
az bicep install
```

**Windows (winget), standalone install:**
```powershell
winget install --exact --id Microsoft.Bicep
```

**RHEL / Linux, standalone binary:**
```bash
curl -Lo bicep https://github.com/Azure/bicep/releases/latest/download/bicep-linux-x64
chmod +x ./bicep
sudo mv ./bicep /usr/local/bin/bicep
bicep --help
```
A standalone install is only needed if you're using Bicep from somewhere that doesn't already carry Azure CLI's copy, like a from a script that calls `bicep` directly instead of `az bicep`.

## Terraform

**Windows (winget):**
```powershell
winget install --id Hashicorp.Terraform --exact
```

**RHEL / Linux, HashiCorp's own repository (separate from Microsoft's, hasn't been a source of the friction you've hit before):**
```bash
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo dnf install terraform
```

**Verify (either OS):** `terraform version`

## VS Code extensions
Same three extensions, same names, on both machines. Install from the Extensions panel (Ctrl+Shift+X), search each by name:
- **PowerShell** (by Microsoft), syntax highlighting, IntelliSense, run .ps1 files directly from the editor.
- **Bicep** (by Microsoft), syntax highlighting, autocomplete, inline validation for .bicep files.
- **HashiCorp Terraform** (by HashiCorp), syntax highlighting and autocomplete for .tf files.

## Quick sanity check
Run on whichever machine you're currently on:
```bash
pwsh --version
az --version
az bicep version
terraform version
```
All four returning a version number with no errors means that machine is ready for module 1 of any section. Run the same check on the other machine whenever you switch to it, don't assume both stay in sync automatically.

## Reference
- https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows
- https://learn.microsoft.com/en-us/powershell/scripting/install/install-rhel
- https://learn.microsoft.com/en-us/powershell/scripting/install/alternate-install-methods
- https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows
- https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/install
- https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
"""


# --- Interactive lesson transformation ---
# Applied to every lesson.md at write time. Finds each fenced code block and
# inserts a hands-on checkpoint right after it, so the lesson itself is
# practiced as you read it, not just read and then practiced later in the
# problem. Doesn't require touching the 35 lesson strings by hand, it's a
# consistent transformation applied uniformly across every module.

import re as _re

_CHECKPOINT_TEMPLATES = {
    "powershell": "Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.",
    "json": "Type the code above into a scratch file (try.json) yourself rather than copy-pasting it. Read back through it and confirm you can name what each part is doing before moving on.",
    "bicep": "Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.",
    "hcl": "Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.",
    "bash": "Run the command above yourself in your terminal before reading on, don't just read what it's supposed to do.",
}
_DEFAULT_CHECKPOINT = "Type the code above yourself and try running or reasoning through it before reading on."

_CODE_BLOCK_PATTERN = _re.compile(r'(```([a-zA-Z]*)\n.*?```)', _re.DOTALL)

def make_interactive(lesson_text: str) -> str:
    counter = {"n": 0}

    def _replacer(match: "_re.Match") -> str:
        counter["n"] += 1
        block = match.group(1)
        lang = match.group(2).lower()
        instruction = _CHECKPOINT_TEMPLATES.get(lang, _DEFAULT_CHECKPOINT)
        checkpoint = f"\n\n> **Try it now, Checkpoint {counter['n']}**\n> {instruction}\n"
        return block + checkpoint

    result = _CODE_BLOCK_PATTERN.sub(_replacer, lesson_text)

    intro_note = (
        "## Lesson\n\n"
        "*This lesson is interactive. Complete each numbered checkpoint as you reach it, "
        "don't read past it and come back later, the point is building the muscle memory "
        "while the concept is still right in front of you.*\n"
    )
    result = result.replace("## Lesson\n", intro_note, 1)

    return result

def write_module(section_path: Path, slug: str, content: dict):
    module_path = section_path / slug
    module_path.mkdir(parents=True, exist_ok=True)
    (module_path / "lesson.md").write_text(make_interactive(content["lesson"]))
    (module_path / "problem.md").write_text(content["problem"])

def build():
    base = Path(REPO_NAME)
    scaffold(base)  # creates the full repo skeleton if it doesn't exist yet
    section_path = base / SECTION
    section_path.mkdir(parents=True, exist_ok=True)
    for slug, content in MODULES.items():
        write_module(section_path, slug, content)
    print(f"Populated {len(MODULES)} modules in {SECTION}/ (full repo skeleton ensured)")

if __name__ == "__main__":
    build()