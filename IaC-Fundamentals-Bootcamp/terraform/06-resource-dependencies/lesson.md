# Resource Dependencies

## Status
In progress

## Lesson

### Implicit dependency
Referencing another resource's attribute inside a different resource block automatically tells Terraform the order things need to be created in, no extra syntax required:

```hcl
resource "azurerm_resource_group" "example" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorage"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
```

Because the storage account references azurerm_resource_group.example.name and .location directly, Terraform knows the resource group has to exist first, no extra configuration needed.

### Explicit dependency
depends_on = [ resource_address ], a meta-argument for cases where a real dependency exists but nothing in the code actually references the other resource's attributes, so Terraform has no way to detect it on its own.

### The dependency graph
Terraform builds a full dependency graph from every implicit and explicit relationship across your configuration, then creates and destroys resources in the correct order automatically, running anything unrelated in parallel when it safely can.

### Same idea, different syntax
If you worked through the bicep-arm-json section of this repo, this is the exact same implicit-vs-explicit concept from that section's dependencies module, just expressed in HCL instead of Bicep syntax.

## Key Terms
See GLOSSARY.md. Reinforces: Dependency graph.

## Reference
- https://developer.hashicorp.com/terraform/language/resources/behavior
