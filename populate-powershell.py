#!/usr/bin/env python3
"""
Populates every module in the powershell/ section of IaC-Fundamentals-Bootcamp
with real lesson and problem content, sourced from Microsoft Learn.
Overwrites lesson.md and problem.md in each module folder. Safe to re-run.
Run this from the same directory that contains IaC-Fundamentals-Bootcamp/,
or edit REPO_NAME below to point at it directly.
"""

from pathlib import Path

REPO_NAME = "IaC-Fundamentals-Bootcamp"
SECTION = "powershell"

MODULES = {}

MODULES["01-variables-and-output"] = {
"lesson": """# Variables, Data Types, and Output

## Status
In progress

## Lesson

### What a variable actually is
A PowerShell variable is a named storage location for a value. Every variable name starts with a dollar sign: $name, $serverCount, $isOnline. You don't declare a type ahead of time like you would in a statically typed language. A variable comes into existence the moment you assign it a value, and PowerShell figures out the type on its own based on whatever you put in it.

```powershell
$firstName = "Gabe"
$ticketCount = 12
$isResolved = $false
```

That's it. No int ticketCount = 12;, no upfront declaration. This is called being dynamically typed, and it's one of the first things that trips people up coming from a language that forces you to declare types.

### Putting a variable inside a bigger string
You'll need this for the problem below, so it's worth covering now instead of waiting. Double-quoted strings don't just hold variables, they can have a variable's value dropped directly inside them. This is called string interpolation:

```powershell
$firstName = "Gabe"
"Hello, $firstName"    # outputs: Hello, Gabe
```

PowerShell sees the $firstName inside the double-quoted string and swaps in its value automatically. This only works with double quotes. The same line with single quotes, 'Hello, $firstName', prints the literal text $firstName, dollar sign and all, because single quotes never interpolate.

### Two string methods you'll need for this module's problem
The full lesson on string manipulation is module 6, but the problem below needs two small pieces of it now, so here they are early:

- .ToLower() converts a string to all lowercase: "SMITH".ToLower() gives you "smith".
- .Substring(start, length) pulls out part of a string by position, counting from 0: "Gabe".Substring(0, 1) gives you "G", the first character.

Both are called directly on a string or a variable holding one, with a dot, no separate cmdlet needed:

```powershell
$firstName = "Gabe"
$firstInitial = $firstName.Substring(0, 1)   # "G"
$lowered = $firstName.ToLower()               # "gabe"
```

### Automatic and preference variables
PowerShell also comes with variables it creates and manages for you. Automatic variables like $_ (the current object in a pipeline) or $PSHOME (the install path) store state PowerShell itself needs, and by convention you don't overwrite them even though technically you could. Preference variables like $ErrorActionPreference control how PowerShell behaves and you can change those on purpose. You don't need to memorize the full list right now, just know these two categories exist and that a $ doesn't always mean "a value I made up."

### Write-Host vs Write-Output, this is the one that actually matters
Both cmdlets can print text to your screen, and that's exactly why people mix them up. The difference is what happens to the value after you write it.

- Write-Host sends output straight to the console for a human to read. It uses the object's .ToString() method and nothing more happens to it. It is not sent down the pipeline. If you use Write-Host inside a function and try to capture the result in a variable, you get nothing. It's gone the moment it's printed.
- Write-Output sends the value into the pipeline. That means it can be captured into a variable, piped into the next cmdlet, or returned as the result of a function.

Microsoft's own PSScriptAnalyzer linter actually flags Write-Host inside functions as a rule violation (AvoidUsingWriteHost) unless the function is explicitly a display-only function using a Show- verb. The reasoning: if you write a function meant to be reused, and you hardcode Write-Host messages into it, nobody downstream can capture or suppress that output. Write-Output, or just leaving a value as the last line of a function (implicit output), is the reusable way to do it.

Rule of thumb: if the message is for the person sitting at the keyboard right now, Write-Host is fine. If the value needs to go anywhere else, a variable, another cmdlet, a return value, use Write-Output or implicit output instead.

## Key Terms
See GLOSSARY.md at the repo root. This module leans on: Variable, Cmdlet, Pipeline, Object, Parameter.

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_variables
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-host
- https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/rules/avoidusingwritehost
""",
"problem": """# Problem: Variables, Data Types, and Output

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
"""
}

