# Problem: Arrays and Hashtables

## Scenario
Onboarding keeps asking which default printer to assign each new hire based on their department, and it's always the same mapping. You want to automate the lookup.

## Your task
In solution.ps1:

1. Build a hashtable mapping at least four department names to a default printer name (department is the key, printer name is the value).
2. Build an array of at least four PSCustomObjects representing new hires, each with a Name and a Department property.
3. Loop through the array of new hires, and for each one, look up their department's default printer from the hashtable using the department stored in their object (not a hardcoded department name).
4. Print each new hire's name alongside their assigned printer.
5. Bonus: handle a new hire whose department isn't in the hashtable at all, without the script erroring, print something like "No default printer configured" instead.

## Hints
- Hint 1: You must use bracket notation for this one, $printerByDept[$hire.Department], since the department name is stored in a variable/property, not typed literally. Dot notation won't work here.
- Hint 2: Looking up a missing key in a hashtable with bracket notation returns $null rather than throwing an error, that's what makes the bonus possible, check if the result is $null before printing it.
- Hint 3: [PSCustomObject]@{ Name = "..."; Department = "..." } is the same pattern you used for the server objects in module 2.

## Expected Result
For a hire in a department that exists in your hashtable, you should see their name paired with the correct printer. For a hire in a department that doesn't exist, you should see your 'no default printer configured' message, not an error.
