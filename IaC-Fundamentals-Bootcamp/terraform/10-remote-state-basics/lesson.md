# Remote State Basics (HCP Terraform)

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

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

> **Try it now, Checkpoint 1**
> Type the code above into a scratch file (try.tf), then run `terraform fmt` and `terraform validate` against it and confirm it passes before reading on.


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
