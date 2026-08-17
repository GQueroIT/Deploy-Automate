$firstname = "Gabe"
$TicketCount = 10
$IsResolved = $True
Write-Host "Hello $firstname, you have $TicketCount tickets to resolve. Resolved status: $IsResolved"

$firstname = "Gabe"
$firstinitial = $firstname.Substring(0,1)
$lowered = $firstinitial.ToLower()
Write-Host "The first initial of $firstname is $lowered"