#'"C:\Program Files\National Instruments\VeriStand 2020\Veristand.exe" -openProject "$(Build.Repository.LocalPath)\$(projectName).nivsprj" -sysDef "$(Build.Repository.LocalPath)\$(systemDefinitionFile)." -deploy'

Start-Process -FilePath "C:\Program Files\National Instruments\VeriStand 2020\veristand.exe" -ArgumentList '-openProject "C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf"', '-deploy' -WindowStyle Normal