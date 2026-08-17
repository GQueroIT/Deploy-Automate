# Problem: Files: Get-Content, Set-Content, CSV Import/Export

## Scenario
You want to track new hires in a simple CSV file instead of a spreadsheet someone has to update by hand, and be able to pull a filtered list back out of it whenever HR asks.

## Your task
In solution.ps1:

1. Build an array of at least five PSCustomObjects representing new hires, each with Name, Department, and StartDate (StartDate can just be a string like "2026-08-01" for now).
2. Export that array to a CSV file using Export-Csv.
3. Re-import the CSV into a new variable using Import-Csv.
4. Filter the re-imported data down to hires in one specific department, and print just their names.
5. Bonus: pick a hire whose StartDate is this month, and print a message confirming they're starting soon. Pay attention to what type StartDate actually comes back as after import, and convert it if you need to for the comparison to work correctly.

## Hints
- Hint 1: -NoTypeInformation on Export-Csv keeps a stray type-metadata line out of the top of your CSV file, worth adding as a habit.
- Hint 2: Everything from Import-Csv is a string. If your bonus comparison against "this month" isn't working, check what type StartDate actually is with $hire.StartDate.GetType(), it's probably not what you expect.
- Hint 3: [datetime]"2026-08-01" converts a string into a real date object you can compare and do math on.
