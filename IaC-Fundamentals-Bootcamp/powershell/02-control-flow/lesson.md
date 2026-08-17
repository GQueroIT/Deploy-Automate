# Control Flow: If/Else, Switch, Loops

By the end of this module, you'll be able to branch logic with if/elseif/else or switch, and loop over a list of items with foreach.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

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

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


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

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


### switch
When you've got more than two or three elseif branches checking the same variable, switch is cleaner:

```powershell
switch ($status) {
    "Down"     { Write-Host "Down" }
    "Degraded" { Write-Host "Degraded" }
    default    { Write-Host "OK" }
}
```

> **Try it now, Checkpoint 3**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


switch can also match wildcards (-Wildcard) or regular expressions (-Regex), and it can evaluate directly against an array, running once per matching item.

### Loops
- foreach ($item in $collection) { } steps through each item in an array one at a time. This is the loop you'll use most.
- for ($i = 0; $i -lt 10; $i++) { } is a counted loop, useful when you specifically need the index number.
- while (condition) { } runs as long as the condition stays true, checked before each pass.
- do { } while (condition) / do { } until (condition) runs the body at least once before checking the condition.

break exits a loop immediately. continue skips to the next iteration.

## Commands Used in This Lesson

- `Write-Host` — Prints text to the console for a human to read. Not sent down the pipeline. Example: `Write-Host "text"`

## Troubleshooting

- if ($status == "Down") throws an error. PowerShell doesn't use ==, use -eq instead.
- A switch statement runs every matching block, not just the first one. If you expected 'first match wins' like some other languages, that's not how PowerShell's switch behaves by default.

## Key Terms
See GLOSSARY.md. New here: Boolean, Operator, Loop, Iteration. A Boolean is a value that's only ever true or false, like $isResolved from module 1. An Operator is a symbol or keyword (like -eq) that compares or combines values. A Loop repeats a block of code. Each single pass through a loop is one Iteration.

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_comparison_operators
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_if
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_switch
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_foreach
