# Outputs

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
