# Problem: The Pipeline: Where-Object, Sort-Object, Select-Object

## Scenario
A machine is running slow and you want a quick way to see what's actually eating memory, without scrolling through every single running process.

## Your task
In solution.ps1, write a single pipeline (you can run this against your own real machine) that:

1. Starts with Get-Process.
2. Filters down to only processes using more than some memory threshold you choose (start with something reasonable like 50MB so you actually get results).
3. Sorts the remaining processes by WorkingSet, highest first.
4. Selects only the Name and WorkingSet properties.
5. Limits the output to the top 5 results.
6. Print or display the final result.

## Hints
- Hint 1: WorkingSet is the property name for memory usage on a process object, confirm this yourself by running Get-Process | Get-Member and looking for it in the property list, rather than trusting it blind.
- Hint 2: The order of the pipeline matters for performance, filter first with Where-Object before sorting, so you're not sorting a huge list you're about to throw most of away anyway.
- Hint 3: -First belongs to Select-Object, not Sort-Object, don't try to limit the count in the wrong cmdlet.
