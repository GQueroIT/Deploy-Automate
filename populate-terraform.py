#!/usr/bin/env python3
"""
Populates every module in the terraform/ section of IaC-Fundamentals-Bootcamp
with real lesson and problem content, sourced from developer.hashicorp.com.
Overwrites lesson.md and problem.md in each module folder. Safe to re-run.
"""

from pathlib import Path

REPO_NAME = "IaC-Fundamentals-Bootcamp"
SECTION = "terraform"

MODULES = {}

MODULES["01-iac-concepts-and-providers"] = {
"lesson": """# IaC Concepts, Providers, Resource Blocks

## Status
In progress

## Lesson

### What Terraform actually does
Terraform is an infrastructure as code tool that lets you define cloud and on-prem resources in human-readable configuration files, written in a language called HCL (HashiCorp Configuration Language), ending in .tf. Those files can be versioned, reused, and shared like any other code. The core workflow is three stages: write your configuration, run a plan to preview what would change, then apply it to actually create or modify the real infrastructure.

Terraform itself doesn't natively know anything about Azure, AWS, or any other platform. It only knows how to read HCL and talk to plugins. That's what a provider is for.

### Providers
A provider is a plugin that lets Terraform manage resources on a specific platform through that platform's API. Providers are released and versioned separately from Terraform itself, and each one has its own documentation on the Terraform Registry describing the resources and data sources it supports.

There are two separate pieces of configuration involved:

1. required_providers — lives inside a top-level terraform {} block. This is where you declare which provider(s) your configuration needs, including the registry source address and a version constraint.
2. provider block — a separate block, outside the terraform {} block, where you actually configure that provider. For Azure, this is the azurerm provider.

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}
```

If you don't pin a version constraint, terraform init can install a newer major version of a provider later on, which can silently change behavior. Pinning it protects you from that.

One quirk worth knowing up front: recent versions of the azurerm provider require the features {} block inside provider "azurerm" even when there's nothing inside it. Leaving it out entirely will cause terraform init to error.

### Resource blocks, at a glance
You'll go deep on these in a later module, but the shape is: resource "<provider_type>" "<local_name>" { arguments }. The local name is just how you refer to that resource elsewhere in your own configuration, it isn't the actual name Azure gives the resource.

## Key Terms
See GLOSSARY.md at the repo root. This module leans on: HCL, Provider, Resource block, Declarative, Idempotent.

## Reference
- https://developer.hashicorp.com/terraform/intro
- https://developer.hashicorp.com/terraform/language/providers
- https://developer.hashicorp.com/terraform/language/providers/requirements
- https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
""",
"problem": """# Problem: IaC Concepts, Providers, Resource Blocks

## Scenario
Your team is about to start managing Azure resources with Terraform instead of clicking through the portal. Before writing any actual resources, you need the skeleton of a working configuration that Terraform can initialize.

## Your task
In solution.tf, write a Terraform configuration that:

1. Declares that this configuration requires the azurerm provider from the official HashiCorp registry, pinned to a specific major version range so an unexpected update doesn't silently change behavior later.
2. Configures the azurerm provider block correctly, including whatever recent versions of that provider require even when left empty.
3. Adds a short comment above each block explaining in your own words what it does and why it's there, like you're leaving a note for the next tech who opens this file cold.

Don't run terraform init yet unless you already have Terraform installed and Azure CLI authenticated locally. The goal of this module is the structure, not the execution, that comes in module 2.

## Hints
- Hint 1: The azurerm provider's page on the Terraform Registry shows the exact source string and current major version right in its usage example.
- Hint 2: required_providers lives inside a terraform {} block. The provider block that actually configures azurerm is a separate block, outside that terraform {} block.
- Hint 3: Recent azurerm provider versions will error out on terraform init if a specific block is missing from provider "azurerm", even with nothing inside it.
"""
}

MODULES["02-core-workflow"] = {
"lesson": """# Core Workflow: Init, Plan, Apply, Destroy

## Status
In progress

## Lesson

### The three-step core loop
1. terraform init — prepares your working directory. Downloads the providers declared in required_providers, sets up the local .terraform folder. You have to run this again whenever you change which providers a configuration requires.
2. terraform plan — compares your configuration against current state and the real infrastructure, and shows exactly what would change, create, update, or destroy, without touching anything. This is the safety net, read it before you ever type yes.
3. terraform apply — runs a fresh plan and asks you to confirm before executing it. You can also feed it a saved plan file from terraform plan -out=tfplan, useful in CI so what gets applied is exactly, byte-for-byte, what a human already reviewed.

### terraform destroy
Tears down every resource the current configuration manages, using state to know what's real. Also asks for confirmation first, just like apply. Under the hood, terraform destroy is really just an alias for terraform apply -destroy.

### Two habits worth building now
- terraform fmt — reformats your files to a consistent style automatically.
- terraform validate — checks syntax and internal consistency without needing any provider credentials or touching real infrastructure.

Running both before every plan catches dumb mistakes early and keeps your files readable.

## Key Terms
See GLOSSARY.md. New here: Execution plan (the specific list of create/update/destroy actions Terraform computes by comparing your configuration to current state, generated by plan and executed by apply).

## Reference
- https://developer.hashicorp.com/terraform/intro/core-workflow
- https://developer.hashicorp.com/terraform/cli/run
- https://developer.hashicorp.com/terraform/tutorials/cli/plan
""",
"problem": """# Problem: Core Workflow: Init, Plan, Apply, Destroy

## Scenario
Before touching anything in Azure, you want to run the full Terraform lifecycle once against something completely harmless, so the workflow itself is second nature before real stakes are involved.

## Your task
1. Starting from the module 1 solution.tf skeleton, add the hashicorp/local provider alongside azurerm in required_providers.
2. Add a single local_file resource that writes a short text file somewhere harmless on disk, no Azure resources, no cost, nothing that touches the cloud.
3. Run, in order: terraform fmt, terraform validate, terraform init, terraform plan, terraform apply (confirm with yes), and finally terraform destroy (confirm with yes).
4. At each step, note in a comment what you observed, what plan told you would happen before apply actually did it.

## Hints
- Hint 1: local_file lives in a completely separate provider (hashicorp/local) from azurerm, it needs its own entry in required_providers alongside the one from module 1.
- Hint 2: terraform init has to be re-run any time you add a new provider to required_providers, even if you already ran it once before for azurerm alone.
- Hint 3: Watch the plan output closely before typing yes on apply, confirm it says exactly 1 to add and nothing else, that habit is the entire point of this exercise.
"""
}