MODULES["02-control-flow"] = {
"lesson": """# Control Flow: If/Else, Switch, Loops

## Status
In progress

## Lesson

### Comparison operators are not what you're used to
PowerShell does not use ==, !=, >, or < for comparisons. It uses word-based operators instead:

- -eq (equal), -ne (not equal)
- -gt, -lt, -ge, -le (greater than, less than, greater or equal, less or equal)
- -like (wildcard string match), -match (regex string match)

```powershell
if ($status -eq "Down") {
    Write-Host "Needs attention"
}
```

This trips up everyone coming from another language at first. -eq is not a typo, it's the actual operator.

### if / elseif / else
Standard branching, same shape you've seen in other languages, just with PowerShell's comparison operators:

```powershell
if ($status -eq "Down") {
    Write-Host "$name is down"
} elseif ($status -eq "Degraded") {
    Write-Host "$name is degraded"
} else {
    Write-Host "$name is fine"
}
```

### switch
When you've got more than two or three elseif branches checking the same variable, switch is cleaner:

```powershell
switch ($status) {
    "Down"     { Write-Host "Down" }
    "Degraded" { Write-Host "Degraded" }
    default    { Write-Host "OK" }
}
```

switch can also match wildcards (-Wildcard) or regular expressions (-Regex), and it can evaluate directly against an array, running once per matching item.

### Loops
- foreach ($item in $collection) { } steps through each item in an array one at a time. This is the loop you'll use most.
- for ($i = 0; $i -lt 10; $i++) { } is a counted loop, useful when you specifically need the index number.
- while (condition) { } runs as long as the condition stays true, checked before each pass.
- do { } while (condition) / do { } until (condition) runs the body at least once before checking the condition.

break exits a loop immediately. continue skips to the next iteration.

## Key Terms
See GLOSSARY.md. New here: Boolean, Operator, Loop, Iteration. A Boolean is a value that's only ever true or false, like $isResolved from module 1. An Operator is a symbol or keyword (like -eq) that compares or combines values. A Loop repeats a block of code. Each single pass through a loop is one Iteration.

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_comparison_operators
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_if
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_switch
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_foreach
""",
"problem": """# Problem: Control Flow: If/Else, Switch, Loops

## Scenario
Your team monitors ten servers. You've got a list of server names, each with a status of "Up", "Down", or "Degraded", and you want a script that loops through the list and calls out anything that needs attention.

## Your task
In solution.ps1:

1. Build an array of at least five objects, each with a Name and a Status property (Up, Down, or Degraded). You can build these with [PSCustomObject]@{ Name = "SERVER01"; Status = "Up" } repeated for each server.
2. Use a foreach loop to step through the array.
3. Inside the loop, use if/elseif/else to print a different message depending on status: something urgent for Down, a warning for Degraded, and a quiet confirmation for Up.
4. Rewrite the same logic a second way using a switch statement on $server.Status instead of if/elseif/else, inside the same loop or a second loop, whichever is cleaner to you.
5. Bonus: count how many servers were Down total, and print that count after the loop finishes.

## Hints
- Hint 1: foreach ($server in $servers) gives you one object per pass, access its properties with $server.Name and $server.Status.
- Hint 2: Remember, comparisons use -eq, not ==. $server.Status -eq "Down" is correct, $server.Status == "Down" will error.
- Hint 3: For the running count, declare a variable before the loop starts (like $downCount = 0) and increment it inside the if block for Down servers, incrementing inside the loop is what makes it a running total instead of resetting every pass.
"""
}

MODULES["03-functions"] = {
"lesson": """# Functions: Params, Return Values, Scope

## Status
In progress

## Lesson

### Defining a function
A function is a named, reusable block of code. PowerShell's naming convention is Verb-Noun, matching the built-in cmdlets, so your own functions blend in and are predictable to read (Get-DiskStatus, not CheckDisk or diskStuff).

```powershell
function Get-DiskStatus {
    param(
        [string]$DriveLetter = "C",
        [int]$WarningThresholdPercent = 90
    )

    $drive = Get-PSDrive -Name $DriveLetter
    # ...logic using $drive...
}
```

### The param() block
Parameters go inside param(), each with a type and optionally a default value. A parameter with a default value is optional to supply when calling the function, exactly like a Bicep parameter with a defaultValue from the other section of this repo. Without a default, PowerShell will actually prompt the person running the script to type a value in interactively, which is rarely what you want, so give sensible defaults or mark it [Parameter(Mandatory)] if you genuinely need to force the caller to supply it.

### Return values
PowerShell doesn't strictly need a return keyword. Anything you output inside a function (via Write-Output, or just leaving an unassigned value as the last line) becomes the function's return value automatically. return does exist and works, mainly useful for exiting a function early.

```powershell
function Add-Numbers {
    param([int]$A, [int]$B)
    $A + $B   # this becomes the return value, no "return" needed
}
```

### Scope
A variable created inside a function only exists inside that function by default, this is local scope. Once the function finishes, that variable is gone, it doesn't leak out and overwrite a variable of the same name outside the function. If you genuinely need a function to change something outside itself, you can reach into $global:variableName, but that's the exception, not the default behavior, and it makes code harder to reason about.

## Key Terms
See GLOSSARY.md. New here: Function, Scope (a variable's scope is where in the script it's visible and usable), Return value.

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_scopes
""",
"problem": """# Problem: Functions: Params, Return Values, Scope

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
"""
}

MODULES["04-arrays-and-hashtables"] = {
"lesson": """# Arrays and Hashtables

## Status
In progress

## Lesson

### Arrays
An array is an ordered collection of values, indexed starting at 0. Build one with @():

```powershell
$servers = @("SERVER01", "SERVER02", "SERVER03")
$servers[0]        # SERVER01
$servers.Count      # 3
$servers += "SERVER04"   # adds a new item
```

Arrays can hold anything, strings, numbers, even other objects, and PowerShell doesn't force every element to be the same type unless you explicitly type the array.

### Hashtables
A hashtable stores key-value pairs instead of an ordered index. Build one with @{}:

```powershell
$printerByDept = @{
    "IT"      = "PRT-IT-01"
    "Sales"   = "PRT-SALES-01"
    "Finance" = "PRT-FIN-01"
}
$printerByDept["IT"]        # PRT-IT-01
$printerByDept.IT           # same thing, dot notation works too
```

Use bracket notation ($hash[$variableName]) when the key itself is stored in a variable, dot notation only works with a literal key name typed directly.

### When to use which
Reach for an array when order matters and you just need a list. Reach for a hashtable when you need to look something up by a name or key rather than by position, exactly like the printer example above, you don't want to remember "IT is index 2", you want to ask for "IT" directly.

## Key Terms
See GLOSSARY.md. New here: Array, Hashtable, Index, Key-value pair.

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_arrays
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_hash_tables
""",
"problem": """# Problem: Arrays and Hashtables

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
"""
}

