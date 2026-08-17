# Error Handling: Try/Catch/Finally

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

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

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


finally is optional, use it for cleanup that has to happen either way, closing a connection, deleting a temp file.

### Terminating vs non-terminating errors
This is the part that actually trips people up: try/catch only catches terminating errors. A lot of built-in cmdlets produce non-terminating errors by default, meaning they print an error message and keep going, without ever triggering your catch block. To force a cmdlet to treat its own error as terminating (so catch can actually see it), add -ErrorAction Stop to that specific command:

```powershell
try {
    Get-Item -Path "C:\DoesNotExist" -ErrorAction Stop
} catch {
    Write-Host "Failed: $($_.Exception.Message)"
}
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


Without -ErrorAction Stop on that Get-Item call, the catch block would silently never run, even though the command clearly failed.

### Reading the error inside catch
Inside a catch block, $_ refers to the error record itself. $_.Exception.Message gives you the human-readable reason it failed, which is what you want to log or display instead of dumping a full stack trace on someone.

### throw
You can raise your own error deliberately with throw "some message", useful inside a function when a condition means it genuinely can't continue.

## Commands Used in This Lesson

- `Write-Host` — Prints text to the console for a human to read. Not sent down the pipeline. Example: `Write-Host "text"`
- `Get-Item` — Gets an item at a given path, like a file. Used with -ErrorAction Stop to make it catchable. Example: `Get-Item -Path $path -ErrorAction Stop`

## Key Terms
See GLOSSARY.md. New here: Exception (the object PowerShell creates describing what went wrong), Terminating error (stops execution immediately, catchable), Non-terminating error (reported but execution continues, not caught by try/catch unless forced with -ErrorAction Stop).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_try_catch_finally
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_throw
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_automatic_variables