MODULES["03-variables-and-outputs"] = {
"lesson": """# Variables and Outputs

## Status
In progress

## Lesson

### Input variables
A variable block defines a named input your configuration accepts, keeping values out of hardcoded resource blocks so the same configuration can be reused with different inputs.

```hcl
variable "resource_group_name" {
  type        = string
  description = "Name of the resource group to create"

  validation {
    condition     = can(regex("^rg-", var.resource_group_name))
    error_message = "Resource group name must start with 'rg-'."
  }
}
```

Reference it elsewhere in your configuration with var.resource_group_name. The validation block enforces a rule at plan time, using a condition expression (often built with the can() function wrapping something that would otherwise error, like a regex match) and a custom error_message shown when it fails.

### Output values
An output block exposes a value after apply finishes, for you to see in the CLI, for another configuration to consume via remote state (covered later), or for automation to capture.

```hcl
output "storage_account_name" {
  description = "Name of the created storage account"
  value       = azurerm_storage_account.example.name
}
```

Add sensitive = true to an output (or a variable) to keep its value out of normal CLI output, similar in spirit to Bicep's @secure() decorator from the other section of this repo.

### .tfvars files
Rather than hardcoding variable values or typing them at every plan/apply, you can supply them from a separate file:

```
terraform plan -var-file="dev.tfvars"
```

This is the standard way to keep per-environment values (dev.tfvars, prod.tfvars) out of your core .tf files entirely.

## Key Terms
See GLOSSARY.md. New here: Input value (a variable's role, accepting data into a configuration), Output value (a value exposed after apply), Validation rule (a condition a variable's value must satisfy before Terraform will proceed).

## Reference
- https://developer.hashicorp.com/terraform/language/values
- https://developer.hashicorp.com/terraform/tutorials/configuration-language/variables
""",
"problem": """# Problem: Variables and Outputs

## Scenario
You want your resource group name enforced to follow a naming convention automatically, rather than trusting everyone on the team to remember it by hand, and you want the storage account name available as an output once it's created.

## Your task
In solution.tf:

1. Declare a variable resource_group_name (string), with a validation block requiring it start with "rg-", and a clear error_message if it doesn't.
2. Declare a variable location (string) with a sensible default so it's optional.
3. Add an output storage_account_name that returns the name of a storage account resource (reuse or reference the resource from module 2's structure, or add a placeholder azurerm_storage_account resource here).
4. Create a dev.tfvars file supplying a valid value for resource_group_name (starting with "rg-").
5. Note the exact command you'd run to plan using that tfvars file instead of relying on a default or manual input.

## Hints
- Hint 1: The validation condition pattern condition = can(regex("^rg-", var.resource_group_name)) is a common, reliable way to check a string prefix, can() catches the error a failed regex would otherwise throw and turns it into a clean true/false.
- Hint 2: terraform plan -var-file="dev.tfvars" is the flag, the filename doesn't have to be terraform.tfvars (which loads automatically), naming it dev.tfvars means you have to point at it explicitly.
- Hint 3: An output's value can reference any resource attribute in your configuration, azurerm_storage_account.example.name, exactly like referencing it anywhere else.
"""
}

MODULES["04-state"] = {
"lesson": """# State: What It Is and Why It Matters

## Status
In progress

## Lesson

### The core purpose
Terraform state's primary job is storing the binding between a resource block in your configuration and the actual real-world object it corresponds to. When Terraform creates something, it records that object's identity against the specific resource instance in your code, so it knows what to update or destroy later when your configuration changes.

### Where it lives, by default
Local state is stored as a JSON file named terraform.tfstate in your working directory, with a backup of the previous version kept as terraform.tfstate.backup. This works fine solo, but it's exactly the setup that breaks down with a team (covered in module 10).

### Refresh, before every operation
Before any plan or apply, Terraform refreshes its understanding of state against the real infrastructure, checking for drift, changes made outside Terraform that state doesn't yet know about.

### Never hand-edit the file
Even though it's just JSON, you don't open terraform.tfstate and edit it directly. Terraform provides terraform state subcommands (list, show, mv, rm, and others) specifically so you never have to. Every state-modifying subcommand writes a local backup first, because state is that sensitive to corruption, one bad edit and Terraform can lose track of what it's actually managing.

### The security angle
State can contain sensitive values, passwords, keys, connection strings, in plain text. A local state file sitting on someone's laptop, or worse, committed to a public git repo, is a real, common way secrets leak. This is the exact problem remote state (module 10) exists to solve.

## Key Terms
See GLOSSARY.md. New here: Drift (a difference between what your configuration says should exist and what's actually there, usually caused by manual changes made outside Terraform), State file (the JSON record Terraform keeps of what it's managing).

## Reference
- https://developer.hashicorp.com/terraform/language/state
- https://developer.hashicorp.com/terraform/cli/commands/state
""",
"problem": """# Problem: State: What It Is and Why It Matters

## Scenario
You want to actually see state working, not just read about it, using the harmless local_file resource you already applied back in module 2.

## Your task
1. If you already ran terraform destroy at the end of module 2, run terraform apply again first so you have a real, current state file to work with.
2. Open terraform.tfstate in a text editor, read-only, do not edit it, and find the section describing your local_file resource. Note what information Terraform actually recorded about it.
3. Now do the same thing the correct way: run terraform state list to get the exact resource address, then terraform state show <that address> to see the same information through the proper command.
4. Compare what you found by reading the raw file against what the state command showed you, same information, safer way to get it.

## Hints
- Hint 1: terraform state list gives you the exact address string (like local_file.example) you need to pass into terraform state show, don't guess at the format.
- Hint 2: Resist the urge to actually change anything in the raw JSON file, even to test something, that's exactly the habit this module is trying to prevent, use the state subcommands instead.
- Hint 3: If your local_file resource isn't showing up in state at all, confirm you actually ran apply (not just plan) after re-creating it in step 1.
"""
}