MODULES["05-the-pipeline"] = {
"lesson": """# The Pipeline: Where-Object, Sort-Object, Select-Object

## Status
In progress

## Lesson

### A quick recap
Back in module 1: PowerShell cmdlets output objects, not plain text, and the pipeline (|) passes those objects from one cmdlet straight into the next. This module is where that actually starts paying off.

### Where-Object: filtering
Filters objects based on a condition. Inside the script block, $_ refers to the current object being evaluated.

```powershell
Get-Process | Where-Object { $_.WorkingSet -gt 100MB }
```

This keeps only processes using more than 100MB of memory. Everything else gets filtered out before it reaches the next cmdlet in the pipeline.

### Finding property names with Get-Member
Before you can filter or sort by a property, you need to know it exists and what it's actually called. Get-Member lists every property and method attached to whatever object comes through the pipeline:

```powershell
Get-Process | Get-Member
```

This is how you confirm a property name instead of guessing at it, run it once, scan the list, then use the exact name you find in your Where-Object or Sort-Object.

### Sort-Object: ordering
Sorts objects by a property. Add -Descending to flip the order.

```powershell
Get-Process | Sort-Object -Property WorkingSet -Descending
```

### Select-Object: picking properties or limiting count
Two different jobs live in this one cmdlet: picking specific properties to keep, and limiting how many objects come through.

```powershell
Get-Process | Select-Object -Property Name, WorkingSet -First 5
```

### Chaining it together
The real power is stacking these in a pipeline, filter, then sort, then trim down to what you actually need to see:

```powershell
Get-Process |
    Where-Object { $_.WorkingSet -gt 100MB } |
    Sort-Object -Property WorkingSet -Descending |
    Select-Object -Property Name, WorkingSet -First 5
```

## Key Terms
See GLOSSARY.md. New here: Filter (narrowing a set of objects down by a condition), Script block (the { } code passed to Where-Object, treated as a chunk of code rather than run immediately), Property (a named piece of data attached to an object, like .WorkingSet on a process).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/sort-object
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/select-object
""",
"problem": """# Problem: The Pipeline: Where-Object, Sort-Object, Select-Object

## Scenario
A machine is running slow and you want a quick way to see what's actually eating memory, without scrolling through every single running process.

## Your task
In solution.ps1, write a single pipeline (you can run this against your own real machine) that:

1. Starts with Get-Process.
2. Filters down to only processes using more than some memory threshold you choose (start with something reasonable like 50MB so you actually get results).
3. Sorts the remaining processes by WorkingSet, highest first.
4. Selects only the Name and WorkingSet properties.
5. Limits the output to the top 5 results.
6. Print or display the final result.

## Hints
- Hint 1: WorkingSet is the property name for memory usage on a process object, confirm this yourself by running Get-Process | Get-Member and looking for it in the property list, rather than trusting it blind.
- Hint 2: The order of the pipeline matters for performance, filter first with Where-Object before sorting, so you're not sorting a huge list you're about to throw most of away anyway.
- Hint 3: -First belongs to Select-Object, not Sort-Object, don't try to limit the count in the wrong cmdlet.
"""
}

MODULES["06-string-manipulation"] = {
"lesson": """# String Manipulation and Formatting

## Status
In progress

## Lesson

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

### The -f format operator
Used for building formatted strings, especially numbers, padding, and alignment:

```powershell
"{0} is at {1}% usage" -f $driveLetter, $percentUsed
```

### Here-strings for multi-line text
When you need a block of text spanning multiple lines, a here-string keeps it readable instead of a wall of `n escape characters:

```powershell
$report = @"
Server: $serverName
Status: $status
"@
```

## Key Terms
See GLOSSARY.md. New here: Method (a built-in action attached to a value, called with a dot, like .ToUpper()), Format operator (-f, builds a string from a template and values), Here-string (a multi-line string block, opened with @" and closed with "@).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_split
- https://learn.microsoft.com/en-us/dotnet/api/system.string
""",
"problem": """# Problem: String Manipulation and Formatting

## Scenario
Your monitoring tool spits out raw log lines like this, and you need to pull the useful pieces out by hand before you can do anything with them:

`2026-08-17 14:32:01 ERROR Disk usage at 95% on SERVER01`

## Your task
In solution.ps1:

1. Store that exact log line in a variable as a single string.
2. Use .Split() to break it into its pieces: date, time, level, and the rest of the message.
3. Pull out just the server name from the end of the message (SERVER01).
4. Pull out just the percentage number (95) as its own value.
5. Using the -f format operator, print a clean one-line summary like: [ERROR] SERVER01 is at 95% disk usage (logged 14:32:01).

## Hints
- Hint 1: .Split(" ") on the whole line gives you an array, but the message itself also contains spaces, so splitting on space alone gives you more pieces than just 4, think about how many pieces you actually need vs. how many you get, and consider .Split(" ", 4) which limits the number of resulting pieces.
- Hint 2: The percentage and server name are both embedded inside that last chunk of text, you'll need a second, smaller split or .Replace() on just that piece rather than trying to solve it in one split.
- Hint 3: -f uses positional placeholders like {0} and {1} that get replaced in order by whatever values you list after the -f, in the order you list them.
"""
}

MODULES["07-error-handling"] = {
"lesson": """# Error Handling: Try/Catch/Finally

## Status
In progress

## Lesson

### The basic shape
```powershell
try {
    # code that might fail
} catch {
    # runs only if something in try failed
} finally {
    # always runs, whether it failed or not
}
```

finally is optional, use it for cleanup that has to happen either way, closing a connection, deleting a temp file.

### Terminating vs non-terminating errors
This is the part that actually trips people up: try/catch only catches terminating errors. A lot of built-in cmdlets produce non-terminating errors by default, meaning they print an error message and keep going, without ever triggering your catch block. To force a cmdlet to treat its own error as terminating (so catch can actually see it), add -ErrorAction Stop to that specific command:

```powershell
try {
    Get-Item -Path "C:\\DoesNotExist" -ErrorAction Stop
} catch {
    Write-Host "Failed: $($_.Exception.Message)"
}
```

Without -ErrorAction Stop on that Get-Item call, the catch block would silently never run, even though the command clearly failed.

### Reading the error inside catch
Inside a catch block, $_ refers to the error record itself. $_.Exception.Message gives you the human-readable reason it failed, which is what you want to log or display instead of dumping a full stack trace on someone.

### throw
You can raise your own error deliberately with throw "some message", useful inside a function when a condition means it genuinely can't continue.

## Key Terms
See GLOSSARY.md. New here: Exception (the object PowerShell creates describing what went wrong), Terminating error (stops execution immediately, catchable), Non-terminating error (reported but execution continues, not caught by try/catch unless forced with -ErrorAction Stop).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_try_catch_finally
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_throw
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_automatic_variables
""",
"problem": """# Problem: Error Handling: Try/Catch/Finally

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
"""
}

