# Problem: The azurerm Provider

## Scenario
Time to actually declare your first real Azure resource through Terraform, starting with the simplest possible one, a resource group.

## Your task
In solution.tf:

1. Using the variables from module 3 (resource_group_name and location), write an azurerm_resource_group resource.
2. Run terraform plan and confirm it shows exactly 1 resource to add, nothing else.
3. In a comment, note which authentication method you're using to talk to Azure (interactive CLI login, service principal, or something else), and how you confirmed it's actually working before running plan.

## Hints
- Hint 1: az login before running any terraform command is the easiest authentication path for local practice, confirm you're logged into the right subscription with az account show before you plan against it.
- Hint 2: Azure region values for the location argument are lowercase strings like "eastus", not display names like "East US", using the wrong format will cause plan or apply to fail.
- Hint 3: If plan shows more than 1 resource to add, or shows changes to something you didn't expect, check whether you're accidentally still holding onto resources from an earlier module in the same .tf files.

## Expected Result
terraform plan should show exactly 1 resource to add, the resource group, and nothing else. az account show should confirm you're authenticated against the subscription you expect.

## Cost & Cleanup
A resource group by itself is free, but get in the habit now: run terraform destroy when you're done experimenting with each module so nothing lingers.