MODULES["05-azurerm-provider"] = {
"lesson": """# The azurerm Provider

## Status
In progress

## Lesson

### What it is
azurerm is HashiCorp's officially maintained provider for Azure, published on the Terraform Registry under the hashicorp/azurerm namespace. It's what actually translates your resource "azurerm_..." blocks into real Azure API calls.

### Authentication
Several authentication methods exist: interactive Azure CLI login, a service principal, or a managed identity. For local practice and learning, the simplest path is having the Azure CLI installed and running az login before you run terraform init, plan, or apply, the azurerm provider can pick up that existing CLI session automatically without you configuring credentials separately inside your Terraform files.

### Naming convention
Almost every resource type in this provider is prefixed azurerm_, for example azurerm_resource_group, azurerm_storage_account, azurerm_virtual_network. If you're not sure a resource type exists, that prefix is the first thing to check for on the Registry.

### The features {} block, again
Covered briefly in module 1: recent versions of the azurerm provider require an explicit features {} block inside provider "azurerm", even completely empty, or terraform init errors out. Some resource types also have provider-specific quirks and required arguments that are genuinely worth checking the Registry's docs page for before writing them from memory, rather than guessing based on what similar resources in Azure usually need.

## Key Terms
See GLOSSARY.md. New here: Authentication method (how you prove your identity to a platform before it lets you manage resources on it).

## Reference
- https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
- https://developer.hashicorp.com/terraform/tutorials/configuration-language/configure-providers
""",
"problem": """# Problem: The azurerm Provider

## Scenario
Time to actually declare your first real Azure resource through Terraform, starting with the simplest possible one, a resource group.

## Your task
In solution.tf:

1. Using the variables from module 3 (resource_group_name and location), write an azurerm_resource_group resource.
2. Run terraform plan and confirm it shows exactly 1 resource to add, nothing else.
3. In a comment, note which authentication method you're using to talk to Azure (interactive CLI login, service principal, or something else), and how you confirmed it's actually working before running plan.

## Hints
- Hint 1: az login before running any terraform command is the easiest authentication path for local practice, confirm you're logged into the right subscription with az account show before you plan against it.
- Hint 2: Azure region values for the location argument are lowercase strings like "eastus", not display names like "East US", using the wrong format will cause plan or apply to fail.
- Hint 3: If plan shows more than 1 resource to add, or shows changes to something you didn't expect, check whether you're accidentally still holding onto resources from an earlier module in the same .tf files.
"""
}

MODULES["06-resource-dependencies"] = {
"lesson": """# Resource Dependencies

## Status
In progress

## Lesson

### Implicit dependency
Referencing another resource's attribute inside a different resource block automatically tells Terraform the order things need to be created in, no extra syntax required:

```hcl
resource "azurerm_resource_group" "example" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorage"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
```

Because the storage account references azurerm_resource_group.example.name and .location directly, Terraform knows the resource group has to exist first, no extra configuration needed.

### Explicit dependency
depends_on = [ resource_address ], a meta-argument for cases where a real dependency exists but nothing in the code actually references the other resource's attributes, so Terraform has no way to detect it on its own.

### The dependency graph
Terraform builds a full dependency graph from every implicit and explicit relationship across your configuration, then creates and destroys resources in the correct order automatically, running anything unrelated in parallel when it safely can.

### Same idea, different syntax
If you worked through the bicep-arm-json section of this repo, this is the exact same implicit-vs-explicit concept from that section's dependencies module, just expressed in HCL instead of Bicep syntax.

## Key Terms
See GLOSSARY.md. Reinforces: Dependency graph.

## Reference
- https://developer.hashicorp.com/terraform/language/resources/behavior
""",
"problem": """# Problem: Resource Dependencies

## Scenario
You need a storage account that lives inside the resource group from module 5, and you want to prove the dependency is real by letting Terraform infer it, not by forcing it with depends_on.

## Your task
In solution.tf:

1. Add an azurerm_storage_account resource.
2. Set its resource_group_name and location arguments by referencing azurerm_resource_group.example.name and .location directly, not by retyping the values as separate strings or variables.
3. Run terraform plan and read the output carefully, confirm the resource group is listed as being created before the storage account, even though you didn't add any dependsOn.
4. In a comment, explain in your own words why this dependency exists without you having written it explicitly.

## Hints
- Hint 1: If you accidentally hardcode the resource group name as a plain string instead of referencing the resource's attribute, the implicit dependency disappears completely, Terraform would have no way to know the two resources are related.
- Hint 2: Storage account names have their own rules (lowercase letters and numbers only, globally unique across Azure), keep that in mind when picking a test name here, same rule as the Bicep section of this repo.
- Hint 3: terraform plan output lists resources roughly in dependency order when there's a real relationship, that ordering itself is a clue you can use to sanity-check whether Terraform actually detected the dependency you intended.
"""
}

