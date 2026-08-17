# Problem: Variables and Outputs

## Scenario
You want your resource group name enforced to follow a naming convention automatically, rather than trusting everyone on the team to remember it by hand, and you want the storage account name available as an output once it's created.

## Your task
In solution.tf:

1. Declare a variable resource_group_name (string), with a validation block requiring it start with "rg-", and a clear error_message if it doesn't.
2. Declare a variable location (string) with a sensible default so it's optional.
3. Add an output storage_account_name that returns the name of a storage account resource (reuse or reference the resource from module 2's structure, or add a placeholder azurerm_storage_account resource here).
4. Create a dev.tfvars file supplying a valid value for resource_group_name (starting with "rg-").
5. Note the exact command you'd run to plan using that tfvars file instead of relying on a default or manual input.

## Hints
- Hint 1: The validation condition pattern condition = can(regex("^rg-", var.resource_group_name)) is a common, reliable way to check a string prefix, can() catches the error a failed regex would otherwise throw and turns it into a clean true/false.
- Hint 2: terraform plan -var-file="dev.tfvars" is the flag, the filename doesn't have to be terraform.tfvars (which loads automatically), naming it dev.tfvars means you have to point at it explicitly.
- Hint 3: An output's value can reference any resource attribute in your configuration, azurerm_storage_account.example.name, exactly like referencing it anywhere else.
