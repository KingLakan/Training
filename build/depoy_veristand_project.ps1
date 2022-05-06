#'"C:\Program Files\National Instruments\VeriStand 2020\Veristand.exe" -openProject "$(Build.Repository.LocalPath)\$(projectName).nivsprj" -sysDef "$(Build.Repository.LocalPath)\$(systemDefinitionFile)." -deploy'

Write-Host "Running deploy veristand"
#$test = start-Process -FilePath "C:\Program Files\National Instruments\VeriStand 2020\veristand.exe" -ArgumentList '-openProject "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo 2.nivsprj"','-sysDef "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf"', '-deploy' -passThru -Wait
#$test = start-Process -FilePath "C:\Program Files\National Instruments\VeriStand 2020\veristand.exe" -ArgumentList '-openProject "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo 2.nivsprj"','-sysDef "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf"' -passThru -Wait
#$test.StartTime

#& "C:\Program Files\National Instruments\VeriStand 2020\veristand.exe" -openProject "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo 2.nivsprj" -sysDef "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf" -deploy
#$test | get-process


$pinfo = New-Object System.Diagnostics.ProcessStartInfo
$pinfo.FileName = "C:\Program Files\National Instruments\VeriStand 2020\veristand.exe"
$pinfo.Arguments ='-openProject "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo 2.nivsprj" -sysDef "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf" -deploy'
$pinfo.RedirectStandardError = $true
$pinfo.RedirectStandardOutput = $true
$pinfo.UseShellExecute = $false
$pinfo.Arguments = "localhost"
$p = New-Object System.Diagnostics.Process
$p.StartInfo = $pinfo
$p.Start() | Out-Null
$p.WaitForExit()
$stdout = $p.StandardOutput.ReadToEnd()
$stderr = $p.StandardError.ReadToEnd()
Write-Host "stdout: $stdout"
Write-Host "stderr: $stderr"
Write-Host "exit code: " + $p.ExitCode