MODULES["07-data-sources"] = {
"lesson": """# Data Sources

## Status
In progress

## Lesson

### What a data source is
A data block pulls in information about something that already exists, without Terraform creating, owning, or managing it. The syntax mirrors a resource block closely, which is intentional:

```hcl
data "azurerm_resource_group" "existing" {
  name = "rg-shared-networking"
}
```

Reference it with data.<type>.<label>.<attribute>, for example data.azurerm_resource_group.existing.location.

### Why this matters
Common real-world use: looking up a resource group, virtual network, or image that some other team or process already created and owns, so you can reference its properties without Terraform trying to take ownership of that resource's lifecycle. If you used a resource block instead of a data block for something you don't actually own, Terraform would try to manage (and potentially destroy) something it never should have touched.

### count and for_each work on data blocks too
Just like resources, you can add count or for_each to a data block to look up multiple instances at once, each one addressed independently afterward.

### A useful sanity check
If a data source's lookup can't find anything matching what you specified, Terraform will refuse to plan and error out, that's actually a helpful behavior, it catches typos in resource group names or missing prerequisites before you get further into a broken plan.

## Key Terms
See GLOSSARY.md. New here: Data source (read-only, Terraform looks it up but never creates, modifies, or destroys it, unlike a managed resource).

## Reference
- https://developer.hashicorp.com/terraform/language/data-sources
- https://developer.hashicorp.com/terraform/language/block/data
""",
"problem": """# Problem: Data Sources

## Scenario
Instead of creating a brand new resource group every time, you want to reuse the one you already created in module 5, without accidentally telling Terraform to manage it as a resource in this new configuration too.

## Your task
In solution.tf:

1. Add a data "azurerm_resource_group" block looking up the resource group you created in module 5 by name (not creating a new azurerm_resource_group resource here).
2. Add a new azurerm_storage_account resource that references the data source's .location and .name attributes, rather than a resource reference or a hardcoded string.
3. Run terraform plan and confirm it shows only the storage account being created, the resource group itself shows no changes at all, because it's only being read, not managed, by this configuration.

## Hints
- Hint 1: The arguments a specific data source accepts (just name for azurerm_resource_group, for example) come from that data source's page in the provider docs, don't assume every data source takes the same arguments.
- Hint 2: If plan shows the resource group itself as something to be created or modified, you've accidentally used a resource block instead of a data block somewhere, double check the block type.
- Hint 3: Deliberately typo the resource group name and run plan again, watch what error Terraform gives you, that's the sanity-check behavior mentioned in the lesson, worth seeing once on purpose.
"""
}

MODULES["08-count-and-for-each"] = {
"lesson": """# count and for_each

## Status
In progress

## Lesson

### count
Set count = N on a resource or module block to create N nearly-identical instances from one block. Each instance is addressed by a zero-based index:

```hcl
resource "azurerm_storage_account" "example" {
  count                    = 3
  name                     = "stg${count.index}${random_id.suffix.hex}"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
```

Reference a specific instance with azurerm_storage_account.example[0], [1], etc.

### for_each
Iterate over a map or a set of strings instead of a plain number, each instance addressed by its key rather than a numeric index:

```hcl
resource "azurerm_storage_account" "example" {
  for_each                 = toset(["logs", "backups", "archive"])
  name                     = "stg${each.key}${random_id.suffix.hex}"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
```

Reference a specific instance with azurerm_storage_account.example["logs"]. for_each needs a map or a set, toset() converts a plain list into a set for exactly this purpose.

### Why the choice actually matters, not just style
With count, removing an item from the middle of a list shifts every subsequent index down by one. Terraform tracks count-based resources by that index in state, so removing "backups" from a 3-item list can make Terraform think the third item changed, even though you only touched the second one, potentially destroying and recreating something you never meant to touch. for_each tracks by a stable key instead, so removing "backups" only affects the "backups" instance, everything else stays untouched.

HashiCorp's own guidance: use count for genuinely identical instances where index doesn't matter, use for_each when instances need distinct values or a stable identity that survives list changes. You cannot use both on the same block.

## Key Terms
See GLOSSARY.md. New here: Meta-argument (a built-in argument, like count, for_each, or depends_on, that works on any resource type and controls Terraform's own behavior rather than the resource's actual configuration), Index vs key (a number based on position, versus a stable name-based identifier).

## Reference
- https://developer.hashicorp.com/terraform/language/meta-arguments/count
- https://support.hashicorp.com/hc/en-us/articles/31348158569363-Terraform-count-versus-for-each-meta-argument
""",
"problem": """# Problem: count and for_each

## Scenario
You need the same three storage accounts from the Bicep loops module (logs, backups, archive), but this time in Terraform, and you want to prove to yourself exactly why for_each is the safer choice for a list that might change later.

## Your task
1. In one file, write the storage accounts using count, indexed against a list variable of three names.
2. In a second block (or comment out the first), write the same three storage accounts using for_each and toset() instead.
3. For the count version: remove the middle item from the list and run terraform plan, note exactly what Terraform says it wants to change or destroy.
4. For the for_each version: remove the middle item from the set and run terraform plan again, compare what it says this time.
5. Write a short comment explaining, in your own words, why the two plans looked different for the exact same change.

## Hints
- Hint 1: With count, index 2 refers to whatever is currently the third item in the list, if you remove item 1 (the middle one), what used to be item 2 shifts down to become the new item 1, that's the shift that causes the unexpected plan.
- Hint 2: toset(["logs", "backups", "archive"]) is required for for_each here, a plain list without toset() won't work directly with for_each in this context.
- Hint 3: each.key is how you reference the current item inside a for_each block, count.index is the equivalent for a count block, don't mix them up between the two versions.
"""
}

