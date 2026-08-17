# Problem: Reading Plan Output and terraform state Commands

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

## Expected Result
After your state mv, running terraform plan again should show 'No changes.' exactly, not a pending destroy/recreate.

## Cost & Cleanup
Once your state matches your configuration again, terraform destroy when you're fully done with this resource.
