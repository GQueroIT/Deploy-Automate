# Problem: Core Workflow: Init, Plan, Apply, Destroy

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