MODULES["09-modules"] = {
"lesson": """# Writing and Calling Modules

## Status
In progress

## Lesson

### Root modules and child modules
Every Terraform configuration is technically a module. The one you run terraform apply on directly is the root module. Anything it calls is a child module. This distinction matters once you start organizing real infrastructure.

### Standard child module layout
```
modules/
  storage-baseline/
    main.tf        # resources
    variables.tf   # input variables
    outputs.tf     # exposed outputs
    README.md
```

### Calling a module
```hcl
module "storage" {
  source              = "./modules/storage-baseline"
  resource_group_name = azurerm_resource_group.example.name
  location             = azurerm_resource_group.example.location
}
```

The module's own variables.tf defines exactly what it accepts as input, that's its interface. The calling (root) module supplies values for those variables directly as arguments inside the module block, it does not, and cannot, reach into the child module's internal resources directly.

### A module's outputs are how data flows back out
```hcl
output "storage_account_name" {
  value = module.storage.storage_account_name
}
```

Reference a child module's output from the calling file as module.<local-name>.<output-name>.

### Design guidance worth internalizing early
Only expose the outputs a caller actually needs, don't leak internal implementation details just because they're technically available. And a module that's just a thin wrapper around a single resource type, with no real abstraction added, usually isn't worth the extra layer, if you can't name the module something other than the resource type it wraps, that's often a sign to just use the resource directly instead.

## Key Terms
See GLOSSARY.md. New here: Root module (the top-level configuration you run apply on), Child module (a reusable module called by another configuration), Interface (the specific inputs a module accepts and outputs it exposes, its contract with whatever calls it).

## Reference
- https://developer.hashicorp.com/terraform/language/modules/develop
- https://developer.hashicorp.com/terraform/language/block/module
""",
"problem": """# Problem: Writing and Calling Modules

## Scenario
Your resource group + storage account pattern from earlier modules is something you'll want to stand up repeatedly for different projects. Time to turn it into a real reusable child module.

## Your task
1. Create a directory modules/storage-baseline/ with its own main.tf, variables.tf, and outputs.tf.
2. In variables.tf, define exactly the inputs the module needs: something like resource_group_name, location, and a name prefix for the storage account.
3. In main.tf, put the resource group and storage account resources, using the module's own variables, not anything from outside the module.
4. In outputs.tf, expose only what a caller would actually need, the storage account name and its resource ID, nothing else.
5. In your root solution.tf, call this module twice with two different name prefixes, standing up two separate environments from the same module code.

## Hints
- Hint 1: A child module's variables.tf has no idea what variables exist in your root configuration, everything it needs has to be explicitly passed in through the module block's arguments, there's no implicit sharing.
- Hint 2: Calling the same module twice means giving each call a different local name (module "dev_storage" and module "prod_storage", for example), and each call needs to result in different actual resource names to avoid a naming collision in Azure.
- Hint 3: Reference an output from either call in your root file as module.dev_storage.storage_account_name, the local name you gave the module call is part of the reference path.
"""
}

MODULES["10-remote-state-basics"] = {
"lesson": """# Remote State Basics (HCP Terraform)

## Status
In progress

## Lesson

### Why local state stops being enough
Local state, what you've used through every module so far, works fine solo. It breaks down the moment more than one person needs to run Terraform against the same infrastructure: two people applying against the same local state file at the same time can conflict or corrupt it, and state can contain secrets in plain text sitting on someone's individual laptop, which is a real security problem the moment more than one person is involved.

### HCP Terraform as a remote backend
HCP Terraform (formerly called Terraform Cloud) is HashiCorp's managed platform that can act as a remote backend, storing your state centrally instead of on anyone's individual machine, and it can also run plan and apply for you remotely rather than on your laptop.

```hcl
terraform {
  cloud {
    organization = "your-org-name"
    workspaces {
      name = "your-workspace-name"
    }
  }
}
```

You'll also need to run terraform login once to authenticate the CLI itself against HCP Terraform, that's a separate login from your Azure authentication.

### A pricing note worth knowing as of 2026
HCP Terraform's free offering changed during 2026: the older flat "500 managed resources free forever" plan ended March 31, 2026. New sign-ups now start on a Pay-As-You-Go plan with a starting credit balance instead of a hard resource cap. It still includes remote state, remote runs, and a private module registry. Since pricing and plan structures shift, check developer.hashicorp.com/terraform/cloud-docs for current numbers before assuming anything based on older tutorials or blog posts, including this one.

### terraform_remote_state
A data source that lets one completely separate Terraform configuration read the outputs of another configuration's state. This is how teams split infrastructure into layers, networking managed by one configuration, compute managed by a separate one, that reads the networking layer's outputs (like a VNet ID) without owning or touching the networking resources itself.

## Key Terms
See GLOSSARY.md. New here: Backend (where and how Terraform stores its state file), Remote state (state stored somewhere other than your local disk, typically for team collaboration and security).

## Reference
- https://developer.hashicorp.com/terraform/cloud-docs/overview
- https://developer.hashicorp.com/terraform/language/state
""",
"problem": """# Problem: Remote State Basics (HCP Terraform)

## Scenario
This module is setup-focused rather than code-heavy, the goal is experiencing the actual migration from local to remote state, not writing new resources.

## Your task
1. Sign up for HCP Terraform at app.terraform.io if you don't already have an account, and create an organization and a workspace.
2. Run terraform login once to authenticate your CLI against it.
3. Add a cloud {} block to the terraform {} block in your module 9 root configuration (or any earlier module's config), pointing at your new organization and workspace.
4. Run terraform init again, Terraform should detect the backend change and offer to migrate your existing local state up to HCP Terraform.
5. Confirm in the HCP Terraform web dashboard that your state actually shows up there now.

## Hints
- Hint 1: terraform login opens a browser for authentication, this is separate and unrelated to any Azure/az login you've done, don't confuse the two.
- Hint 2: When you run terraform init after adding the cloud {} block, read the prompt carefully, it will ask whether to copy existing state up to the new backend, say yes if you want to keep what you've already built.
- Hint 3: If you don't have an Azure account handy for this exercise and don't want to sign up for one just to test this, the local_file resource from module 2 is a perfectly good stand-in, remote state doesn't care what provider the resources belong to.
"""
}