MODULES["08-files-and-csv"] = {
"lesson": """# Files: Get-Content, Set-Content, CSV Import/Export

## Status
In progress

## Lesson

### Reading and writing plain text
- Get-Content -Path file.txt reads a file and returns an array of strings, one per line. Add -Raw to get the whole file back as a single string instead, useful when you're about to do something like ConvertFrom-Json on it later.
- Set-Content -Path file.txt -Value "text" overwrites the file completely.
- Add-Content -Path file.txt -Value "text" appends to the end instead of overwriting.

### CSV: Import-Csv and Export-Csv
This is where files and the pipeline/object concepts from earlier modules connect. Export-Csv takes PowerShell objects and writes them out as a CSV file, one row per object, one column per property:

```powershell
$newHires | Export-Csv -Path hires.csv -NoTypeInformation
```

Import-Csv does the reverse, reads a CSV and turns each row back into a PowerShell object you can pipe, filter, and sort exactly like any other object:

```powershell
$imported = Import-Csv -Path hires.csv
$imported | Where-Object { $_.Department -eq "IT" }
```

### The gotcha worth knowing up front
Everything that comes back from Import-Csv is a string, even things that look like numbers or dates. If you exported a StartDate as a real date, re-importing it gives you back the text representation of that date, not an actual date object. If you need to compare or sort by it as a real date afterward, you'll need to convert it back explicitly with something like [datetime]$row.StartDate.

If you're ever unsure what type a value actually is, .GetType() tells you directly: $row.StartDate.GetType() prints the underlying type, useful for confirming a suspicion instead of guessing at why a comparison isn't working.

## Key Terms
See GLOSSARY.md. New here: CSV (comma-separated values, a plain-text table format where each line is a row and commas separate the columns).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-content
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-csv
""",
"problem": """# Problem: Files: Get-Content, Set-Content, CSV Import/Export

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
"""
}

MODULES["09-json-in-powershell"] = {
"lesson": """# JSON in PowerShell: ConvertTo-Json / ConvertFrom-Json

## Status
In progress

## Lesson

### Turning PowerShell objects into JSON, and back
ConvertTo-Json takes a PowerShell object, hashtable, array, custom object, whatever, and turns it into a JSON-formatted string. This is called serialization, packaging a value into a portable text format.

```powershell
$config = @{
    ServerName = "SERVER01"
    Port = 443
    EnableLogging = $true
}
$config | ConvertTo-Json
```

ConvertFrom-Json does the reverse, deserialization, taking a JSON string and turning it back into a usable PowerShell object (a PSCustomObject):

```powershell
$json = Get-Content -Path config.json -Raw
$parsed = $json | ConvertFrom-Json
$parsed.ServerName
```

Notice the -Raw on Get-Content here, this matters. ConvertFrom-Json expects one single string, not an array of line-strings, which is what Get-Content returns by default. Skip -Raw and this will fail or behave unexpectedly.

### The -Depth gotcha
ConvertTo-Json only goes 2 levels deep into nested objects by default. If your data has arrays inside objects inside objects, anything past that default depth gets flattened or truncated, silently, no error. If you're converting anything with real nesting, set -Depth explicitly higher than you think you need:

```powershell
$config | ConvertTo-Json -Depth 10
```

### Why this matters beyond just PowerShell
This is the exact same JSON format you hand-wrote in the bicep-arm-json section of this repo for ARM templates. Same format, different producer and consumer, a config file, an API response, an ARM template, it's all just JSON, and now you can move data between PowerShell and any of it.

## Key Terms
See GLOSSARY.md. New here: Serialization (converting a value into a storable/transmittable format like JSON), Deserialization (the reverse, turning that format back into a usable value).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertto-json
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertfrom-json
""",
"problem": """# Problem: JSON in PowerShell

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
"""
}

