# Variables, Data Types, and Output

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