MODULES["11-lifecycle-blocks"] = {
"lesson": """# Lifecycle Blocks

## Status
In progress

## Lesson

### What lifecycle controls
lifecycle {} is a nested block inside any resource that customizes how Terraform handles that specific resource's create, update, and destroy behavior, overriding Terraform's normal default handling.

### create_before_destroy
By default, when a change requires replacing a resource entirely (something that can't be updated in place due to the platform's own API limitations), Terraform destroys the old one first, then creates the new one. That gap means downtime for anything relying on that resource. create_before_destroy = true reverses the order, build the replacement first, then tear down the old one, reducing or eliminating that gap.

```hcl
resource "azurerm_storage_account" "example" {
  # ...
  lifecycle {
    create_before_destroy = true
  }
}
```

### prevent_destroy
prevent_destroy = true makes Terraform refuse to destroy that resource, erroring out instead of proceeding. Genuinely useful for anything where accidental deletion would be a serious problem, a production database, an encryption key, a DNS zone.

The real gotcha: this rule only protects the resource while the lifecycle block itself is still present in your configuration. If someone removes the entire resource block from your .tf files, prevent_destroy goes with it, and Terraform will destroy the real object during the next apply anyway, protection bypassed entirely, no error. To legitimately destroy a protected resource, remove the prevent_destroy rule first, apply that change, then destroy, a deliberate two-step process.

### ignore_changes
ignore_changes = [ attribute, ... ] tells Terraform to stop flagging drift on specific attributes, useful when something outside Terraform, an autoscaler, a manual tag someone adds through the portal, legitimately and repeatedly changes a value you don't want constantly fighting with your configuration on every plan. Use ignore_changes = all to ignore every attribute (Terraform can still create and destroy the object, but will never propose an update to it).

## Key Terms
See GLOSSARY.md. New here: Downtime (a gap where a resource is unavailable, relevant to why create_before_destroy exists), reinforces Drift from module 4.

## Reference
- https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle
""",
"problem": """# Problem: Lifecycle Blocks

## Scenario
The storage account you've been building across earlier modules is exactly the kind of resource you don't want accidentally destroyed by a careless terraform destroy run.

## Your task
1. Add a lifecycle block with prevent_destroy = true to your storage account resource.
2. Run terraform destroy and confirm Terraform actually refuses and errors out instead of proceeding.
3. Now remove the protection the correct, deliberate way: edit the configuration to set prevent_destroy = false (or remove the lifecycle block entirely), run terraform apply to register that change, and only then run terraform destroy.
4. In a comment, note what would have happened if you'd instead just deleted the entire resource block to "get around" the protection, without going through the proper two-step process.

## Hints
- Hint 1: The error message from a blocked destroy attempt is worth reading carefully, it tells you exactly which resource and which lifecycle setting is stopping it.
- Hint 2: prevent_destroy must be a literal true or false, you can't drive it from a variable or expression, Terraform evaluates lifecycle rules before it evaluates most other expressions in your configuration.
- Hint 3: This two-step "remove protection, apply, then destroy" process is intentional friction, it exists specifically to make you think twice before it happens, don't look for a faster workaround, there isn't meant to be one.
"""
}

MODULES["12-plan-output-and-state-commands"] = {
"lesson": """# Reading Plan Output and terraform state Commands

## Status
In progress

## Lesson

### The symbols in plan output
- + create
- - destroy
- ~ update in place
- -/+ destroy and recreate (a full replacement, not an update)

Reading a plan carefully before typing yes isn't a formality, it's the actual safety mechanism the entire workflow is built around. This is where you catch an unexpected replacement (which usually means real downtime, and sometimes real data loss) before it happens instead of after.

### terraform state list
Lists every resource address currently tracked in state, the starting point whenever you need to reference a specific resource with any other state subcommand.

### terraform state show
```
terraform state show azurerm_storage_account.example
```
Prints the full set of attributes Terraform has recorded for one specific resource, straight from state, without touching real infrastructure.

### terraform state mv
```
terraform state mv azurerm_storage_account.example azurerm_storage_account.baseline
```
Renames or moves a resource's tracked address in state without destroying and recreating the real underlying object. This matters after any kind of refactor, renaming a resource block, moving a resource into a module, because without it, Terraform sees the old address disappear and a "new" resource appear at the new address, and plans to destroy the old one and create a new one, even though nothing about the real infrastructure needed to change at all.

Takes the OLD address first, then the NEW address, in that order.

### A safety habit worth keeping
All state-modifying subcommands write a local backup file automatically before making any change, because state is genuinely sensitive to corruption. Still, always run terraform plan again after any state mv or similar operation to confirm you actually fixed what you meant to fix, don't just assume the command worked as intended.

## Key Terms
See GLOSSARY.md. New here: Replacement (destroy and recreate, shown as -/+ in plan output), In-place update (a change applied to the existing object without destroying it, shown as ~).

## Reference
- https://developer.hashicorp.com/terraform/cli/commands/state
- https://developer.hashicorp.com/terraform/tutorials/state/state-cli
""",
"problem": """# Problem: Reading Plan Output and terraform state Commands

## Scenario
You've decided azurerm_storage_account.example should really be named azurerm_storage_account.baseline going forward, a pure naming cleanup, nothing about the actual Azure resource should change.

## Your task
1. Rename the resource block in your configuration from azurerm_storage_account.example to azurerm_storage_account.baseline, purely a text change in the .tf file.
2. Run terraform plan and read the output, it should show the old address being destroyed and a new one being created, a full replacement, even though you know nothing real needs to change.
3. Instead of applying that plan (which would cause real downtime and possibly data loss for no reason), fix it properly with terraform state mv azurerm_storage_account.example azurerm_storage_account.baseline.
4. Run terraform plan again and confirm it now shows no changes at all, proving the state now matches your renamed configuration without ever touching the real resource.

## Hints
- Hint 1: terraform state mv takes the address exactly as it currently exists in state first (the OLD one), then the new address you want it tracked as, get this order backwards and the command will fail or do the wrong thing.
- Hint 2: Don't skip step 4, running plan again after the state mv is what actually confirms you fixed it, assuming it worked without checking is exactly the mistake this whole module is trying to train you out of.
- Hint 3: If you're unsure of the exact current address to use in the mv command, terraform state list will show you precisely how it's currently recorded, character for character.
"""
}

