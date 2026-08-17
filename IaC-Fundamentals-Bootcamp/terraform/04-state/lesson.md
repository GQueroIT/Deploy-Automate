# State: What It Is and Why It Matters

## Status
In progress

## Lesson

*This lesson is interactive. Complete each numbered checkpoint as you reach it, don't read past it and come back later, the point is building the muscle memory while the concept is still right in front of you.*

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
