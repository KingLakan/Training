#'"C:\Program Files\National Instruments\VeriStand 2020\Veristand.exe" -openProject "$(Build.Repository.LocalPath)\$(projectName).nivsprj" -sysDef "$(Build.Repository.LocalPath)\$(systemDefinitionFile)." -deploy'

Write-Host "Running deploy veristand"
Write-Host "Start Gateway"
$cwd = Get-Location
py.exe $cwd\start_gateway.py

Write-Host "Deploy System definition"
py.exe $cwd\deploy.py