# Arrays and Hashtables

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
