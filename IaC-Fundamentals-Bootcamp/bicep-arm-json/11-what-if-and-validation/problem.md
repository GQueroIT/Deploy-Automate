# Problem: What-If and Validation Workflow

## Scenario
Before you run the subscription-level deployment from module 10 for real, you want to confirm it's only going to create things, and nothing you didn't expect.

## Your task
1. Using the solution.bicep from module 10, write out the exact az deployment sub what-if command you'd run to preview it (include the required --location flag).
2. In a comment or a short written note in solution.bicep, describe what you would expect the what-if output to show: how many resources, and whether they should all be marked as Create (+) and nothing else.
3. If you have Azure CLI and an Azure account available, actually run it and compare the real output against your prediction. If not, reason through it carefully based on what you know is in the template.

## Hints
- Hint 1: what-if needs the same --template-file and --location flags as the real deployment command would, just swap create for what-if in the command itself.
- Hint 2: Since this is a brand new resource group and a brand new storage account inside it, every resource in the what-if output should show a + (create), if you see a ~ or a - anywhere, something in the template isn't behaving the way you think it is.
- Hint 3: what-if output can be verbose, focus on the summary section first, which lists each resource and its action, before digging into the detailed property-level diff.

## Expected Result
Your what-if command should include the exact same --template-file and --location values your module 10 deployment would use. Every resource in the summary should be marked as a Create action, nothing else.

## Cost & Cleanup
what-if never creates or changes anything by itself, nothing to clean up from this module alone.
