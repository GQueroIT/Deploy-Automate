# Lifecycle Blocks

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### What lifecycle controls
lifecycle {} is a nested block inside any resource that customizes how Terraform handles that specific resource's create, update, and destroy behavior, overriding Terraform's normal default handling.

### create_before_destroy
By default, when a change requires replacing a resource entirely (something that can't be updated in place due to the platform's own API limitations), Terraform destroys the old one first, then creates the new one. That gap means downtime for anything relying on that resource. create_before_destroy = true reverses the order, build the replacement first, then tear down the old one, reducing or eliminating that gap.

```hcl
resource "azurerm_storage_account" "example" {
  # ...
  lifecycle {
    create_before_destroy = true
  }
}
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.


### prevent_destroy
prevent_destroy = true makes Terraform refuse to destroy that resource, erroring out instead of proceeding. Genuinely useful for anything where accidental deletion would be a serious problem, a production database, an encryption key, a DNS zone.

The real gotcha: this rule only protects the resource while the lifecycle block itself is still present in your configuration. If someone removes the entire resource block from your .tf files, prevent_destroy goes with it, and Terraform will destroy the real object during the next apply anyway, protection bypassed entirely, no error. To legitimately destroy a protected resource, remove the prevent_destroy rule first, apply that change, then destroy, a deliberate two-step process.

### ignore_changes
ignore_changes = [ attribute, ... ] tells Terraform to stop flagging drift on specific attributes, useful when something outside Terraform, an autoscaler, a manual tag someone adds through the portal, legitimately and repeatedly changes a value you don't want constantly fighting with your configuration on every plan. Use ignore_changes = all to ignore every attribute (Terraform can still create and destroy the object, but will never propose an update to it).

## Key Terms
See GLOSSARY.md. New here: Downtime (a gap where a resource is unavailable, relevant to why create_before_destroy exists), reinforces Drift from module 4.

## Reference
- https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle
