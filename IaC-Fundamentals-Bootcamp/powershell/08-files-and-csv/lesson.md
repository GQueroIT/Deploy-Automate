# Files: Get-Content, Set-Content, CSV Import/Export

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### Reading and writing plain text
- Get-Content -Path file.txt reads a file and returns an array of strings, one per line. Add -Raw to get the whole file back as a single string instead, useful when you're about to do something like ConvertFrom-Json on it later.
- Set-Content -Path file.txt -Value "text" overwrites the file completely.
- Add-Content -Path file.txt -Value "text" appends to the end instead of overwriting.

### CSV: Import-Csv and Export-Csv
This is where files and the pipeline/object concepts from earlier modules connect. Export-Csv takes PowerShell objects and writes them out as a CSV file, one row per object, one column per property:

```powershell
$newHires | Export-Csv -Path hires.csv -NoTypeInformation
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


Import-Csv does the reverse, reads a CSV and turns each row back into a PowerShell object you can pipe, filter, and sort exactly like any other object:

```powershell
$imported = Import-Csv -Path hires.csv
$imported | Where-Object { $_.Department -eq "IT" }
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


### The gotcha worth knowing up front
Everything that comes back from Import-Csv is a string, even things that look like numbers or dates. If you exported a StartDate as a real date, re-importing it gives you back the text representation of that date, not an actual date object. If you need to compare or sort by it as a real date afterward, you'll need to convert it back explicitly with something like [datetime]$row.StartDate.

If you're ever unsure what type a value actually is, .GetType() tells you directly: $row.StartDate.GetType() prints the underlying type, useful for confirming a suspicion instead of guessing at why a comparison isn't working.

## Key Terms
See GLOSSARY.md. New here: CSV (comma-separated values, a plain-text table format where each line is a row and commas separate the columns).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-content
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-csv
