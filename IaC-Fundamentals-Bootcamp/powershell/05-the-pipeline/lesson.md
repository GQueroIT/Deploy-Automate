# The Pipeline: Where-Object, Sort-Object, Select-Object

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
