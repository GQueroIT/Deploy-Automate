# Az PowerShell Module Basics

By the end of this module, you'll be able to connect to Azure from PowerShell, confirm which subscription you're pointed at, and pull back a clean list of what's actually there.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

### Az, not AzureRM
The Az module is the current, actively maintained PowerShell module for managing Azure resources. There's an older module called AzureRM that's now legacy, Microsoft's own guidance is that Az and AzureRM should not be installed side by side on the same system, they define overlapping cmdlets and will conflict. If you're setting this up fresh, you only want Az.

```powershell
Install-Module -Name Az -Repository PSGallery -Force
```

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


Keep it current later with Update-Module -Name Az -Force.

### Connecting to Azure
Connect-AzAccount opens a browser window for interactive sign-in (with MFA support). You have to do this again every time you start a new PowerShell session, the connection doesn't persist automatically across sessions unless you specifically set that up.

```powershell
Connect-AzAccount
```

> **Try it now, Checkpoint 2**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


### Checking and setting context
Once connected, if your account has access to more than one subscription, PowerShell picks one as the "current context" and every command runs against that subscription until you change it. Always verify before running anything that creates or modifies resources:

```powershell
Get-AzContext                      # what subscription am I currently pointed at?
Get-AzContext -ListAvailable       # what subscriptions do I have access to?
Set-AzContext -Subscription "name-or-id"   # switch to a specific one
```

> **Try it now, Checkpoint 3**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


Running a command against the wrong subscription because nobody checked context first is a genuinely common real-world mistake, get in the habit of checking it early in any script that touches Azure.

### Listing resources and formatting the output
Once connected, Az cmdlets follow the same Verb-Noun pattern as everything else, and the same pipeline concepts from earlier modules apply directly:

```powershell
Get-AzResourceGroup
```

> **Try it now, Checkpoint 4**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


This returns one object per resource group in your current subscription, with properties like ResourceGroupName and Location, exactly like any other PowerShell object. To display just specific properties as a clean table instead of the full default output, pipe it into Format-Table:

```powershell
Get-AzResourceGroup | Format-Table -Property ResourceGroupName, Location
```

> **Try it now, Checkpoint 5**
> Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.


Format-Table doesn't change the underlying objects, it only changes how they're displayed on screen. If you tried to capture this into a variable and use it further down a pipeline, you'd get formatted display text back, not usable objects, which is why formatting cmdlets like this one are usually the last thing in a pipeline, not the middle.

## Commands Used in This Lesson

- `Install-Module` — Installs a PowerShell module from a repository like the PowerShell Gallery. Example: `Install-Module -Name Az -Repository PSGallery -Force`
- `Update-Module` — Updates an already-installed module to the latest version. Example: `Update-Module -Name Az -Force`
- `Connect-AzAccount` — Signs in to Azure interactively from PowerShell. Example: `Connect-AzAccount`
- `Get-AzContext` — Shows which Azure subscription and tenant the current session is pointed at. Example: `Get-AzContext`
- `Set-AzContext` — Switches the current session to a specific subscription. Example: `Set-AzContext -Subscription "name-or-id"`
- `Get-AzResourceGroup` — Lists resource groups in the current subscription. Example: `Get-AzResourceGroup`
- `Format-Table` — Displays objects as a table, showing only the properties you choose. Example: `... | Format-Table -Property Name, Location`

## Troubleshooting

- Get-AzResourceGroup returns 'Run Connect-AzAccount to login'. The session isn't authenticated yet, or it expired, reconnect.
- Commands run successfully but against the wrong subscription. Always check Get-AzContext before running anything, especially if your account has access to more than one subscription.

## Key Terms
See GLOSSARY.md. New here: Authentication (proving who you are to Azure before it lets you do anything), Context (which subscription/tenant your current session is currently pointed at).

## Reference
- https://learn.microsoft.com/en-us/powershell/azure/install-azps-windows
- https://learn.microsoft.com/en-us/powershell/module/az.accounts/connect-azaccount

## See Also

- [Terraform module 05, The azurerm Provider](../../terraform/05-azurerm-provider/lesson.md)
