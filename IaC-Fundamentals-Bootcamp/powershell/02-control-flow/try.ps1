if ($status -eq "down") {
    Write-Host "The system is down. Please check the server"
} elseif ($status -eq "degraded") {
    Write-Host "Degraded"
} else {
    Write-Host "The system is up and running"
}