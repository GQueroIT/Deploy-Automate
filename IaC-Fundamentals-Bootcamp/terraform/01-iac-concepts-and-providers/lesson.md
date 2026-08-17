# IaC Concepts, Providers, Resource Blocks

By the end of this module, you'll be able to declare which provider a Terraform configuration needs and configure it correctly, including the quirks that trip up a first init.

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

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

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.


If you don't pin a version constraint, terraform init can install a newer major version of a provider later on, which can silently change behavior. Pinning it protects you from that.

One quirk worth knowing up front: recent versions of the azurerm provider require the features {} block inside provider "azurerm" even when there's nothing inside it. Leaving it out entirely will cause terraform init to error.

### Resource blocks, at a glance
You'll go deep on these in a later module, but the shape is: resource "<provider_type>" "<local_name>" { arguments }. The local name is just how you refer to that resource elsewhere in your own configuration, it isn't the actual name Azure gives the resource.

## Commands Used in This Lesson

- `terraform init` — Prepares the working directory and downloads required providers. Example: `terraform init`

## Troubleshooting

- terraform init fails immediately after adding the provider block. Recent azurerm versions require the features {} block even empty, missing it is the single most common first-run error.
- init downloads a newer provider version than you expected. You didn't pin a version constraint, or pinned it too loosely, tighten the version argument in required_providers.

## Key Terms
See GLOSSARY.md at the repo root. This module leans on: HCL, Provider, Resource block, Declarative, Idempotent.

## Reference
- https://developer.hashicorp.com/terraform/intro
- https://developer.hashicorp.com/terraform/language/providers
- https://developer.hashicorp.com/terraform/language/providers/requirements
- https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
