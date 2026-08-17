# Decompiling ARM to Bicep

## Status
In progress

## Lesson

### The command
az bicep decompile <file.json> converts an existing ARM JSON template into Bicep. Useful when you inherit old ARM templates someone else wrote, or when you export a resource's current live configuration from the Azure portal and want to bring it into Bicep going forward.

```bash
az bicep decompile main.json
```

### Best-effort, not guaranteed
Microsoft is explicit about this: decompiling is a best-effort process, there's no guarantee of a perfect, direct mapping from ARM JSON back to Bicep. You'll typically need to review the output and manually fix warnings or errors it flags. This isn't a bug in the tool, ARM JSON is more flexible and less structured than Bicep, so some patterns don't translate cleanly.

### VS Code's paste-as-Bicep shortcut
Visual Studio Code has a feature that lets you paste raw ARM JSON directly into a .bicep file, and it automatically runs the decompile process for you behind the scenes, no separate CLI command needed for quick one-off conversions.

### Closing the loop on this whole section
Think about what you've actually done across this section of the repo: hand-wrote ARM JSON from scratch (module 1), wrote the equivalent in Bicep and compiled it back to JSON to compare (module 2), and now you're decompiling JSON back into Bicep. You've gone in both directions across the exact same conversion, which is the fastest way to actually understand that Bicep isn't a separate system, it's a syntax layer over the same ARM engine.

## Key Terms
See GLOSSARY.md. New here: Best-effort conversion (a tool does its best to translate automatically, but the output isn't guaranteed correct or complete without review).

## Reference
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile
