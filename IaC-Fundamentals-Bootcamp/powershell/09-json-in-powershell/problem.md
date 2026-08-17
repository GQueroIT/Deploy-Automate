# Problem: JSON in PowerShell

## Scenario
You want to store a small server configuration as a JSON file that other tools (or a future Bicep/ARM deployment) could also read, instead of hardcoding values into every script.

## Your task
In solution.ps1:

1. Build a hashtable representing a config with at least 3 levels of nesting, for example: ServerName, Port, and a nested Tags object containing an array of environment tags, and a nested Monitoring object containing its own nested AlertContacts array.
2. Convert it to JSON with ConvertTo-Json, first WITHOUT specifying -Depth, and print the result, look closely at whether your deepest nested values actually made it into the output.
3. Convert it again WITH an explicit -Depth high enough to capture everything, and compare the two outputs.
4. Save the correctly-depth JSON to a file with Set-Content.
5. Read the file back in with Get-Content -Raw, pipe it through ConvertFrom-Json, and pull out one specific deeply nested value to prove the round trip worked.

## Hints
- Hint 1: The default -Depth is 2. Count how many levels deep your Monitoring.AlertContacts array actually sits, if it's deeper than 2, you'll see it get cut off or collapsed in step 2, that's expected, that's the point of this problem.
- Hint 2: Get-Content without -Raw returns an array of lines, ConvertFrom-Json wants one single string, this will bite you if you forget it here just like in module 8.
- Hint 3: After ConvertFrom-Json, nested values are accessed the same way as any nested object, $parsed.Monitoring.AlertContacts[0].

## Expected Result
With the default -Depth, printed JSON for your nested config should visibly cut off or flatten your deepest nested values. With -Depth set high enough, the same conversion should show every level intact, and reading it back should let you access that deep value directly.
