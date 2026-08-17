# Error Handling: Try/Catch/Finally

## Status
In progress

## Lesson

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

Without -ErrorAction Stop on that Get-Item call, the catch block would silently never run, even though the command clearly failed.

### Reading the error inside catch
Inside a catch block, $_ refers to the error record itself. $_.Exception.Message gives you the human-readable reason it failed, which is what you want to log or display instead of dumping a full stack trace on someone.

### throw
You can raise your own error deliberately with throw "some message", useful inside a function when a condition means it genuinely can't continue.

## Key Terms
See GLOSSARY.md. New here: Exception (the object PowerShell creates describing what went wrong), Terminating error (stops execution immediately, catchable), Non-terminating error (reported but execution continues, not caught by try/catch unless forced with -ErrorAction Stop).

## Reference
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_try_catch_finally
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_throw
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_automatic_variables