MODULES["10-script-structure"] = {
"lesson": """# Script Structure: Params Blocks, Comment-Based Help

## Status
In progress

## Lesson

### Script-level param blocks
Just like a function can accept parameters, a whole .ps1 script file can too. The param() block has to be the very first real statement in the file, before anything else runs (comments above it are fine):

```powershell
param(
    [string]$DriveLetter = "C",
    [int]$WarningThresholdPercent = 90
)
```

Now the script itself can be called with arguments: .\\Check-Disk.ps1 -DriveLetter D -WarningThresholdPercent 85.

### Comment-based help
A specially formatted comment block that PowerShell's own Get-Help cmdlet can read and display, exactly like the help text for built-in cmdlets:

```powershell
<#
.SYNOPSIS
    Checks disk space against a warning threshold.
.DESCRIPTION
    Looks up a drive's used space and flags it if usage is above the threshold.
.PARAMETER DriveLetter
    The drive letter to check. Defaults to C.
.PARAMETER WarningThresholdPercent
    The percent-used value that triggers a warning. Defaults to 90.
.EXAMPLE
    .\\Check-Disk.ps1 -DriveLetter D -WarningThresholdPercent 85
#>
```

This block needs to sit as the very first thing in the file (above even the param block, or immediately below it, both work, just be consistent) for Get-Help .\\Check-Disk.ps1 -Full to actually find and display it.

### [CmdletBinding()]
Adding [CmdletBinding()] right above your param() block makes your script (or function) behave more like a real built-in cmdlet, it automatically gains support for common parameters like -Verbose and -ErrorAction without you having to build that yourself.

```powershell
[CmdletBinding()]
param(
    [string]$DriveLetter = "C"
)
```

## Key Terms
See GLOSSARY.md. New here: CmdletBinding (an attribute that upgrades a function/script to behave like a real cmdlet), Comment-based help (a structured comment block that PowerShell's help system can read).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_comment_based_help
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_cmdletbindingattribute
""",
"problem": """# Problem: Script Structure: Params Blocks, Comment-Based Help

## Scenario
The Get-DiskSpaceStatus function you wrote back in module 3 works fine, but it's stuck inside your head as "that function I wrote once," it's not a real, documented, callable script yet.

## Your task
Turn it into a proper standalone script:

1. In solution.ps1, add a script-level param() block at the very top (before any other code) exposing DriveLetter and WarningThresholdPercent, same as the function's parameters from module 3.
2. Add [CmdletBinding()] above the param block.
3. Add a full comment-based help block (.SYNOPSIS, .DESCRIPTION, .PARAMETER for each parameter, and at least one .EXAMPLE) either immediately above or immediately below the param block.
4. Move the actual disk-checking logic from module 3's function into the body of this script, using the script's own $DriveLetter and $WarningThresholdPercent instead of function parameters.
5. Confirm it works by mentally running Get-Help .\\solution.ps1 -Full, does everything you'd expect to see actually show up based on what you wrote?

## Hints
- Hint 1: The param() block must be the first executable line, comments and blank lines above it are fine, but no other code, not even a variable assignment, can come before it.
- Hint 2: Comment-based help has to be a single contiguous <# ... #> block, formatted exactly with .SYNOPSIS, .DESCRIPTION etc. each on their own line, not scattered as separate # comments.
- Hint 3: [CmdletBinding()] goes directly above param(), with nothing in between.
"""
}

MODULES["11-az-powershell-basics"] = {
"lesson": """# Az PowerShell Module Basics

## Status
In progress

## Lesson

### Az, not AzureRM
The Az module is the current, actively maintained PowerShell module for managing Azure resources. There's an older module called AzureRM that's now legacy, Microsoft's own guidance is that Az and AzureRM should not be installed side by side on the same system, they define overlapping cmdlets and will conflict. If you're setting this up fresh, you only want Az.

```powershell
Install-Module -Name Az -Repository PSGallery -Force
```

Keep it current later with Update-Module -Name Az -Force.

### Connecting to Azure
Connect-AzAccount opens a browser window for interactive sign-in (with MFA support). You have to do this again every time you start a new PowerShell session, the connection doesn't persist automatically across sessions unless you specifically set that up.

```powershell
Connect-AzAccount
```

### Checking and setting context
Once connected, if your account has access to more than one subscription, PowerShell picks one as the "current context" and every command runs against that subscription until you change it. Always verify before running anything that creates or modifies resources:

```powershell
Get-AzContext                      # what subscription am I currently pointed at?
Get-AzContext -ListAvailable       # what subscriptions do I have access to?
Set-AzContext -Subscription "name-or-id"   # switch to a specific one
```

Running a command against the wrong subscription because nobody checked context first is a genuinely common real-world mistake, get in the habit of checking it early in any script that touches Azure.

### Listing resources and formatting the output
Once connected, Az cmdlets follow the same Verb-Noun pattern as everything else, and the same pipeline concepts from earlier modules apply directly:

```powershell
Get-AzResourceGroup
```

This returns one object per resource group in your current subscription, with properties like ResourceGroupName and Location, exactly like any other PowerShell object. To display just specific properties as a clean table instead of the full default output, pipe it into Format-Table:

```powershell
Get-AzResourceGroup | Format-Table -Property ResourceGroupName, Location
```

Format-Table doesn't change the underlying objects, it only changes how they're displayed on screen. If you tried to capture this into a variable and use it further down a pipeline, you'd get formatted display text back, not usable objects, which is why formatting cmdlets like this one are usually the last thing in a pipeline, not the middle.

## Key Terms
See GLOSSARY.md. New here: Authentication (proving who you are to Azure before it lets you do anything), Context (which subscription/tenant your current session is currently pointed at).

## Reference
- https://learn.microsoft.com/en-us/powershell/azure/install-azps-windows
- https://learn.microsoft.com/en-us/powershell/module/az.accounts/connect-azaccount
""",
"problem": """# Problem: Az PowerShell Module Basics

## Scenario
You're about to start managing Azure resources from PowerShell instead of the portal, and before you write anything that actually changes something, you want a safe, read-only script that confirms exactly what subscription you're pointed at and what already exists there.

## Your task
In solution.ps1:

1. Connect to Azure with Connect-AzAccount (only actually run this if you have an Azure account handy, otherwise write the script as if you would).
2. Retrieve and display the current context with Get-AzContext, specifically call out the subscription name in your output.
3. List every resource group in the current subscription using Get-AzResourceGroup.
4. Display the results as a formatted table showing just the resource group name and location, using Format-Table.
5. Bonus: wrap the whole thing so that if Get-AzContext comes back empty (meaning you're not connected), it prints a clear message telling you to run Connect-AzAccount first, instead of just erroring out further down the script.

## Hints
- Hint 1: Get-AzResourceGroup returns full objects with a lot of properties, Format-Table -Property ResourceGroupName, Location narrows it to just what you want to see.
- Hint 2: Get-AzContext returns $null (or an empty result) if you're not connected yet, that's exactly what you can check for in the bonus.
- Hint 3: Connecting is a one-time-per-session thing, if you're testing this script repeatedly in the same PowerShell window, you don't need to reconnect every single run.
"""
}

