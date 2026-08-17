# Data Sources

By the end of this module, you'll be able to read information about a resource you don't own without Terraform trying to manage it.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### What a data source is
A data block pulls in information about something that already exists, without Terraform creating, owning, or managing it. The syntax mirrors a resource block closely, which is intentional:

```hcl
data "azurerm_resource_group" "existing" {
  name = "rg-shared-networking"
}
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.


Reference it with data.<type>.<label>.<attribute>, for example data.azurerm_resource_group.existing.location.

### Why this matters
Common real-world use: looking up a resource group, virtual network, or image that some other team or process already created and owns, so you can reference its properties without Terraform trying to take ownership of that resource's lifecycle. If you used a resource block instead of a data block for something you don't actually own, Terraform would try to manage (and potentially destroy) something it never should have touched.

### count and for_each work on data blocks too
Just like resources, you can add count or for_each to a data block to look up multiple instances at once, each one addressed independently afterward.

### A useful sanity check
If a data source's lookup can't find anything matching what you specified, Terraform will refuse to plan and error out, that's actually a helpful behavior, it catches typos in resource group names or missing prerequisites before you get further into a broken plan.

## Troubleshooting

- The data source returns an error saying nothing matches. Confirm the resource you're looking up actually exists with that exact name, data sources don't create anything.
- You accidentally wrote a resource block instead of a data block, and plan shows something being created that shouldn't be. Double-check the block type at the top.

## Key Terms
See GLOSSARY.md. New here: Data source (read-only, Terraform looks it up but never creates, modifies, or destroys it, unlike a managed resource).

## Reference
- https://developer.hashicorp.com/terraform/language/data-sources
- https://developer.hashicorp.com/terraform/language/block/data