# --- Full repo scaffold (creates the whole IaC-Fundamentals-Bootcamp skeleton) ---
# Included so this script can be run standalone, on an empty folder, and still
# produce a complete, valid repo. Only fills in files that don't already exist,
# so it never overwrites content another one of these scripts already populated.

GLOSSARY_CONTENT = """# General IaC Concepts

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
"""

SCAFFOLD_SECTIONS = [
    (
        "powershell",
        "PowerShell",
        [
            ("01-variables-and-output", "Variables, Data Types, and Output", "ps1"),
            ("02-control-flow", "Control Flow: If/Else, Switch, Loops", "ps1"),
            ("03-functions", "Functions: Params, Return Values, Scope", "ps1"),
            ("04-arrays-and-hashtables", "Arrays and Hashtables", "ps1"),
            ("05-the-pipeline", "The Pipeline: Where-Object, Sort-Object, Select-Object", "ps1"),
            ("06-string-manipulation", "String Manipulation and Formatting", "ps1"),
            ("07-error-handling", "Error Handling: Try/Catch/Finally", "ps1"),
            ("08-files-and-csv", "Files: Get-Content, Set-Content, CSV Import/Export", "ps1"),
            ("09-json-in-powershell", "JSON in PowerShell: ConvertTo-Json / ConvertFrom-Json", "ps1"),
            ("10-script-structure", "Script Structure: Params Blocks, Comment-Based Help", "ps1"),
            ("11-az-powershell-basics", "Az PowerShell Module Basics", "ps1"),
        ],
    ),
    (
        "bicep-arm-json",
        "Bicep, ARM, and JSON",
        [
            ("01-arm-json-anatomy", "ARM JSON Anatomy", "json"),
            ("02-bicep-basics", "Bicep Basics: JSON to Bicep", "bicep"),
            ("03-parameters-and-variables", "Parameters and Variables", "bicep"),
            ("04-outputs", "Outputs", "bicep"),
            ("05-expressions-and-functions", "Expressions and Built-In Functions", "bicep"),
            ("06-conditionals-and-loops", "Conditionals and Loops", "bicep"),
            ("07-modules", "Modules", "bicep"),
            ("08-dependencies", "Dependencies: Implicit vs Explicit", "bicep"),
            ("09-array-loops-multiple-resources", "Array Loops for Multiple Resources", "bicep"),
            ("10-deployment-scopes", "Deployment Scopes", "bicep"),
            ("11-what-if-and-validation", "What-If and Validation Workflow", "bicep"),
            ("12-decompile-arm-to-bicep", "Decompiling ARM to Bicep", "bicep"),
        ],
    ),
    (
        "terraform",
        "Terraform",
        [
            ("01-iac-concepts-and-providers", "IaC Concepts, Providers, Resource Blocks", "tf"),
            ("02-core-workflow", "Core Workflow: Init, Plan, Apply, Destroy", "tf"),
            ("03-variables-and-outputs", "Variables and Outputs", "tf"),
            ("04-state", "State: What It Is and Why It Matters", "tf"),
            ("05-azurerm-provider", "The azurerm Provider", "tf"),
            ("06-resource-dependencies", "Resource Dependencies", "tf"),
            ("07-data-sources", "Data Sources", "tf"),
            ("08-count-and-for-each", "count and for_each", "tf"),
            ("09-modules", "Writing and Calling Modules", "tf"),
            ("10-remote-state-basics", "Remote State Basics (HCP Terraform)", "tf"),
            ("11-lifecycle-blocks", "Lifecycle Blocks", "tf"),
            ("12-plan-output-and-state-commands", "Reading Plan Output and terraform state Commands", "tf"),
        ],
    ),
]

def _stub_lesson(title: str) -> str:
    return f"""# {title}

## Status
Not started

## Lesson
(To be filled in when you start this module.)

## Key Terms
See GLOSSARY.md at the repo root for terms used in this module.
"""

def _stub_problem(title: str) -> str:
    return f"""# Problem: {title}

(Problem to be added when you start this module.)
"""

def _stub_solution(ext: str) -> str:
    comment = "#" if ext in ("ps1", "tf") else "//"
    return f"{comment} Solution - write your work here\n"

def _write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content)
    return True

