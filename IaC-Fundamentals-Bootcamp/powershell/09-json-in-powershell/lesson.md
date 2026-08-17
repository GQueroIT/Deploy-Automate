# JSON in PowerShell: ConvertTo-Json / ConvertFrom-Json

By the end of this module, you'll be able to convert PowerShell data to and from JSON, and know why -Depth matters.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

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

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


ConvertFrom-Json does the reverse, deserialization, taking a JSON string and turning it back into a usable PowerShell object (a PSCustomObject):

```powershell
$json = Get-Content -Path config.json -Raw
$parsed = $json | ConvertFrom-Json
$parsed.ServerName
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


Notice the -Raw on Get-Content here, this matters. ConvertFrom-Json expects one single string, not an array of line-strings, which is what Get-Content returns by default. Skip -Raw and this will fail or behave unexpectedly.

### The -Depth gotcha
ConvertTo-Json only goes 2 levels deep into nested objects by default. If your data has arrays inside objects inside objects, anything past that default depth gets flattened or truncated, silently, no error. If you're converting anything with real nesting, set -Depth explicitly higher than you think you need:

```powershell
$config | ConvertTo-Json -Depth 10
```

> **Try it now, Checkpoint 3**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


### Why this matters beyond just PowerShell
This is the exact same JSON format you hand-wrote in the bicep-arm-json section of this repo for ARM templates. Same format, different producer and consumer, a config file, an API response, an ARM template, it's all just JSON, and now you can move data between PowerShell and any of it.

## Commands Used in This Lesson

- `Get-Content` — Reads a file's contents, returning an array of lines, or one string with -Raw. Example: `Get-Content -Path file.txt -Raw`
- `ConvertTo-Json` — Converts a PowerShell object into a JSON string. Example: `$data | ConvertTo-Json -Depth 10`
- `ConvertFrom-Json` — Parses a JSON string into a PowerShell object. Example: `$json | ConvertFrom-Json`

## Troubleshooting

- Deeply nested data goes missing after ConvertTo-Json. You hit the default -Depth of 2, set it explicitly higher for anything with real nesting.
- ConvertFrom-Json fails on a file you know is valid JSON. Check whether you used Get-Content without -Raw, it hands over an array of lines instead of one string.

## Key Terms
See GLOSSARY.md. New here: Serialization (converting a value into a storable/transmittable format like JSON), Deserialization (the reverse, turning that format back into a usable value).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertto-json
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertfrom-json

## See Also

- [Bicep/ARM/JSON module 01, ARM JSON Anatomy](../../bicep-arm-json/01-arm-json-anatomy/lesson.md)
