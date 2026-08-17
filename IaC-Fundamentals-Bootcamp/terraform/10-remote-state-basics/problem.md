# Problem: Remote State Basics (HCP Terraform)

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

## Expected Result
After init with the cloud block added, your state should be visible in the HCP Terraform workspace dashboard in the browser, not just locally anymore.
