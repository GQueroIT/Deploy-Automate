# Problem: Parameters and Variables

## Scenario
You're standardizing how your team parameterizes deployments across dev, test, and prod, and you need to make sure nobody can accidentally typo an environment name or leak a password into deployment logs.

## Your task
In solution.bicep:

1. Declare an environment parameter (string), restricted with @allowed to only 'dev', 'test', or 'prod', with a @description explaining what it's for.
2. Declare an adminPassword parameter (string), marked @secure(), with no default value.
3. Declare a variable resourcePrefix that computes a different prefix string depending on the environment parameter (for example, 'dev-app', 'test-app', 'prod-app'), using a ternary or similar expression.
4. Add a resource of any type (reuse the storage account from module 2 if you want) that uses resourcePrefix as part of its name.

## Hints
- Hint 1: @allowed takes a literal array as its argument, written directly in the decorator, ['dev', 'test', 'prod'].
- Hint 2: @secure() only works on parameters typed string or object, if you try it on an int or bool parameter it won't be valid.
- Hint 3: For the ternary, environment == 'prod' ? 'prod-app' : 'nonprod-app' is the basic shape, you can nest more conditions if you want three distinct prefixes instead of two.

## Expected Result
Attempting to deploy or compile with an environment value outside dev/test/prod should fail validation immediately. Your adminPassword parameter should never appear in plain text anywhere in compiled output.

## Cost & Cleanup
If you deployed this for real, clean up when you're done: az group delete --name <your-rg> --yes --no-wait.
