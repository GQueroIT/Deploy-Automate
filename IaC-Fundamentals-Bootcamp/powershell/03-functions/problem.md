# Problem: Functions: Params, Return Values, Scope

## Scenario
You keep manually checking disk space on machines when tickets come in about "low disk space" warnings. You want a reusable function instead of typing the same check every time.

## Your task
In solution.ps1, write a function called Get-DiskSpaceStatus that:

1. Accepts a DriveLetter parameter (type string), defaulting to "C" if not supplied.
2. Accepts a WarningThresholdPercent parameter (type int), defaulting to 90 if not supplied.
3. Uses Get-PSDrive to look up the actual drive's used and free space.
4. Calculates the percent used.
5. Returns a custom object (using [PSCustomObject]@{ }) with properties: DriveLetter, PercentUsed, and IsOverThreshold (a boolean).
6. Call the function at least twice: once with defaults, once passing a different drive letter or threshold, and print both results.

## Hints
- Hint 1: Get-PSDrive -Name $DriveLetter returns an object with .Used and .Free properties, in bytes, you'll need both to calculate a percentage.
- Hint 2: You don't need the word return, just leave the [PSCustomObject]@{ } as the last line of the function and it becomes the output automatically.
- Hint 3: Test that scope is really working, try referencing a variable you declared inside the function from outside it after calling it, it should be empty or throw an error, confirming it never left the function.
