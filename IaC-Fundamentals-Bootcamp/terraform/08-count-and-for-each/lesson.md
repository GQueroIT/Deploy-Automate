# count and for_each

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### count
Set count = N on a resource or module block to create N nearly-identical instances from one block. Each instance is addressed by a zero-based index:

```hcl
resource "azurerm_storage_account" "example" {
  count                    = 3
  name                     = "stg${count.index}${random_id.suffix.hex}"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.


Reference a specific instance with azurerm_storage_account.example[0], [1], etc.

### for_each
Iterate over a map or a set of strings instead of a plain number, each instance addressed by its key rather than a numeric index:

```hcl
resource "azurerm_storage_account" "example" {
  for_each                 = toset(["logs", "backups", "archive"])
  name                     = "stg${each.key}${random_id.suffix.hex}"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.


Reference a specific instance with azurerm_storage_account.example["logs"]. for_each needs a map or a set, toset() converts a plain list into a set for exactly this purpose.

### Why the choice actually matters, not just style
With count, removing an item from the middle of a list shifts every subsequent index down by one. Terraform tracks count-based resources by that index in state, so removing "backups" from a 3-item list can make Terraform think the third item changed, even though you only touched the second one, potentially destroying and recreating something you never meant to touch. for_each tracks by a stable key instead, so removing "backups" only affects the "backups" instance, everything else stays untouched.

HashiCorp's own guidance: use count for genuinely identical instances where index doesn't matter, use for_each when instances need distinct values or a stable identity that survives list changes. You cannot use both on the same block.

## Commands Used in This Lesson

- `toset()` — Converts a list into a set, required for for_each on a plain list of strings. Example: `toset(["a", "b", "c"])`

## Key Terms
See GLOSSARY.md. New here: Meta-argument (a built-in argument, like count, for_each, or depends_on, that works on any resource type and controls Terraform's own behavior rather than the resource's actual configuration), Index vs key (a number based on position, versus a stable name-based identifier).

## Reference
- https://developer.hashicorp.com/terraform/language/meta-arguments/count
- https://support.hashicorp.com/hc/en-us/articles/31348158569363-Terraform-count-versus-for-each-meta-argument
