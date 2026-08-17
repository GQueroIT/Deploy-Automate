# Variables and Outputs

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### Input variables
A variable block defines a named input your configuration accepts, keeping values out of hardcoded resource blocks so the same configuration can be reused with different inputs.

```hcl
variable "resource_group_name" {
  type        = string
  description = "Name of the resource group to create"

  validation {
    condition     = can(regex("^rg-", var.resource_group_name))
    error_message = "Resource group name must start with 'rg-'."
  }
}
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.


Reference it elsewhere in your configuration with var.resource_group_name. The validation block enforces a rule at plan time, using a condition expression (often built with the can() function wrapping something that would otherwise error, like a regex match) and a custom error_message shown when it fails.

### Output values
An output block exposes a value after apply finishes, for you to see in the CLI, for another configuration to consume via remote state (covered later), or for automation to capture.

```hcl
output "storage_account_name" {
  description = "Name of the created storage account"
  value       = azurerm_storage_account.example.name
}
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.


Add sensitive = true to an output (or a variable) to keep its value out of normal CLI output, similar in spirit to Bicep's @secure() decorator from the other section of this repo.

### .tfvars files
Rather than hardcoding variable values or typing them at every plan/apply, you can supply them from a separate file:

```
terraform plan -var-file="dev.tfvars"
```

> **Try it now, Checkpoint 3**
> Type the code above yourself and try running or reasoning through it before reading on.


This is the standard way to keep per-environment values (dev.tfvars, prod.tfvars) out of your core .tf files entirely.

## Commands Used in This Lesson

- `terraform plan` — Previews what would change, without touching anything. Example: `terraform plan`

## Key Terms
See GLOSSARY.md. New here: Input value (a variable's role, accepting data into a configuration), Output value (a value exposed after apply), Validation rule (a condition a variable's value must satisfy before Terraform will proceed).

## Reference
- https://developer.hashicorp.com/terraform/language/values
- https://developer.hashicorp.com/terraform/tutorials/configuration-language/variables
