# Problem: IaC Concepts, Providers, Resource Blocks

## Scenario
Your team is about to start managing Azure resources with Terraform instead of clicking through the portal. Before writing any actual resources, you need the skeleton of a working configuration that Terraform can initialize.

## Your task
In solution.tf, write a Terraform configuration that:

1. Declares that this configuration requires the azurerm provider from the official HashiCorp registry, pinned to a specific major version range so an unexpected update doesn't silently change behavior later.
2. Configures the azurerm provider block correctly, including whatever recent versions of that provider require even when left empty.
3. Adds a short comment above each block explaining in your own words what it does and why it's there, like you're leaving a note for the next tech who opens this file cold.

Don't run terraform init yet unless you already have Terraform installed and Azure CLI authenticated locally. The goal of this module is the structure, not the execution, that comes in module 2.

## Hints
- Hint 1: The azurerm provider's page on the Terraform Registry shows the exact source string and current major version right in its usage example.
- Hint 2: required_providers lives inside a terraform {} block. The provider block that actually configures azurerm is a separate block, outside that terraform {} block.
- Hint 3: Recent azurerm provider versions will error out on terraform init if a specific block is missing from provider "azurerm", even with nothing inside it.

## Expected Result
terraform validate should pass with no errors once your provider block includes the features {} argument. You shouldn't need internet access or real Azure credentials for this module, it's structure only.
