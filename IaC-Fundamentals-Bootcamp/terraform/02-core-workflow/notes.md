# Lab 02 - Terraform Core Workflow

## Objective

Learn the basic Terraform workflow from beginning to end.

Instead of creating something in Azure, I used Terraform to create a simple text file on my computer.

This gave me a safe way to practice:

```text
Init
  ↓
Plan
  ↓
Apply
  ↓
Destroy
```

without creating a cloud resource or worrying about cost.

---

## What I Did

I added the HashiCorp Local provider alongside the AzureRM provider.

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }

    local = {
      source  = "hashicorp/local"
      version = "~> 2.9.0"
    }
  }
}

provider "azurerm" {
  features {}
}

provider "local" {}
```

I then created a local file resource:

```hcl
resource "local_file" "terraformrocks" {
  filename = "terraformrocks.txt"
  content  = "Terraform rocks!"
}
```

Terraform created:

```text
terraformrocks.txt
```

with:

```text
Terraform rocks!
```

At the end of the lab, I used Terraform to destroy the resource and watched the file disappear.

---

## What I Learned

### Using More Than One Provider

Terraform can use more than one provider in the same configuration.

In this lab I had:

```text
azurerm
local
```

AzureRM gives Terraform the ability to work with Azure.

The Local provider gives Terraform the ability to manage certain things on my local computer, such as files.

Each provider gets its own section inside:

```hcl
required_providers
```

---

### Provider Source vs Provider Name

This confused me at first.

I originally wrote:

```hcl
provider "hashicorp/local" {}
```

Terraform gave me an error.

I learned that:

```text
hashicorp/local
      ↓
Where Terraform gets the provider

local
      ↓
The name I use for the provider in my code
```

That means:

```hcl
local = {
  source = "hashicorp/local"
}
```

uses the full source address.

But when configuring it, I use:

```hcl
provider "local" {}
```

The same idea applies to AzureRM:

```text
hashicorp/azurerm = Provider source

azurerm = Name used in my Terraform code
```

---

## Provider Versions

I originally copied the AzureRM version:

```hcl
version = "~> 4.0"
```

and used it for the Local provider.

Terraform returned an error saying that no available Local provider releases matched that version.

This taught me that every provider has its own versions.

```text
AzureRM Provider
      ↓
Has its own versions

Local Provider
      ↓
Has its own versions
```

I cannot assume that because one provider uses version 4.x, another provider does too.

I corrected the Local provider to:

```hcl
version = "~> 2.9.0"
```

and ran:

```bash
terraform init
```

again.

Terraform was then able to initialize successfully.

---

## Creating My First Terraform Resource

I created:

```hcl
resource "local_file" "terraformrocks" {
  filename = "terraformrocks.txt"
  content  = "Terraform rocks!"
}
```

I learned how to start reading a Terraform resource block.

```text
resource "local_file" "terraformrocks"
            ↓               ↓
       Resource Type    Name I gave it
                        inside Terraform
```

Inside the resource:

```hcl
filename = "terraformrocks.txt"
```

tells Terraform what I want the file to be called.

```hcl
content = "Terraform rocks!"
```

tells Terraform what I want written inside the file.

The basic idea is:

```text
I describe what I want
        ↓
Terraform figures out how to create it
```

---

## terraform init

After adding the Local provider, I ran:

```bash
terraform init
```

Terraform downloaded what it needed for the Local provider.

This reinforced something I learned in Lab 01:

If I add or change provider requirements, I should expect to run `terraform init` again.

---

## terraform plan

I ran:

```bash
terraform plan
```

Terraform showed:

```text
Plan: 1 to add, 0 to change, 0 to destroy.
```

This was one of the most important parts of the lab.

`terraform plan` showed me what Terraform wanted to do **before it actually did it**.

I think of it as:

```text
terraform plan
      ↓
"Show me what you're about to do."
```

The numbers also tell me a lot:

```text
1 to add
=
Terraform wants to create one resource.

0 to change
=
Terraform does not need to modify anything.

0 to destroy
=
Terraform does not plan to delete anything.
```

In a real environment, I should read this before applying changes.

---

## terraform apply

I ran:

```bash
terraform apply
```

Terraform showed the plan again and asked me to confirm.

I entered:

```text
yes
```

Terraform then created the resource.

The result showed:

```text
Apply complete!

