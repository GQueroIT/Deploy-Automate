# Problem: State: What It Is and Why It Matters

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
