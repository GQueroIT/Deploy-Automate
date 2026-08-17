# Environment Setup

This assumes nothing is installed yet. Do this once, in order, before starting module 1 of any section. Both Windows and RHEL/Linux are covered in full for every tool, pick whichever machine you're on, both work equally well for everything in this repo.

## If a Microsoft package install has failed on RHEL before
Every Microsoft Linux tool below has a way to install as a single downloaded file, no repository registration step at all. Where that applies, it's called out explicitly, use that path first if the dnf-repo method has given you trouble before.

## PowerShell 7

**Windows (winget):**
```powershell
winget install --id Microsoft.PowerShell --source winget
```
Installs the current PowerShell 7 release side by side with the built-in Windows PowerShell 5.1, both can coexist.

**RHEL / Linux, Option A, single RPM, no repo registration (start here if you've had trouble before):**
```bash
sudo dnf install https://github.com/PowerShell/PowerShell/releases/download/v7.6.5/powershell-7.6.5-1.rh.x86_64.rpm
```
Installs directly from one downloaded package. Does not register Microsoft's repository on your system, nothing for subscription-manager to conflict with.

**RHEL / Linux, Option B, tar.gz binary, no root required:**
```bash
curl -L -o /tmp/powershell.tar.gz https://github.com/PowerShell/PowerShell/releases/download/v7.6.5/powershell-7.6.5-linux-x64.tar.gz
mkdir -p ~/powershell
tar -xzf /tmp/powershell.tar.gz -C ~/powershell
~/powershell/pwsh
```
Unpacks into your own home directory. Nothing system-wide, nothing to register, works without sudo.

**RHEL / Linux, Option C, Microsoft's package repository (registers a new repo, most likely to hit prior friction):**
```bash
source /etc/os-release
curl -sSL -O https://packages.microsoft.com/config/rhel/$VERSION_ID/packages-microsoft-prod.rpm
sudo rpm -i packages-microsoft-prod.rpm
sudo dnf install powershell -y
```
Microsoft's documented preferred method, and the one that registers a full repo, the exact step that's caused registration problems before. Use A or B instead if this fails.

**Verify (either OS):** `pwsh --version`

## Azure CLI
Needed for PowerShell module 11, and for every deployment in the Bicep/ARM/JSON section.

**Windows (winget):**
```powershell
winget install --exact --id Microsoft.AzureCLI
```

**Windows (MSI, alternative):**
Download and run the installer from `https://aka.ms/installazurecliwindows`, close and reopen your terminal afterward.

**RHEL / Linux, Option A, universal install script:**
```bash
curl -L https://aka.ms/InstallAzureCli | bash
```
Detects your distro and installs without you manually configuring a repo.

**RHEL / Linux, Option B, dnf with Microsoft's repo (same registration step as PowerShell Option C above):**
```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install -y https://packages.microsoft.com/config/rhel/$(source /etc/os-release; echo $VERSION_ID)/packages-microsoft-prod.rpm
sudo dnf install azure-cli
```

**Either OS, Option C, Azure Cloud Shell, zero install:**
portal.azure.com has a Cloud Shell icon in the top bar, a browser-based terminal with Azure CLI, Bicep, and PowerShell already installed. Nothing local to configure, a good fallback while sorting out a local install.

**Verify (either OS):** `az --version`
**Sign in (either OS):** `az login`

## Bicep CLI
Usually nothing to install separately on either OS. Azure CLI 2.20.0+ installs its own self-contained Bicep CLI automatically the first time you run a command that needs it.
```bash
az bicep version
```
If it's missing:
```bash
az bicep install
```

**Windows (winget), standalone install:**
```powershell
winget install --exact --id Microsoft.Bicep
```

**RHEL / Linux, standalone binary:**
```bash
curl -Lo bicep https://github.com/Azure/bicep/releases/latest/download/bicep-linux-x64
chmod +x ./bicep
sudo mv ./bicep /usr/local/bin/bicep
bicep --help
```
A standalone install is only needed if you're using Bicep from somewhere that doesn't already carry Azure CLI's copy, like a from a script that calls `bicep` directly instead of `az bicep`.

## Terraform

**Windows (winget):**
```powershell
winget install --id Hashicorp.Terraform --exact
```

**RHEL / Linux, HashiCorp's own repository (separate from Microsoft's, hasn't been a source of the friction you've hit before):**
```bash
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo dnf install terraform
```

**Verify (either OS):** `terraform version`

## VS Code extensions
Same three extensions, same names, on both machines. Install from the Extensions panel (Ctrl+Shift+X), search each by name:
- **PowerShell** (by Microsoft), syntax highlighting, IntelliSense, run .ps1 files directly from the editor.
- **Bicep** (by Microsoft), syntax highlighting, autocomplete, inline validation for .bicep files.
- **HashiCorp Terraform** (by HashiCorp), syntax highlighting and autocomplete for .tf files.

## Quick sanity check
Run on whichever machine you're currently on:
```bash
pwsh --version
az --version
az bicep version
terraform version
```
All four returning a version number with no errors means that machine is ready for module 1 of any section. Run the same check on the other machine whenever you switch to it, don't assume both stay in sync automatically.

## Reference
- https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows
- https://learn.microsoft.com/en-us/powershell/scripting/install/install-rhel
- https://learn.microsoft.com/en-us/powershell/scripting/install/alternate-install-methods
- https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows
- https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/install
- https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
