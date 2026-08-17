# Reading Plan Output and terraform state Commands

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### The symbols in plan output
- + create
- - destroy
- ~ update in place
- -/+ destroy and recreate (a full replacement, not an update)

Reading a plan carefully before typing yes isn't a formality, it's the actual safety mechanism the entire workflow is built around. This is where you catch an unexpected replacement (which usually means real downtime, and sometimes real data loss) before it happens instead of after.

### terraform state list
Lists every resource address currently tracked in state, the starting point whenever you need to reference a specific resource with any other state subcommand.

### terraform state show
```
terraform state show azurerm_storage_account.example
```

> **Try it now, Checkpoint 1**
> Type the code above yourself and try running or reasoning through it before reading on.

Prints the full set of attributes Terraform has recorded for one specific resource, straight from state, without touching real infrastructure.

### terraform state mv
```
terraform state mv azurerm_storage_account.example azurerm_storage_account.baseline
```

> **Try it now, Checkpoint 2**
> Type the code above yourself and try running or reasoning through it before reading on.

Renames or moves a resource's tracked address in state without destroying and recreating the real underlying object. This matters after any kind of refactor, renaming a resource block, moving a resource into a module, because without it, Terraform sees the old address disappear and a "new" resource appear at the new address, and plans to destroy the old one and create a new one, even though nothing about the real infrastructure needed to change at all.

Takes the OLD address first, then the NEW address, in that order.

### A safety habit worth keeping
All state-modifying subcommands write a local backup file automatically before making any change, because state is genuinely sensitive to corruption. Still, always run terraform plan again after any state mv or similar operation to confirm you actually fixed what you meant to fix, don't just assume the command worked as intended.

## Key Terms
See GLOSSARY.md. New here: Replacement (destroy and recreate, shown as -/+ in plan output), In-place update (a change applied to the existing object without destroying it, shown as ~).

## Reference
- https://developer.hashicorp.com/terraform/cli/commands/state
- https://developer.hashicorp.com/terraform/tutorials/state/state-cli
