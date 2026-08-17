## Your task
## Write a script (solution.ps1) that:

## 1. Stores a new employee's first name and last name in two separate variables.
## 2. Builds a username by combining the first letter of the first name with the full last name, all lowercase. Example: John + Smith becomes jsmith.
## 3. Displays a friendly on-screen message confirming the generated username, meant purely for whoever is running the script to read. This output should never be capturable by another command down the line.
## 4. Separately, outputs just the username by itself in a way that could be captured into a variable or piped into another cmdlet.
## 5. Bonus: add a variable for department and include it in the on-screen message from step 3, but do not include it in the piped output from step 4. 

$firstname = "Gabriel"
$lastname = "Quero"
$departmentName = "IT"
$firstinitial = $firstname.Substring(0,1)
$username = $firstinitial.Tolower() + $lastname.Tolower()

Write-Host "The new hire employee's name is $username and he should be added to the $departmentName department."
Write-Output $username