# --- Full repo scaffold (creates the whole IaC-Fundamentals-Bootcamp skeleton) ---
# Included so this script can be run standalone, on an empty folder, and still
# produce a complete, valid repo. Only fills in files that don't already exist,
# so it never overwrites content another one of these scripts already populated.

GLOSSARY_CONTENT = """# General IaC Concepts

**Infrastructure as Code (IaC)** - writing your servers, networks, and cloud resources as text files instead of clicking through a portal, so the setup can be saved, reused, and tracked like any other code.

**Declarative** - you describe what the end result should look like, and the tool figures out how to get there. This is how Bicep, ARM, and Terraform work.

**Imperative** - you write out every step in order to make something happen. This is how a PowerShell script works.

**State** - a record of what infrastructure already exists right now, so the tool knows what to change instead of rebuilding everything from scratch every time.

**Idempotent** - running the same thing twice gives you the same result the second time as the first. No duplicate resources, no surprise side effects.

**Provider** - the plugin that lets a tool talk to a specific platform. Terraform's azurerm provider is how Terraform talks to Azure.

**Resource** - a single thing being created or managed: a VM, a storage account, a virtual network.

**Module** - a reusable, packaged chunk of code you call instead of rewriting the same block over and over.

**Deployment** - the actual act of running your code against the cloud and creating or changing real resources.

# PowerShell

**Cmdlet** - pronounced "command-let." A built-in PowerShell command, always named Verb-Noun, like Get-Process or New-Item.

**Pipeline** - the | symbol. Takes the output of one cmdlet and feeds it straight into the next one as input.

**Object** - everything that comes out of a cmdlet in PowerShell is a structured object with properties, not plain text. That's what makes Get-Member and Where-Object work.

**Parameter** - a named input you pass into a cmdlet or function, like -Name or -Path.

**Variable** - a named container holding a value, always starts with $, like $name.

**Script** - a saved .ps1 file containing a sequence of PowerShell commands.

**Function** - a named, reusable block of code inside a script that you call with parameters.

# JSON and ARM

**JSON (JavaScript Object Notation)** - a plain text format for storing structured data as key-value pairs. ARM templates are written in this format.

**ARM template** - a JSON file describing the Azure resources you want deployed. Azure Resource Manager reads it and builds them.

**Resource provider** - the Azure service responsible for a resource type, written like Microsoft.Compute or Microsoft.Storage.

**API version** - a dated version string, like 2023-09-01, that tells Azure which version of a resource's schema you're using.

**Schema** - the shape a JSON file is supposed to follow: which fields are required, what type each value should be.

# Bicep

**Bicep** - a simpler language that compiles down into ARM JSON. You write Bicep, Azure still deploys ARM JSON underneath it.

**Decorator** - a tag starting with @ placed above a parameter to add a rule, like @allowed([...]) or @secure().

**Scope** - where a deployment targets: resource group, subscription, or management group.

**Interpolation** - dropping a variable's value directly inside a string using ${} syntax.

**Compile** - turning a .bicep file into the ARM JSON that actually gets deployed (az bicep build).

**Decompile** - the reverse: turning an existing ARM JSON template back into Bicep (az bicep decompile).

# Terraform

**HCL (HashiCorp Configuration Language)** - the language Terraform files are written in, ending in .tf.

**Resource block** - the chunk of HCL defining one piece of infrastructure to create.

**State file** - a JSON file Terraform keeps (terraform.tfstate) tracking what it has already built, so it knows what's real versus what's just in your code.

**Plan** - a preview of what Terraform would change, generated with terraform plan, before anything actually happens.

**Apply** - the command that takes the plan and actually creates or changes the real resources.

**Data source** - a way to pull in information about something that already exists, without Terraform managing or creating it.

**count / for_each** - meta-arguments that let one resource block create multiple copies of itself from a number or a list.
"""

SCAFFOLD_SECTIONS = [
    (
        "powershell",
        "PowerShell",
        [
            ("01-variables-and-output", "Variables, Data Types, and Output", "ps1"),
            ("02-control-flow", "Control Flow: If/Else, Switch, Loops", "ps1"),
            ("03-functions", "Functions: Params, Return Values, Scope", "ps1"),
            ("04-arrays-and-hashtables", "Arrays and Hashtables", "ps1"),
            ("05-the-pipeline", "The Pipeline: Where-Object, Sort-Object, Select-Object", "ps1"),
            ("06-string-manipulation", "String Manipulation and Formatting", "ps1"),
            ("07-error-handling", "Error Handling: Try/Catch/Finally", "ps1"),
            ("08-files-and-csv", "Files: Get-Content, Set-Content, CSV Import/Export", "ps1"),
            ("09-json-in-powershell", "JSON in PowerShell: ConvertTo-Json / ConvertFrom-Json", "ps1"),
            ("10-script-structure", "Script Structure: Params Blocks, Comment-Based Help", "ps1"),
            ("11-az-powershell-basics", "Az PowerShell Module Basics", "ps1"),
        ],
    ),
    (
        "bicep-arm-json",
        "Bicep, ARM, and JSON",
        [
            ("01-arm-json-anatomy", "ARM JSON Anatomy", "json"),
            ("02-bicep-basics", "Bicep Basics: JSON to Bicep", "bicep"),
            ("03-parameters-and-variables", "Parameters and Variables", "bicep"),
            ("04-outputs", "Outputs", "bicep"),
            ("05-expressions-and-functions", "Expressions and Built-In Functions", "bicep"),
            ("06-conditionals-and-loops", "Conditionals and Loops", "bicep"),
            ("07-modules", "Modules", "bicep"),
            ("08-dependencies", "Dependencies: Implicit vs Explicit", "bicep"),
            ("09-array-loops-multiple-resources", "Array Loops for Multiple Resources", "bicep"),
            ("10-deployment-scopes", "Deployment Scopes", "bicep"),
            ("11-what-if-and-validation", "What-If and Validation Workflow", "bicep"),
            ("12-decompile-arm-to-bicep", "Decompiling ARM to Bicep", "bicep"),
        ],
    ),
    (
        "terraform",
        "Terraform",
        [
            ("01-iac-concepts-and-providers", "IaC Concepts, Providers, Resource Blocks", "tf"),
            ("02-core-workflow", "Core Workflow: Init, Plan, Apply, Destroy", "tf"),
            ("03-variables-and-outputs", "Variables and Outputs", "tf"),
            ("04-state", "State: What It Is and Why It Matters", "tf"),
            ("05-azurerm-provider", "The azurerm Provider", "tf"),
            ("06-resource-dependencies", "Resource Dependencies", "tf"),
            ("07-data-sources", "Data Sources", "tf"),
            ("08-count-and-for-each", "count and for_each", "tf"),
            ("09-modules", "Writing and Calling Modules", "tf"),
            ("10-remote-state-basics", "Remote State Basics (HCP Terraform)", "tf"),
            ("11-lifecycle-blocks", "Lifecycle Blocks", "tf"),
            ("12-plan-output-and-state-commands", "Reading Plan Output and terraform state Commands", "tf"),
        ],
    ),
]

