# Problem: Writing and Calling Modules

## Scenario
Your resource group + storage account pattern from earlier modules is something you'll want to stand up repeatedly for different projects. Time to turn it into a real reusable child module.

## Your task
1. Create a directory modules/storage-baseline/ with its own main.tf, variables.tf, and outputs.tf.
2. In variables.tf, define exactly the inputs the module needs: something like resource_group_name, location, and a name prefix for the storage account.
3. In main.tf, put the resource group and storage account resources, using the module's own variables, not anything from outside the module.
4. In outputs.tf, expose only what a caller would actually need, the storage account name and its resource ID, nothing else.
5. In your root solution.tf, call this module twice with two different name prefixes, standing up two separate environments from the same module code.

## Hints
- Hint 1: A child module's variables.tf has no idea what variables exist in your root configuration, everything it needs has to be explicitly passed in through the module block's arguments, there's no implicit sharing.
- Hint 2: Calling the same module twice means giving each call a different local name (module "dev_storage" and module "prod_storage", for example), and each call needs to result in different actual resource names to avoid a naming collision in Azure.
- Hint 3: Reference an output from either call in your root file as module.dev_storage.storage_account_name, the local name you gave the module call is part of the reference path.
