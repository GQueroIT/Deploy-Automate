# Problem: Data Sources

## Scenario
Instead of creating a brand new resource group every time, you want to reuse the one you already created in module 5, without accidentally telling Terraform to manage it as a resource in this new configuration too.

## Your task
In solution.tf:

1. Add a data "azurerm_resource_group" block looking up the resource group you created in module 5 by name (not creating a new azurerm_resource_group resource here).
2. Add a new azurerm_storage_account resource that references the data source's .location and .name attributes, rather than a resource reference or a hardcoded string.
3. Run terraform plan and confirm it shows only the storage account being created, the resource group itself shows no changes at all, because it's only being read, not managed, by this configuration.

## Hints
- Hint 1: The arguments a specific data source accepts (just name for azurerm_resource_group, for example) come from that data source's page in the provider docs, don't assume every data source takes the same arguments.
- Hint 2: If plan shows the resource group itself as something to be created or modified, you've accidentally used a resource block instead of a data block somewhere, double check the block type.
- Hint 3: Deliberately typo the resource group name and run plan again, watch what error Terraform gives you, that's the sanity-check behavior mentioned in the lesson, worth seeing once on purpose.

## Expected Result
terraform plan should show zero changes to the resource group the data source looked up, only the new storage account should show as something to create.

## Cost & Cleanup
The data source itself costs nothing, it only reads. If you created a real storage account alongside it, terraform destroy when you're done.
