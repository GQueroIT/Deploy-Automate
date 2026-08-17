# Writing and Calling Modules

By the end of this module, you'll be able to package resources into a reusable child module and call it more than once with different inputs.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### Root modules and child modules
Every Terraform configuration is technically a module. The one you run terraform apply on directly is the root module. Anything it calls is a child module. This distinction matters once you start organizing real infrastructure.

### Standard child module layout
```
modules/
  storage-baseline/
    main.tf        # resources
    variables.tf   # input variables
    outputs.tf     # exposed outputs
    README.md
```

> **Try it now, Checkpoint 1**
> Type the code above yourself and try running or reasoning through it before reading on.


### Calling a module
```hcl
module "storage" {
  source              = "./modules/storage-baseline"
  resource_group_name = azurerm_resource_group.example.name
  location             = azurerm_resource_group.example.location
}
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.


The module's own variables.tf defines exactly what it accepts as input, that's its interface. The calling (root) module supplies values for those variables directly as arguments inside the module block, it does not, and cannot, reach into the child module's internal resources directly.

### A module's outputs are how data flows back out
```hcl
output "storage_account_name" {
  value = module.storage.storage_account_name
}
```

> **Try it now, Checkpoint 3**
> Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.


Reference a child module's output from the calling file as module.<local-name>.<output-name>.

### Design guidance worth internalizing early
Only expose the outputs a caller actually needs, don't leak internal implementation details just because they're technically available. And a module that's just a thin wrapper around a single resource type, with no real abstraction added, usually isn't worth the extra layer, if you can't name the module something other than the resource type it wraps, that's often a sign to just use the resource directly instead.

## Commands Used in This Lesson

- `terraform apply` — Executes a plan and actually creates or changes real resources. Example: `terraform apply`

## Troubleshooting

- Calling the module a second time reuses the same resource names and collides. Each module call needs distinct input values, not just a distinct local name for the call itself.
- A variable you expect the child module to see isn't available inside it. Nothing is implicitly shared, every value the module needs has to be explicitly passed in.

## Key Terms
See GLOSSARY.md. New here: Root module (the top-level configuration you run apply on), Child module (a reusable module called by another configuration), Interface (the specific inputs a module accepts and outputs it exposes, its contract with whatever calls it).

## Reference
- https://developer.hashicorp.com/terraform/language/modules/develop
- https://developer.hashicorp.com/terraform/language/block/module

## See Also

- [Bicep module 07, Modules](../../bicep-arm-json/07-modules/lesson.md)
