# Variables, Data Types, and Output

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### What a variable actually is
A PowerShell variable is a named storage location for a value. Every variable name starts with a dollar sign: $name, $serverCount, $isOnline. You don't declare a type ahead of time like you would in a statically typed language. A variable comes into existence the moment you assign it a value, and PowerShell figures out the type on its own based on whatever you put in it.

```powershell
$firstName = "Gabe"
$ticketCount = 12
$isResolved = $false
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


That's it. No int ticketCount = 12;, no upfront declaration. This is called being dynamically typed, and it's one of the first things that trips people up coming from a language that forces you to declare types.

### Putting a variable inside a bigger string
You'll need this for the problem below, so it's worth covering now instead of waiting. Double-quoted strings don't just hold variables, they can have a variable's value dropped directly inside them. This is called string interpolation:

```powershell
$firstName = "Gabe"
"Hello, $firstName"    # outputs: Hello, Gabe
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


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

> **Try it now, Checkpoint 3**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


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