def scaffold(base: Path):
    """Creates the full repo skeleton: all 3 sections' stub folders, README.md,
    GLOSSARY.md. Never overwrites a file that already exists, so it's safe to
    call even after other sections have already been populated for real."""
    base.mkdir(exist_ok=True)
    _write_if_missing(base / "GLOSSARY.md", GLOSSARY_CONTENT)
    _write_if_missing(base / "ENVIRONMENT-SETUP.md", ENVIRONMENT_SETUP_CONTENT)

    readme_lines = [
        "# IaC Fundamentals Bootcamp",
        "",
        "Hands-on bootcamp covering PowerShell, Bicep/ARM/JSON, and Terraform in one repo.",
        "Each module has a lesson.md, a problem.md, and a solution file. Work modules in any order.",
        "See GLOSSARY.md for terminology.",
        "",
    ]
    for folder, title, modules in SCAFFOLD_SECTIONS:
        section_path = base / folder
        section_path.mkdir(exist_ok=True)
        readme_lines.append(f"# {title}")
        readme_lines.append("")
        for slug, mod_title, ext in modules:
            module_path = section_path / slug
            module_path.mkdir(exist_ok=True)
            _write_if_missing(module_path / "lesson.md", _stub_lesson(mod_title))
            _write_if_missing(module_path / "problem.md", _stub_problem(mod_title))
            _write_if_missing(module_path / f"solution.{ext}", _stub_solution(ext))
            readme_lines.append(f"- [ ] {slug}: {mod_title}")
        readme_lines.append("")
    _write_if_missing(base / "README.md", "\n".join(readme_lines))

# --- Environment setup (written once at repo root, alongside README/GLOSSARY) ---

ENVIRONMENT_SETUP_CONTENT = """# Environment Setup

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

## Practicing Safely
The early modules (variables, output, control flow) only touch memory and the console, nothing on disk, nothing on the network. Run those checkpoints directly in your real terminal, there's nothing to protect against yet.

That changes once a module starts reading or writing files (module 8), or touching real Azure resources (module 11 and the Bicep/Terraform sections). A few ways to practice those safely, easiest first:

**A dedicated scratch folder.** For anything that reads or writes files, point every path in a practice script at one throwaway folder, like `~/ps-practice`, instead of anywhere that matters. Worst case you lose test files you didn't care about.

**Windows Sandbox.** Built into Windows 10/11 Pro for free. Search "Windows Sandbox" in the Start menu (enable it under Windows Features if it's not already on). It opens a completely clean, disposable Windows desktop in seconds, closing the window throws away every change inside it, no cleanup needed. Best option if you're on Windows and haven't set anything else up yet.

**A spare VM.** If you've got Windows Server or Linux VMs available, take a snapshot before practicing, revert it after. This is the best fit once you're running real Az cmdlets or actually touching Azure resources, not just local files.

**-WhatIf for state-changing cmdlets.** Not a sandbox, but a lot of cmdlets, especially in the Az module, support `-WhatIf`, which shows exactly what would happen without doing it. Example: `Remove-AzResourceGroup -Name test -WhatIf`. Check with `Get-Help <cmdlet> -Full` first, not every cmdlet supports it. Good as a second layer even inside a sandbox or VM, not a replacement for one.

## Reference
- https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows
- https://learn.microsoft.com/en-us/powershell/scripting/install/install-rhel
- https://learn.microsoft.com/en-us/powershell/scripting/install/alternate-install-methods
- https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows
- https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux
- https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/install
- https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
"""


# --- Interactive lesson transformation ---
# Applied to every lesson.md at write time. Finds each fenced code block and
# inserts a hands-on checkpoint right after it, so the lesson itself is
# practiced as you read it, not just read and then practiced later in the
# problem. Doesn't require touching the 35 lesson strings by hand, it's a
# consistent transformation applied uniformly across every module.

import re as _re

_CHECKPOINT_TEMPLATES = {
    "powershell": "Type the code above into a scratch file (try.ps1) or directly into your terminal, and run it before reading on. Confirm you actually see what the lesson just described, don't just take it on faith.",
    "json": "Type the code above into a scratch file (try.json) yourself rather than copy-pasting it. Read back through it and confirm you can name what each part is doing before moving on.",
    "bicep": "Type the code above into a scratch file (try.bicep), then run `az bicep build --file try.bicep` against it and confirm it compiles with no errors before reading on.",
    "hcl": "Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.",
    "bash": "Run the command above yourself in your terminal before reading on, don't just read what it's supposed to do.",
}
_DEFAULT_CHECKPOINT = "Type the code above yourself and try running or reasoning through it before reading on."

_CODE_BLOCK_PATTERN = _re.compile(r'(```([a-zA-Z]*)\n.*?```)', _re.DOTALL)

def make_interactive(lesson_text: str) -> str:
    counter = {"n": 0}

    def _replacer(match: "_re.Match") -> str:
        counter["n"] += 1
        block = match.group(1)
        lang = match.group(2).lower()
        instruction = _CHECKPOINT_TEMPLATES.get(lang, _DEFAULT_CHECKPOINT)
        checkpoint = f"\n\n> **Try it now, Checkpoint {counter['n']}**\n> {instruction}\n"
        return block + checkpoint

    result = _CODE_BLOCK_PATTERN.sub(_replacer, lesson_text)

    intro_note = (
        "## Lesson\n\n"
        "*This lesson is interactive. Complete each numbered checkpoint as you reach it, "
        "don't read past it and come back later, the point is building the muscle memory "
        "while the concept is still right in front of you.*\n"
    )
    result = result.replace("## Lesson\n", intro_note, 1)

    return result

def write_module(section_path: Path, slug: str, content: dict):
    module_path = section_path / slug
    module_path.mkdir(parents=True, exist_ok=True)
    (module_path / "lesson.md").write_text(make_interactive(content["lesson"]))
    (module_path / "problem.md").write_text(content["problem"])

def build():
    base = Path(REPO_NAME)
    scaffold(base)  # creates the full repo skeleton if it doesn't exist yet
    section_path = base / SECTION
    section_path.mkdir(parents=True, exist_ok=True)
    for slug, content in MODULES.items():
        write_module(section_path, slug, content)
    print(f"Populated {len(MODULES)} modules in {SECTION}/ (full repo skeleton ensured)")

if __name__ == "__main__":
    build()