# Problem: Az PowerShell Module Basics

## Scenario
You're about to start managing Azure resources from PowerShell instead of the portal, and before you write anything that actually changes something, you want a safe, read-only script that confirms exactly what subscription you're pointed at and what already exists there.

## Your task
In solution.ps1:

1. Connect to Azure with Connect-AzAccount (only actually run this if you have an Azure account handy, otherwise write the script as if you would).
2. Retrieve and display the current context with Get-AzContext, specifically call out the subscription name in your output.
3. List every resource group in the current subscription using Get-AzResourceGroup.
4. Display the results as a formatted table showing just the resource group name and location, using Format-Table.
5. Bonus: wrap the whole thing so that if Get-AzContext comes back empty (meaning you're not connected), it prints a clear message telling you to run Connect-AzAccount first, instead of just erroring out further down the script.

## Hints
- Hint 1: Get-AzResourceGroup returns full objects with a lot of properties, Format-Table -Property ResourceGroupName, Location narrows it to just what you want to see.
- Hint 2: Get-AzContext returns $null (or an empty result) if you're not connected yet, that's exactly what you can check for in the bonus.
- Hint 3: Connecting is a one-time-per-session thing, if you're testing this script repeatedly in the same PowerShell window, you don't need to reconnect every single run.
