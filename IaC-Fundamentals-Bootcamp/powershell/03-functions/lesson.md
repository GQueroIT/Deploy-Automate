# Functions: Params, Return Values, Scope

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
