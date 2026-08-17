# Problem: count and for_each

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
