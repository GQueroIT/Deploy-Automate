# Script Structure: Params Blocks, Comment-Based Help

By the end of this module, you'll be able to turn a script into a properly documented, parameter-driven tool that Get-Help can read.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### Script-level param blocks
Just like a function can accept parameters, a whole .ps1 script file can too. The param() block has to be the very first real statement in the file, before anything else runs (comments above it are fine):

```powershell
param(
    [string]$DriveLetter = "C",
    [int]$WarningThresholdPercent = 90
)
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


Now the script itself can be called with arguments: .\Check-Disk.ps1 -DriveLetter D -WarningThresholdPercent 85.

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
    .\Check-Disk.ps1 -DriveLetter D -WarningThresholdPercent 85
#>
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


This block needs to sit as the very first thing in the file (above even the param block, or immediately below it, both work, just be consistent) for Get-Help .\Check-Disk.ps1 -Full to actually find and display it.

### [CmdletBinding()]
Adding [CmdletBinding()] right above your param() block makes your script (or function) behave more like a real built-in cmdlet, it automatically gains support for common parameters like -Verbose and -ErrorAction without you having to build that yourself.

```powershell
[CmdletBinding()]
param(
    [string]$DriveLetter = "C"
)
```

> **Try it now, Checkpoint 3**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


## Commands Used in This Lesson

- `Get-Help` — Displays help and documentation for a cmdlet, function, or script. Example: `Get-Help .\script.ps1 -Full`

## Troubleshooting

- Get-Help .\script.ps1 -Full shows nothing useful. The comment-based help block has to be a single contiguous block with the exact .SYNOPSIS/.DESCRIPTION formatting, sitting right above or below the param block.
- The script errors immediately with 'param is not recognized'. Something came before param() in the file, it has to be the very first real statement.

## Key Terms
See GLOSSARY.md. New here: CmdletBinding (an attribute that upgrades a function/script to behave like a real cmdlet), Comment-based help (a structured comment block that PowerShell's help system can read).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_comment_based_help
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_cmdletbindingattribute
