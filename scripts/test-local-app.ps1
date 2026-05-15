Write-Host "Testing root endpoint..."
Invoke-RestMethod -Uri "http://localhost:5000/" -Method GET

Write-Host "`nTesting health endpoint..."
Invoke-RestMethod -Uri "http://localhost:5000/health" -Method GET

Write-Host "`nTesting admin endpoint..."
Invoke-RestMethod -Uri "http://localhost:5000/admin" -Method GET

Write-Host "`nTesting failed login..."
$badBody = @{
  username = "admin"
  password = "wrongpassword"
} | ConvertTo-Json

try {
  Invoke-RestMethod -Uri "http://localhost:5000/login" -Method POST -ContentType "application/json" -Body $badBody
} catch {
  Write-Host "Expected failed login response received."
  Write-Host $_.Exception.Message
}

Write-Host "`nTesting successful login..."
$goodBody = @{
  username = "admin"
  password = "password123"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/login" -Method POST -ContentType "application/json" -Body $goodBody

Write-Host "`nLocal app testing complete."