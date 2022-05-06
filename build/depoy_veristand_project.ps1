#'"C:\Program Files\National Instruments\VeriStand 2020\Veristand.exe" -openProject "$(Build.Repository.LocalPath)\$(projectName).nivsprj" -sysDef "$(Build.Repository.LocalPath)\$(systemDefinitionFile)." -deploy'

Write-Host "Running deploy veristand"
#$test = start-Process -FilePath "C:\Program Files\National Instruments\VeriStand 2020\veristand.exe" -ArgumentList '-openProject "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo 2.nivsprj"','-sysDef "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf"', '-deploy' -passThru -Wait
$test = start-Process -FilePath "C:\Program Files\National Instruments\VeriStand 2020\veristand.exe" -ArgumentList '-openProject "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo 2.nivsprj"','-sysDef "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf"' -passThru -RedirectStandardOutput Out.txt -RedirectStandardError Err.txt
Write-Host "Done"
exit 0
#$test.StartTime 

#& "C:\Program Files\National Instruments\VeriStand 2020\veristand.exe" -openProject "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo 2.nivsprj" -sysDef "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf" -deploy
#$test | get-process


