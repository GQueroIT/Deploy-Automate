# Problem: Outputs

## Scenario
Another team needs to consume information about the storage account you're deploying, they need the resource ID and the blob endpoint URL, but nothing sensitive should ever show up in deployment history.

## Your task
Working from your module 2 or 3 storage account solution.bicep:

1. Add an output returning the storage account's resource ID.
2. Add an output returning the storage account's primary blob endpoint.
3. Add a third, fake output for a variable called adminPassword (just a placeholder string value is fine), first WITHOUT @secure(), and deploy or compile it to see how it looks in the output.
4. Now add @secure() to that same output and compile again, compare the difference in how it's represented.

## Hints
- Hint 1: A resource's resource ID is available via its symbolic name's .id property, no function call needed.
- Hint 2: The blob endpoint lives nested under .properties.primaryEndpoints.blob on a storage account resource, you'll need to drill into the property path correctly.
- Hint 3: @secure() on an output only works for string or object typed outputs, same restriction as parameters.

## Expected Result
Compiling should produce three outputs. The first two should have plain string values, the third, your @secure() one, should show as hidden or redacted rather than the actual value.

## Cost & Cleanup
If you deployed this for real, clean up when you're done: az group delete --name <your-rg> --yes --no-wait.