def _stub_lesson(title: str) -> str:
    return f"""# {title}

## Status
Not started

## Lesson
(To be filled in when you start this module.)

## Key Terms
See GLOSSARY.md at the repo root for terms used in this module.
"""

def _stub_problem(title: str) -> str:
    return f"""# Problem: {title}

(Problem to be added when you start this module.)
"""

def _stub_solution(ext: str) -> str:
    comment = "#" if ext in ("ps1", "tf") else "//"
    return f"{comment} Solution - write your work here\n"

def _write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content)
    return True

def scaffold(base: Path):
    """Creates the full repo skeleton: all 3 sections' stub folders, README.md,
    GLOSSARY.md. Never overwrites a file that already exists, so it's safe to
    call even after other sections have already been populated for real."""
    base.mkdir(exist_ok=True)
    _write_if_missing(base / "GLOSSARY.md", GLOSSARY_CONTENT)
    _write_if_missing(base / "ENVIRONMENT-SETUP.md", ENVIRONMENT_SETUP_CONTENT)

    readme_lines = [
        "# IaC Fundamentals Bootcamp",
        "",
        "Hands-on bootcamp covering PowerShell, Bicep/ARM/JSON, and Terraform in one repo.",
        "Each module has a lesson.md, a problem.md, and a solution file. Work modules in any order.",
        "See GLOSSARY.md for terminology.",
        "",
    ]
    for folder, title, modules in SCAFFOLD_SECTIONS:
        section_path = base / folder
        section_path.mkdir(exist_ok=True)
        readme_lines.append(f"# {title}")
        readme_lines.append("")
        for slug, mod_title, ext in modules:
            module_path = section_path / slug
            module_path.mkdir(exist_ok=True)
            _write_if_missing(module_path / "lesson.md", _stub_lesson(mod_title))
            _write_if_missing(module_path / "problem.md", _stub_problem(mod_title))
            _write_if_missing(module_path / f"solution.{ext}", _stub_solution(ext))
            readme_lines.append(f"- [ ] {slug}: {mod_title}")
        readme_lines.append("")
    _write_if_missing(base / "README.md", "\n".join(readme_lines))

# --- Environment setup (written once at repo root, alongside README/GLOSSARY) ---

