# General IaC Concepts

**Infrastructure as Code (IaC)** - writing your servers, networks, and cloud resources as text files instead of clicking through a portal, so the setup can be saved, reused, and tracked like any other code.

**Declarative** - you describe what the end result should look like, and the tool figures out how to get there. This is how Bicep, ARM, and Terraform work.

**Imperative** - you write out every step in order to make something happen. This is how a PowerShell script works.

**State** - a record of what infrastructure already exists right now, so the tool knows what to change instead of rebuilding everything from scratch every time.

**Idempotent** - running the same thing twice gives you the same result the second time as the first. No duplicate resources, no surprise side effects.

**Provider** - the plugin that lets a tool talk to a specific platform. Terraform's azurerm provider is how Terraform talks to Azure.

**Resource** - a single thing being created or managed: a VM, a storage account, a virtual network.

**Module** - a reusable, packaged chunk of code you call instead of rewriting the same block over and over.

**Deployment** - the actual act of running your code against the cloud and creating or changing real resources.

# PowerShell

**Cmdlet** - pronounced "command-let." A built-in PowerShell command, always named Verb-Noun, like Get-Process or New-Item.

**Pipeline** - the | symbol. Takes the output of one cmdlet and feeds it straight into the next one as input.

**Object** - everything that comes out of a cmdlet in PowerShell is a structured object with properties, not plain text. That's what makes Get-Member and Where-Object work.

**Parameter** - a named input you pass into a cmdlet or function, like -Name or -Path.

**Variable** - a named container holding a value, always starts with $, like $name.

**Script** - a saved .ps1 file containing a sequence of PowerShell commands.

**Function** - a named, reusable block of code inside a script that you call with parameters.

# JSON and ARM

**JSON (JavaScript Object Notation)** - a plain text format for storing structured data as key-value pairs. ARM templates are written in this format.

**ARM template** - a JSON file describing the Azure resources you want deployed. Azure Resource Manager reads it and builds them.

**Resource provider** - the Azure service responsible for a resource type, written like Microsoft.Compute or Microsoft.Storage.

**API version** - a dated version string, like 2023-09-01, that tells Azure which version of a resource's schema you're using.

**Schema** - the shape a JSON file is supposed to follow: which fields are required, what type each value should be.

# Bicep

**Bicep** - a simpler language that compiles down into ARM JSON. You write Bicep, Azure still deploys ARM JSON underneath it.

**Decorator** - a tag starting with @ placed above a parameter to add a rule, like @allowed([...]) or @secure().

**Scope** - where a deployment targets: resource group, subscription, or management group.

**Interpolation** - dropping a variable's value directly inside a string using ${} syntax.

**Compile** - turning a .bicep file into the ARM JSON that actually gets deployed (az bicep build).

**Decompile** - the reverse: turning an existing ARM JSON template back into Bicep (az bicep decompile).

# Terraform

**HCL (HashiCorp Configuration Language)** - the language Terraform files are written in, ending in .tf.

**Resource block** - the chunk of HCL defining one piece of infrastructure to create.

**State file** - a JSON file Terraform keeps (terraform.tfstate) tracking what it has already built, so it knows what's real versus what's just in your code.

**Plan** - a preview of what Terraform would change, generated with terraform plan, before anything actually happens.

**Apply** - the command that takes the plan and actually creates or changes the real resources.

**Data source** - a way to pull in information about something that already exists, without Terraform managing or creating it.

**count / for_each** - meta-arguments that let one resource block create multiple copies of itself from a number or a list.
