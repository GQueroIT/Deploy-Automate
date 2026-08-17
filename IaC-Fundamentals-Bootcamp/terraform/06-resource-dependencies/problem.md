# Problem: Resource Dependencies

## Scenario
You need a storage account that lives inside the resource group from module 5, and you want to prove the dependency is real by letting Terraform infer it, not by forcing it with depends_on.

## Your task
In solution.tf:

1. Add an azurerm_storage_account resource.
2. Set its resource_group_name and location arguments by referencing azurerm_resource_group.example.name and .location directly, not by retyping the values as separate strings or variables.
3. Run terraform plan and read the output carefully, confirm the resource group is listed as being created before the storage account, even though you didn't add any dependsOn.
4. In a comment, explain in your own words why this dependency exists without you having written it explicitly.

## Hints
- Hint 1: If you accidentally hardcode the resource group name as a plain string instead of referencing the resource's attribute, the implicit dependency disappears completely, Terraform would have no way to know the two resources are related.
- Hint 2: Storage account names have their own rules (lowercase letters and numbers only, globally unique across Azure), keep that in mind when picking a test name here, same rule as the Bicep section of this repo.
- Hint 3: terraform plan output lists resources roughly in dependency order when there's a real relationship, that ordering itself is a clue you can use to sanity-check whether Terraform actually detected the dependency you intended.

## Expected Result
terraform plan should list the resource group before the storage account, reflecting the dependency, even though you never wrote depends_on.

## Cost & Cleanup
Storage accounts here are minimal cost, but don't leave them running, terraform destroy when you're done.
