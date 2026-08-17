# Problem: Modules

## Scenario
Your main.bicep file is getting cluttered with every resource inline. You want the storage account logic pulled out into its own reusable file that any future project could call.

## Your task
1. Create a new file storage.bicep (inside this module's folder is fine for the exercise) containing just the storage account resource from earlier modules, with its own param() block for storageAccountName and location, and its own output for the resource ID.
2. In solution.bicep, write a module block that calls storage.bicep, passing in a computed name (using uniqueString() from module 5) and resourceGroup().location.
3. Reference the module's output (the storage account ID) in an output of your main solution.bicep file, to prove data can flow back out of a module.

## Hints
- Hint 1: The module's own params must be satisfied inside the params: {} block of the module call, you can't skip a required one without a default just because it "should" be obvious.
- Hint 2: To reference a module's output from the calling file, use moduleSymbolicName.outputs.outputName, not just the output name by itself.
- Hint 3: The path in module storageModule 'storage.bicep' = { is relative to the calling file's location, keep both files in the same folder for this exercise to keep the path simple.

## Expected Result
Your main file should reference storage.bicep as a module and pass it real parameter values. The module's own file should have no knowledge of anything outside itself.

## Cost & Cleanup
If you deployed this for real, clean up when you're done: az group delete --name <your-rg> --yes --no-wait.
