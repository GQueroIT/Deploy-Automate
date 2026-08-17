# Problem: Lifecycle Blocks

## Scenario
The storage account you've been building across earlier modules is exactly the kind of resource you don't want accidentally destroyed by a careless terraform destroy run.

## Your task
1. Add a lifecycle block with prevent_destroy = true to your storage account resource.
2. Run terraform destroy and confirm Terraform actually refuses and errors out instead of proceeding.
3. Now remove the protection the correct, deliberate way: edit the configuration to set prevent_destroy = false (or remove the lifecycle block entirely), run terraform apply to register that change, and only then run terraform destroy.
4. In a comment, note what would have happened if you'd instead just deleted the entire resource block to "get around" the protection, without going through the proper two-step process.

## Hints
- Hint 1: The error message from a blocked destroy attempt is worth reading carefully, it tells you exactly which resource and which lifecycle setting is stopping it.
- Hint 2: prevent_destroy must be a literal true or false, you can't drive it from a variable or expression, Terraform evaluates lifecycle rules before it evaluates most other expressions in your configuration.
- Hint 3: This two-step "remove protection, apply, then destroy" process is intentional friction, it exists specifically to make you think twice before it happens, don't look for a faster workaround, there isn't meant to be one.

## Expected Result
terraform destroy on the protected resource should fail with an error naming prevent_destroy specifically. After removing the setting and applying that change, destroy should succeed.

## Cost & Cleanup
This module is specifically about protecting a resource from deletion, that's the point, but don't forget to actually destroy it through the proper two-step process once you're fully done with the exercise.
