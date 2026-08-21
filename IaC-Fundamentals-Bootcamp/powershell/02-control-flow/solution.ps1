# Solution - write your work here
$servers = @(
  @{ ServerName = "Server01"; Status = "UP" }
  @{ ServerName = "Server02"; Status = "Down" }
  @{ ServerName = "Server03"; Status = "Down" }
  @{ ServerName = "Server04"; Status = "Up" }
  @{ ServerName = "Server05"; Status = "Degraded" }
  @{ ServerName = "Server06"; Status = "Maintenance" }
  @{ ServerName = "Server07"; Status = "monkeys" }
)

foreach ($server in $servers) {
  if ($server.Status -eq "Down") {
    Write-Host "$($server.ServerName) is down"
  }
  elseif ($server.Status -eq "Degraded") {
    Write-Host "$($server.ServerName) is degraded"
  }
  elseif ($server.Status -eq "Up") {
    Write-Host "$($server.ServerName) is Up"
  }
  elseif ($server.Status -eq "Maintenance") {
    Write-Host "$($server.ServerName) is under maintenance"
  }
  else {
    Write-Host "$($server.ServerName) has an unknown status: $($server.Status)"
  }
}