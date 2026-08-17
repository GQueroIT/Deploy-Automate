# Resource Dependencies

By the end of this module, you'll be able to create a real dependency between two resources just by referencing an attribute, with zero depends_on.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

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

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.


Because the storage account references azurerm_resource_group.example.name and .location directly, Terraform knows the resource group has to exist first, no extra configuration needed.

### Explicit dependency
depends_on = [ resource_address ], a meta-argument for cases where a real dependency exists but nothing in the code actually references the other resource's attributes, so Terraform has no way to detect it on its own.

### The dependency graph
Terraform builds a full dependency graph from every implicit and explicit relationship across your configuration, then creates and destroys resources in the correct order automatically, running anything unrelated in parallel when it safely can.

### Same idea, different syntax
If you worked through the bicep-arm-json section of this repo, this is the exact same implicit-vs-explicit concept from that section's dependencies module, just expressed in HCL instead of Bicep syntax.

## Troubleshooting

- The dependency doesn't show up correctly in plan even though you referenced an attribute. Confirm you're referencing the actual resource attribute, not a hardcoded copy of the same string that happens to match.
- Changing the resource group triggers unrelated changes elsewhere. That's the dependency graph working correctly, a real upstream change should ripple to anything that depends on it.

## Key Terms
See GLOSSARY.md. Reinforces: Dependency graph.

## Reference
- https://developer.hashicorp.com/terraform/language/resources/behavior

## See Also

- [Bicep module 08, Dependencies: Implicit vs Explicit](../../bicep-arm-json/08-dependencies/lesson.md)