Resources: 1 added, 0 changed, 0 destroyed.
```

I could then see:

```text
terraformrocks.txt
```

inside the folder.

This was the first time I actually watched Terraform take my code and turn it into something real.

---

## Terraform State

After running `terraform apply`, I also saw:

```text
terraform.tfstate
```

I learned that Terraform uses state to keep track of the resources it manages.

For now, I understand it like this:

```text
My Terraform Code
      ↓
What I WANT

terraformrocks.txt
      ↓
What actually EXISTS

terraform.tfstate
      ↓
Terraform's RECORD of what it manages
```

I do not know everything about Terraform state yet, but I understand that it is important.

Terraform needs a way to remember what resources belong to the configuration.

---

## terraform destroy

At the end of the lab, I ran:

```bash
terraform destroy
```

Terraform showed:

```text
Plan: 0 to add, 0 to change, 1 to destroy.
```

This told me Terraform planned to remove one resource.

After I entered:

```text
yes
```

Terraform removed:

```text
terraformrocks.txt
```

and reported:

```text
Destroy complete!

Resources: 1 destroyed.
```

This showed me that Terraform can manage the entire life of a resource.

It can create it, track it, and remove it.

---

## The Core Terraform Workflow

The workflow makes more sense to me now:

```text
Write Terraform Code
        ↓
terraform fmt
        ↓
terraform validate
        ↓
terraform init
        ↓
terraform plan
        ↓
READ THE PLAN
        ↓
terraform apply
        ↓
Resource Created
        ↓
Terraform Tracks It
        ↓
terraform destroy
        ↓
Resource Removed
```

I do not want to just memorize these commands.

I want to remember what each one is doing:

```text
fmt
=
Clean up my Terraform code.

validate
=
Check whether my configuration makes sense to Terraform.

init
=
Prepare the folder and download what Terraform needs.

plan
=
Show me what Terraform wants to do.

apply
=
Actually make the changes.

destroy
=
Remove the resources Terraform manages.
```

---

## Troubleshooting

### Problem 1 - Wrong Provider Name

I originally wrote:

```hcl
provider "hashicorp/local" {}
```

Terraform returned:

```text
Invalid provider local name
```

I learned that `hashicorp/local` is the source address.

The provider block should use:

```hcl
provider "local" {}
```

---

### Problem 2 - Wrong Provider Version

I originally used:

```hcl
version = "~> 4.0"
```

for the Local provider because AzureRM was using version 4.x.

Terraform could not find a Local provider release that matched what I requested.

I learned that provider versions are independent.

I fixed the Local provider version and ran:

```bash
terraform init
```

again.

---

### Problem 3 - New Provider Needed Initialization

After adding the Local provider, Terraform told me the required provider was missing.

The code knew that I wanted to use Local, but Terraform still needed to download the provider.

I fixed this with:

```bash
terraform init
```

This showed me why initialization is needed when provider requirements change.

---

## Best Practices

* Use `terraform fmt` to keep my code clean.
* Use `terraform validate` to check the configuration.
* Run `terraform init` when providers are added or changed.
* Check provider versions instead of guessing them.
* Always read `terraform plan` before applying changes.
* Pay attention to how many resources Terraform wants to add, change, or destroy.
* Be especially careful if Terraform unexpectedly wants to destroy something.
* Treat `terraform.tfstate` as important.
* Do not manually edit the state file just because something looks wrong.
* Remember that `terraform destroy` can delete real infrastructure when I start working with Azure.

---

## Key Takeaways

This lab helped me understand why Terraform is more than just writing code.

I wrote what I wanted:

```text
Create terraformrocks.txt
and put "Terraform rocks!" inside it.
```

Terraform then showed me what it planned to do.

I approved the change.

Terraform created the file and kept track of it.

Then I used Terraform to remove it.

The biggest workflow I want to remember is:

```text
Describe what I want
        ↓
Check what Terraform plans to do
        ↓
Review it
        ↓
Apply it
        ↓
Terraform manages it
```

The troubleshooting also taught me not to treat every Terraform error the same way.

One error came from using the wrong provider name.

Another came from requesting a provider version that did not exist.

Another happened because Terraform needed to initialize the new provider.

The first thing I should do when Terraform fails is read the error and figure out **what type of problem it is** before I start changing things.
