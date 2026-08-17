# Arrays and Hashtables

By the end of this module, you'll be able to choose between an array and a hashtable for a given problem, and look values up by index or by key.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### Arrays
An array is an ordered collection of values, indexed starting at 0. Build one with @():

```powershell
$servers = @("SERVER01", "SERVER02", "SERVER03")
$servers[0]        # SERVER01
$servers.Count      # 3
$servers += "SERVER04"   # adds a new item
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


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

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


Use bracket notation ($hash[$variableName]) when the key itself is stored in a variable, dot notation only works with a literal key name typed directly.

### When to use which
Reach for an array when order matters and you just need a list. Reach for a hashtable when you need to look something up by a name or key rather than by position, exactly like the printer example above, you don't want to remember "IT is index 2", you want to ask for "IT" directly.

## Troubleshooting

- $hash['Key'] returns nothing but the key definitely exists. Hashtable keys are case-sensitive by default, double check the exact casing you used.
- Adding to an array with += inside a loop feels slow. That's real, += rebuilds the whole array each time, fine for exercises this size, but worth knowing why it doesn't scale.

## Key Terms
See GLOSSARY.md. New here: Array, Hashtable, Index, Key-value pair.

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_arrays
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_hash_tables
