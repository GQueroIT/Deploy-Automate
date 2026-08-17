# Problem: Control Flow: If/Else, Switch, Loops

## Scenario
Your team monitors ten servers. You've got a list of server names, each with a status of "Up", "Down", or "Degraded", and you want a script that loops through the list and calls out anything that needs attention.

## Your task
In solution.ps1:

1. Build an array of at least five objects, each with a Name and a Status property (Up, Down, or Degraded). You can build these with [PSCustomObject]@{ Name = "SERVER01"; Status = "Up" } repeated for each server.
2. Use a foreach loop to step through the array.
3. Inside the loop, use if/elseif/else to print a different message depending on status: something urgent for Down, a warning for Degraded, and a quiet confirmation for Up.
4. Rewrite the same logic a second way using a switch statement on $server.Status instead of if/elseif/else, inside the same loop or a second loop, whichever is cleaner to you.
5. Bonus: count how many servers were Down total, and print that count after the loop finishes.

## Hints
- Hint 1: foreach ($server in $servers) gives you one object per pass, access its properties with $server.Name and $server.Status.
- Hint 2: Remember, comparisons use -eq, not ==. $server.Status -eq "Down" is correct, $server.Status == "Down" will error.
- Hint 3: For the running count, declare a variable before the loop starts (like $downCount = 0) and increment it inside the if block for Down servers, incrementing inside the loop is what makes it a running total instead of resetting every pass.
