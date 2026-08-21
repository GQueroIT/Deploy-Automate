# Lab 01 - IaC Concepts and Providers

## Objective

Learn the basic structure of Terraform and understand what a provider does.

For this lab, I was not trying to create anything in Azure yet. I wanted to understand what Terraform needs before it can work with Azure.

---

## What I Did

I created a basic Terraform configuration using the AzureRM provider.

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

I practiced using:

```bash
terraform fmt
terraform validate
terraform init
```

---

## What I Learned

### Terraform Providers

Terraform needs providers to work with different platforms.

For Azure, I am using:

```text
hashicorp/azurerm
```

The easiest way for me to understand this is:

```text
Terraform = The tool I am using

AzureRM Provider = Gives Terraform the ability to work with Azure
```

Terraform itself does not automatically know how to manage Azure resources. The AzureRM provider gives Terraform that ability.

---

### required_providers

This section tells Terraform which provider my configuration needs:

```hcl
required_providers {
  azurerm = {
    source  = "hashicorp/azurerm"
    version = "~> 4.0"
  }
}
```

I learned that each part has a purpose.

```text
azurerm
```

This is the name I use for the provider inside my Terraform configuration.

```text
hashicorp/azurerm
```

This tells Terraform where the provider comes from.

```text
~> 4.0
```

This tells Terraform which provider versions it is allowed to use.

---

### Provider Block

The provider block is separate:

```hcl
provider "azurerm" {
  features {}
}
```

For now, I think of the difference like this:

```text
required_providers
=
What provider does Terraform need?

provider "azurerm"
=
Configure that provider so Terraform can use it.
```

---

## Terraform Commands

### terraform fmt

```bash
terraform fmt
```

Formats my Terraform files so the code is clean and consistent.

---

### terraform validate

```bash
terraform validate
```

Checks whether Terraform understands my configuration and whether the structure is valid.

---

### terraform init

```bash
terraform init
```

Prepares the current folder for Terraform.

It also downloads the providers that my configuration requires.

---

## Troubleshooting

### Problem 1 - Trying to Validate One File

I originally ran:

```bash
terraform validate try.tf
```

Terraform returned an error.

I learned that `terraform validate` checks the Terraform configuration in the current folder.

The correct command was:

```bash
terraform validate
```

---

### Problem 2 - Missing Provider

When I first ran:

```bash
terraform validate
```

Terraform told me the AzureRM provider was missing.

My code said that I needed the provider, but Terraform had not downloaded it yet.

I fixed it by running:

```bash
terraform init
```

After that, I ran:

```bash
terraform validate
```

and the configuration passed.

---

### Problem 3 - Duplicate Provider Configuration

I created:

```text
try.tf
```

so I could practice the code from the lesson.

I also had:

```text
solution.tf
```

in the same folder.

Both files contained similar provider configurations, so Terraform reported duplicate provider errors.

This taught me something important:

```text
Terraform reads the .tf files in the same folder together.
```

For example:

```text
main.tf
providers.tf
network.tf
outputs.tf
```

These can all be different files, but Terraform sees them as pieces of the same configuration.

The filenames help me organize my work, but they do not automatically make the files separate Terraform projects.

Since `try.tf` was only for practice, I deleted it.

---

## Files Created by terraform init

After running:

```bash
terraform init
```

I noticed Terraform created:

```text
.terraform/
.terraform.lock.hcl
```

### .terraform/

This is a local working folder used by Terraform.

It can contain things such as downloaded providers.

I normally should **not commit this folder to Git**.

---

### .terraform.lock.hcl

This file keeps track of the provider versions Terraform selected.

This file normally **should be committed to Git**.

That helps keep provider versions more consistent when the project is used again.

---

## Best Practices

* Use `terraform fmt` to keep my Terraform code clean.
* Use `terraform validate` to check my configuration.
* Run `terraform init` when starting a Terraform working folder.
* Run `terraform init` again when provider requirements change.
* Remember that Terraform reads `.tf` files in the same folder together.
* Do not commit the `.terraform/` folder to Git.
* Commit `.terraform.lock.hcl`.
* Read the Terraform error message before randomly changing code.

---

## Key Takeaways

The biggest thing I learned was how Terraform uses providers.

```text
Terraform
    |
    v
AzureRM Provider
    |
    v
Azure
```

I also learned the beginning of the Terraform workflow:

```text
Write the configuration
        |
        v
terraform fmt
        |
        v
terraform init
        |
        v
terraform validate
```

The troubleshooting helped me understand how Terraform looks at my files.

I now know that Terraform does not treat every `.tf` file in the same folder as a separate project. It reads them together as one configuration.

I also learned that when Terraform gives me an error, I should slow down and read exactly what it is telling me. The error usually gives me a clue about what part of the configuration is wrong.
