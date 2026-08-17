# Parameters and Variables

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

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

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.


Bicep allows a maximum of 256 parameters per file, and parameter names can only contain letters, digits, and underscores (no periods, unlike ARM JSON).

### Variables
var <variable-name> = <variable-value>, type is usually inferred from the value rather than declared explicitly. Variables can also use decorators, and you're limited to 512 variables per file.

```bicep
var resourcePrefix = 'app'
var instanceCount = environment == 'prod' ? 5 : 2
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.


That ternary (condition ? valueIfTrue : valueIfFalse) is a common pattern for computing a variable based on a parameter.

## Key Terms
See GLOSSARY.md. New here: Decorator, Sensitive value (data that shouldn't be exposed in logs or output, like a password).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameters
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/variables
