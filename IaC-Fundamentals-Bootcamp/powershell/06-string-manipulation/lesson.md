# String Manipulation and Formatting

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### Quotes, again, but it matters more here
Double quotes interpolate variables ("Hello $name"), single quotes print exactly what's typed, dollar signs and all ('Hello $name' literally prints Hello $name).

### Built-in string methods
Every string in PowerShell already has useful methods attached, you don't need a special cmdlet for basic text manipulation:

- .ToUpper() / .ToLower() — case conversion
- .Trim() — removes leading/trailing whitespace
- .Replace("old", "new") — swaps text
- .Split("delimiter") — breaks a string into an array on a delimiter, this is the one you'll use constantly for parsing
- .Substring(start, length) — pulls out part of a string by position
- .Contains("text") — returns true/false, does the string contain this

```powershell
$line = "2026-08-17 14:32:01 ERROR Disk usage at 95%"
$parts = $line.Split(" ")
$parts[0]   # 2026-08-17
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


### The -f format operator
Used for building formatted strings, especially numbers, padding, and alignment:

```powershell
"{0} is at {1}% usage" -f $driveLetter, $percentUsed
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


### Here-strings for multi-line text
When you need a block of text spanning multiple lines, a here-string keeps it readable instead of a wall of `n escape characters:

```powershell
$report = @"
Server: $serverName
Status: $status
"@
```

> **Try it now, Checkpoint 3**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


## Key Terms
See GLOSSARY.md. New here: Method (a built-in action attached to a value, called with a dot, like .ToUpper()), Format operator (-f, builds a string from a template and values), Here-string (a multi-line string block, opened with @" and closed with "@).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_split
- https://learn.microsoft.com/en-us/dotnet/api/system.string