ENVIRONMENT_SETUP_CONTENT = """# Environment Setup

This assumes nothing is installed yet. Do this once, in order, before starting module 1 of any section. Both Windows and RHEL/Linux are covered in full for every tool, pick whichever machine you're on, both work equally well for everything in this repo.

## If a Microsoft package install has failed on RHEL before
Every Microsoft Linux tool below has a way to install as a single downloaded file, no repository registration step at all. Where that applies, it's called out explicitly, use that path first if the dnf-repo method has given you trouble before.

## PowerShell 7

**Windows (winget):**
```powershell
winget install --id Microsoft.PowerShell --source winget
```
Installs the current PowerShell 7 release side by side with the built-in Windows PowerShell 5.1, both can coexist.

**RHEL / Linux, Option A, single RPM, no repo registration (start here if you've had trouble before):**
```bash
sudo dnf install https://github.com/PowerShell/PowerShell/releases/download/v7.6.5/powershell-7.6.5-1.rh.x86_64.rpm
```
Installs directly from one downloaded package. Does not register Microsoft's repository on your system, nothing for subscription-manager to conflict with.

**RHEL / Linux, Option B, tar.gz binary, no root required:**
```bash
curl -L -o /tmp/powershell.tar.gz https://github.com/PowerShell/PowerShell/releases/download/v7.6.5/powershell-7.6.5-linux-x64.tar.gz
mkdir -p ~/powershell
tar -xzf /tmp/powershell.tar.gz -C ~/powershell
~/powershell/pwsh
```
Unpacks into your own home directory. Nothing system-wide, nothing to register, works without sudo.

**RHEL / Linux, Option C, Microsoft's package repository (registers a new repo, most likely to hit prior friction):**
```bash
source /etc/os-release
curl -sSL -O https://packages.microsoft.com/config/rhel/$VERSION_ID/packages-microsoft-prod.rpm
sudo rpm -i packages-microsoft-prod.rpm
sudo dnf install powershell -y
```
Microsoft's documented preferred method, and the one that registers a full repo, the exact step that's caused registration problems before. Use A or B instead if this fails.

**Verify (either OS):** `pwsh --version`

## Azure CLI
Needed for PowerShell module 11, and for every deployment in the Bicep/ARM/JSON section.

**Windows (winget):**
```powershell
winget install --exact --id Microsoft.AzureCLI
```

**Windows (MSI, alternative):**
Download and run the installer from `https://aka.ms/installazurecliwindows`, close and reopen your terminal afterward.

**RHEL / Linux, Option A, universal install script:**
```bash
curl -L https://aka.ms/InstallAzureCli | bash
```
Detects your distro and installs without you manually configuring a repo.

**RHEL / Linux, Option B, dnf with Microsoft's repo (same registration step as PowerShell Option C above):**
```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install -y https://packages.microsoft.com/config/rhel/$(source /etc/os-release; echo $VERSION_ID)/packages-microsoft-prod.rpm
sudo dnf install azure-cli
```

**Either OS, Option C, Azure Cloud Shell, zero install:**
portal.azure.com has a Cloud Shell icon in the top bar, a browser-based terminal with Azure CLI, Bicep, and PowerShell already installed. Nothing local to configure, a good fallback while sorting out a local install.

**Verify (either OS):** `az --version`
**Sign in (either OS):** `az login`

## Bicep CLI
Usually nothing to install separately on either OS. Azure CLI 2.20.0+ installs its own self-contained Bicep CLI automatically the first time you run a command that needs it.
```bash
az bicep version
```
If it's missing:
```bash
az bicep install
```

**Windows (winget), standalone install:**
```powershell
winget install --exact --id Microsoft.Bicep
```

**RHEL / Linux, standalone binary:**
```bash
curl -Lo bicep https://github.com/Azure/bicep/releases/latest/download/bicep-linux-x64
chmod +x ./bicep
sudo mv ./bicep /usr/local/bin/bicep
bicep --help
```
A standalone install is only needed if you're using Bicep from somewhere that doesn't already carry Azure CLI's copy, like a from a script that calls `bicep` directly instead of `az bicep`.

## Terraform

**Windows (winget):**
```powershell
winget install --id Hashicorp.Terraform --exact
```

**RHEL / Linux, HashiCorp's own repository (separate from Microsoft's, hasn't been a source of the friction you've hit before):**
```bash
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo dnf install terraform
```

**Verify (either OS):** `terraform version`

## VS Code extensions
Same three extensions, same names, on both machines. Install from the Extensions panel (Ctrl+Shift+X), search each by name:
- **PowerShell** (by Microsoft), syntax highlighting, IntelliSense, run .ps1 files directly from the editor.
- **Bicep** (by Microsoft), syntax highlighting, autocomplete, inline validation for .bicep files.
- **HashiCorp Terraform** (by HashiCorp), syntax highlighting and autocomplete for .tf files.

## Quick sanity check
Run on whichever machine you're currently on:
```bash
pwsh --version
az --version
az bicep version
terraform version
```
All four returning a version number with no errors means that machine is ready for module 1 of any section. Run the same check on the other machine whenever you switch to it, don't assume both stay in sync automatically.

## Reference
- https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows
- https://learn.microsoft.com/en-us/powershell/scripting/install/install-rhel
- https://learn.microsoft.com/en-us/powershell/scripting/install/alternate-install-methods
- https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows
- https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/install
- https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
"""


# --- Interactive lesson transformation ---
# Applied to every lesson.md at write time. Finds each fenced code block and
# inserts a hands-on checkpoint right after it, so the lesson itself is
# practiced as you read it, not just read and then practiced later in the
# problem. Doesn't require touching the 35 lesson strings by hand, it's a
# consistent transformation applied uniformly across every module.

import re as _re

_CHECKPOINT_TEMPLATES = {
    "powershell": "Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.",
    "json": "Type the code above into a scratch file (try.json) yourself rather than copy-pasting it. Read back through it and confirm you can name what each part is doing before moving on.",
    "bicep": "Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.",
    "hcl": "Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.",
    "bash": "Run the command above yourself in your terminal before reading on, don't just read what it's supposed to do.",
}
_DEFAULT_CHECKPOINT = "Type the code above yourself and try running or reasoning through it before reading on."

_CODE_BLOCK_PATTERN = _re.compile(r'(```([a-zA-Z]*)\n.*?```)', _re.DOTALL)

def make_interactive(lesson_text: str) -> str:
    counter = {"n": 0}

    def _replacer(match: "_re.Match") -> str:
        counter["n"] += 1
        block = match.group(1)
        lang = match.group(2).lower()
        instruction = _CHECKPOINT_TEMPLATES.get(lang, _DEFAULT_CHECKPOINT)
        checkpoint = f"\n\n> **Try it now, Checkpoint {counter['n']}**\n> {instruction}\n"
        return block + checkpoint

    result = _CODE_BLOCK_PATTERN.sub(_replacer, lesson_text)

    intro_note = (
        "## Lesson\n\n"
        "*This lesson is interactive. Complete each numbered checkpoint as you reach it, "
        "don't read past it and come back later, the point is building the muscle memory "
        "while the concept is still right in front of you.*\n"
    )
    result = result.replace("## Lesson\n", intro_note, 1)

    return result

def write_module(section_path: Path, slug: str, content: dict):
    module_path = section_path / slug
    module_path.mkdir(parents=True, exist_ok=True)
    (module_path / "lesson.md").write_text(make_interactive(content["lesson"]))
    (module_path / "problem.md").write_text(content["problem"])

def build():
    base = Path(REPO_NAME)
    scaffold(base)  # creates the full repo skeleton if it doesn't exist yet
    section_path = base / SECTION
    section_path.mkdir(parents=True, exist_ok=True)
    for slug, content in MODULES.items():
        write_module(section_path, slug, content)
    print(f"Populated {len(MODULES)} modules in {SECTION}/ (full repo skeleton ensured)")

if __name__ == "__main__":
    build()