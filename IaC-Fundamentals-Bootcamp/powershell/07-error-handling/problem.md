# Problem: Error Handling: Try/Catch/Finally

## Scenario
You want a function that checks whether a given file path exists on disk, and if it doesn't, logs a clean, friendly message instead of letting PowerShell dump a wall of red error text.

## Your task
In solution.ps1, write a function Test-PathSafely that:

1. Accepts a Path parameter (string).
2. Inside a try block, attempts Get-Item on that path, forcing it to be a terminating error so your catch block can actually run.
3. In the catch block, writes a friendly message like "Could not find <path>: <short reason>" using $_.Exception.Message, not the raw error object.
4. In a finally block, writes a message noting the check has completed (this should print whether the file was found or not).
5. Call the function twice: once with a path you know exists, once with a fake path you know doesn't, and confirm both branches behave correctly.

## Hints
- Hint 1: Get-Item on its own won't trigger your catch block for a missing file, by default that's a non-terminating error, you need -ErrorAction Stop on that specific line.
- Hint 2: $_ only means anything inside the catch block itself, it refers to whatever just failed, don't expect it to work outside catch.
- Hint 3: finally always runs, prove it to yourself by adding a Write-Host inside it and confirming it prints in both the success case and the failure case.

## Expected Result
Testing a path you know exists should print a success-flavored message and your finally message. Testing a fake path should print your friendly 'Could not find...' message with the actual reason, not a wall of red PowerShell error text, plus your finally message either way.
