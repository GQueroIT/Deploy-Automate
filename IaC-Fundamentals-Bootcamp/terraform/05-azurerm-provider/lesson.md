# The azurerm Provider

By the end of this module, you'll be able to authenticate to Azure and declare your first real azurerm resource.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### What it is
azurerm is HashiCorp's officially maintained provider for Azure, published on the Terraform Registry under the hashicorp/azurerm namespace. It's what actually translates your resource "azurerm_..." blocks into real Azure API calls.

### Authentication
Several authentication methods exist: interactive Azure CLI login, a service principal, or a managed identity. For local practice and learning, the simplest path is having the Azure CLI installed and running az login before you run terraform init, plan, or apply, the azurerm provider can pick up that existing CLI session automatically without you configuring credentials separately inside your Terraform files.

### Naming convention
Almost every resource type in this provider is prefixed azurerm_, for example azurerm_resource_group, azurerm_storage_account, azurerm_virtual_network. If you're not sure a resource type exists, that prefix is the first thing to check for on the Registry.

### The features {} block, again
Covered briefly in module 1: recent versions of the azurerm provider require an explicit features {} block inside provider "azurerm", even completely empty, or terraform init errors out. Some resource types also have provider-specific quirks and required arguments that are genuinely worth checking the Registry's docs page for before writing them from memory, rather than guessing based on what similar resources in Azure usually need.

## Commands Used in This Lesson

- `az login` — Signs in to Azure from the CLI. Example: `az login`
- `terraform init` — Prepares the working directory and downloads required providers. Example: `terraform init`

## Troubleshooting

- terraform plan fails with an authentication error. Run az login again, CLI sessions expire, and azurerm depends on that session being valid.
- Resources plan against the wrong subscription. Check az account show and az account set --subscription if you have access to more than one.

## Key Terms
See GLOSSARY.md. New here: Authentication method (how you prove your identity to a platform before it lets you manage resources on it).

## Reference
- https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
- https://developer.hashicorp.com/terraform/tutorials/configuration-language/configure-providers

## See Also

- [PowerShell module 11, Az PowerShell Module Basics](../../powershell/11-az-powershell-basics/lesson.md)
