# The azurerm Provider

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

## Key Terms
See GLOSSARY.md. New here: Authentication method (how you prove your identity to a platform before it lets you manage resources on it).

## Reference
- https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
- https://developer.hashicorp.com/terraform/tutorials/configuration-language/configure-providers
