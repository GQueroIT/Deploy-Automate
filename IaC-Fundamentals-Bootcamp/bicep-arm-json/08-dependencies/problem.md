# Problem: Dependencies: Implicit vs Explicit

## Scenario
You need a storage account and a file share inside it, and the file share obviously has to wait for the storage account to exist first. You want to prove you can express that relationship without ever touching dependsOn.

## Your task
In solution.bicep:

1. Declare a storage account resource.
2. Declare a file service resource as a child of that storage account (Microsoft.Storage/storageAccounts/fileServices), using the parent property to link it, not dependsOn.
3. Declare a file share resource as a child of the file service (Microsoft.Storage/storageAccounts/fileServices/shares), again using parent, not dependsOn.
4. Confirm your finished file contains zero dependsOn entries, and that the dependency chain is still fully correct through parent references alone.

## Hints
- Hint 1: The parent property takes the symbolic name of the containing resource, not a string, reference the actual resource you declared above it.
- Hint 2: Nesting three levels deep (storage account, then file service, then share) means each one's parent is the resource declared directly above it, not the original storage account every time.
- Hint 3: If you're tempted to add dependsOn "just to be safe," that's the exact instinct Microsoft's best-practices guidance is warning against, trust the parent reference, it's already creating the dependency.

## Expected Result
Your finished file should have zero occurrences of the word dependsOn, and the compiled output should still show the file share correctly nested under the storage account.

## Cost & Cleanup
Storage accounts and file shares are both low-cost, but nothing here needs to stay running, clean up when you're done: az group delete --name <your-rg> --yes --no-wait.
