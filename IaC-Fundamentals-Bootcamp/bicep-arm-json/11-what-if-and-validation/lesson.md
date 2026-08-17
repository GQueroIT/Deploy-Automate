# What-If and Validation Workflow

## Status
In progress

## Lesson

### az deployment group validate
Checks that your template will deploy successfully without actually creating anything, a syntax-and-schema level check. Good as a fast first pass, but it doesn't tell you what would actually change in your environment.

```bash
az deployment group validate \
  --resource-group myResourceGroup \
  --template-file main.bicep \
  --parameters @params.json
```

### az deployment group what-if
Goes further than validate: it shows you exactly what would happen, which resources would be created, modified, or deleted, and which specific properties would change, without applying anything. This is your actual safety net before running a deployment against an environment that already has real resources in it.

```bash
az deployment group what-if \
  --resource-group myResourceGroup \
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
