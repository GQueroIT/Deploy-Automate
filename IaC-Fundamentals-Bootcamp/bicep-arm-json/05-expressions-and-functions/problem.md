# Problem: Expressions and Built-In Functions

## Scenario
Your module 2 storage account solution has a name that was either fully hardcoded or passed in as a required parameter every time, which means either it'll collide with someone else's globally, or you have to remember to type something unique every single deployment.

## Your task
Fix it in solution.bicep:

1. Remove any hardcoded storage account name.
2. Build the storage account name from a short prefix combined with uniqueString(resourceGroup().id), using string interpolation.
3. Replace any hardcoded region/location value with resourceGroup().location instead.
4. Compile the file and confirm the generated name is a valid storage account name (lowercase letters and numbers only, no dashes, no uppercase, under 24 characters total).

## Hints
- Hint 1: uniqueString() returns a fixed-length string of lowercase letters and numbers, that's exactly the character set storage account names require, which is part of why it's the standard tool for this.
- Hint 2: Storage account names cannot contain dashes or uppercase letters, if your prefix has either, the deployment will reject it even though the uniqueString() portion is fine.
- Hint 3: Because uniqueString(resourceGroup().id) is deterministic, redeploying this same file into the same resource group will always compute the exact same name, that's a feature, not a bug, it's what keeps redeployments idempotent instead of creating duplicates.

## Expected Result
Compiling twice in a row without changing anything should produce the exact same storage account name both times, that's the deterministic part working. The name should contain only lowercase letters and numbers.

## Cost & Cleanup
If you deployed this for real, clean up when you're done: az group delete --name <your-rg> --yes --no-wait.
