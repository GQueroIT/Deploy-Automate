# Az PowerShell Module Basics

## Status
In progress

## Lesson

### Az, not AzureRM
The Az module is the current, actively maintained PowerShell module for managing Azure resources. There's an older module called AzureRM that's now legacy, Microsoft's own guidance is that Az and AzureRM should not be installed side by side on the same system, they define overlapping cmdlets and will conflict. If you're setting this up fresh, you only want Az.

```powershell
Install-Module -Name Az -Repository PSGallery -Force
```

Keep it current later with Update-Module -Name Az -Force.

### Connecting to Azure
Connect-AzAccount opens a browser window for interactive sign-in (with MFA support). You have to do this again every time you start a new PowerShell session, the connection doesn't persist automatically across sessions unless you specifically set that up.

```powershell
Connect-AzAccount
```

### Checking and setting context
Once connected, if your account has access to more than one subscription, PowerShell picks one as the "current context" and every command runs against that subscription until you change it. Always verify before running anything that creates or modifies resources:

```powershell
Get-AzContext                      # what subscription am I currently pointed at?
Get-AzContext -ListAvailable       # what subscriptions do I have access to?
Set-AzContext -Subscription "name-or-id"   # switch to a specific one
```

Running a command against the wrong subscription because nobody checked context first is a genuinely common real-world mistake, get in the habit of checking it early in any script that touches Azure.

## Key Terms
See GLOSSARY.md. New here: Authentication (proving who you are to Azure before it lets you do anything), Context (which subscription/tenant your current session is currently pointed at).

## Reference
- https://learn.microsoft.com/en-us/powershell/azure/install-azps-windows
- https://learn.microsoft.com/en-us/powershell/module/az.accounts/connect-azaccount
