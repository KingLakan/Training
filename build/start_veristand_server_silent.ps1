Start-Process -FilePath "C:\Program Files (x86)\National Instruments\VeriStand 2020\veristand-server.exe" "start" -WindowStyle Normal
Get-Process veristand-server
Start-Process -FilePath "C:\Program Files (x86)\National Instruments\VeriStand 2020\veristand-server.exe" "status" -WindowStyle Normal

#Stop-Process -Name "winver" -PassThru