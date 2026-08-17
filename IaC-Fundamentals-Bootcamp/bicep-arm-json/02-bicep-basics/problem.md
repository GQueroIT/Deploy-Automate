# Problem: Bicep Basics: JSON to Bicep

## Scenario
You've got the raw ARM JSON storage account template from module 1. Now rewrite the same thing in Bicep, and prove to yourself that compiling it produces the same result.

## Your task
1. In solution.bicep, recreate the exact same storage account you hand-wrote in module 1's solution.json: a required storageAccountName parameter, a location parameter with a default, the storage account resource itself, and an output for the resource ID.
2. Run az bicep build --file solution.bicep to compile it to JSON.
3. Open the generated JSON and compare it section by section against your hand-written module 1 solution.json. They won't be identical (Bicep adds its own metadata and generates a languageVersion), but the parameters, resources, and outputs sections should match in substance.
4. Note at least two differences you noticed between what you wrote by hand and what Bicep generated for you automatically.

## Hints
- Hint 1: resourceGroup().location is a common default for a location parameter, it pulls the location from the resource group you're deploying into rather than forcing you to hardcode a region.
- Hint 2: The symbolic name you choose (storageAccount, stg, whatever) has zero effect on the deployed resource's actual name, don't confuse the two.
- Hint 3: If az bicep build errors, read the specific line number and property it's complaining about, Bicep's compiler errors are usually precise about what's missing or malformed.

## Expected Result
az bicep build --file solution.bicep should complete with no errors and produce a .json file. Opening that file, the resources array should contain one storage account matching what you wrote by hand in module 1.

## Cost & Cleanup
If you deployed this for real rather than just compiling, storage accounts on Standard_LRS cost very little, but delete it when you're done: az group delete --name <your-rg> --yes --no-wait.
