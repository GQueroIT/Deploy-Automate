# Problem: Variables, Data Types, and Output

## Scenario
You're building the first piece of an onboarding script for your team. Every time a new hire starts, someone has to figure out their username by hand, and it's always the same pattern: first initial plus last name, lowercase.

## Your task
Write a script (solution.ps1) that:

1. Stores a new employee's first name and last name in two separate variables.
2. Builds a username by combining the first letter of the first name with the full last name, all lowercase. Example: John + Smith becomes jsmith.
3. Displays a friendly on-screen message confirming the generated username, meant purely for whoever is running the script to read. This output should never be capturable by another command down the line.
4. Separately, outputs just the username by itself in a way that could be captured into a variable or piped into another cmdlet.
5. Bonus: add a variable for department and include it in the on-screen message from step 3, but do not include it in the piped output from step 4.

## Hints
- Hint 1: PowerShell builds strings out of variables using double quotes, not single quotes. Single quotes print the literal text, dollar sign and all.
- Hint 2: One cmdlet from this lesson is for the person watching the screen. Another is for handing data to whatever comes next. They are not interchangeable, and using the wrong one will make step 4 impossible to verify.
- Hint 3: String methods like .ToLower() and .Substring() will get you the pieces you need to build the username. You don't need a special cmdlet for this, strings in PowerShell already have these methods built in.

## Expected Result
Running your script should print an on-screen message like 'Generated username: jsmith' (from Write-Host) and separately output just 'jsmith' in a way you could capture into a variable. For John Smith, the username should be exactly jsmith, all lowercase.
