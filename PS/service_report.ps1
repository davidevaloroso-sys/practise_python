#Da una o più macchine Windows raccogli:
#elenco servizi
#servizi automatici in esecuzione
#eventi di sistema e sicurezza
#eventi relativi ai servizi
#eventuali log PowerShell operativi

#pulizia vecchi file .csv & .json
try { 
    Remove-Item -Path $outputPath
    Remove-Item -Path $outjson
}
catch {
    
    Write-Host "File non trovati, procedo con la creazione..."
}
Finally {
    Write-Host "Cleanup Completo"
}
#elenco servizi + esportazione in CSV 
$outputPath = "$env:USERPROFILE\practise_python\PS\services.csv"
Get-Service | Select-Object Name, DisplayName, Status, StartType | Export-Csv -Path $outputPath -NoTypeInformation -Encoding UTF8
Write-Host "Esportazione completata: $outputPath" -ForegroundColor Green
#servizi automatici in esecuzione + export su file CSV precedentemente creato
Get-Service | Where-Object {$_.Status -eq 'Running' -and $_.StartType -eq 'Automatic'} | Select-Object Name, DisplayName, Status, StartType | Export-Csv -Path $outputPath -NoTypeInformation -Append -Encoding UTF8

#Tipo elevazione token indica il tipo di token assegnato al nuovo processo in conformità con il criterio Controllo account 
#              utente.
#               
#              Il tipo 1 è un token completo in cui non sono stati rimossi privilegi o disabilitati gruppi. Un token completo viene 
#               utilizzato solo se Controllo account utente è disabilitato o se l'utente è l'account Administrator predefinito o un account 
#               di servizio.
#               
#               Il tipo 2 è un token elevato in cui non sono stati rimossi privilegi o disabilitati gruppi. Un token elevato viene utilizzato 
#               quando Controllo account utente è abilitato e l'utente sceglie di avviare il programma utilizzando Esegui come 
#              amministratore. Un token elevato viene anche utilizzato quando un'applicazione è configurata per richiedere sempre privilegi 
#               amministrativi o il privilegio più elevato e l'utente è membro del gruppo Administrators.
#               
#               Il tipo 3 è un token limitato con privilegi amministrativi rimossi e gruppi amministrativi disabilitati. Un token limitato 
#               viene utilizzato quando Controllo account utente è abilitato, l'applicazione non richiede privilegi amministrativi e l'utente 
#               non sceglie di avviare il programma utilizzando Esegui come amministratore.
#eventi di sistema e sicurezza
$outjson = "$env:USERPROFILE\practise_python\PS\events.json"
Get-WinEvent -FilterHashtable @{ 
    LogName = @('Security', 'System') 
    StartTime = (Get-Date).AddDays(-1)
    id = @('4625', '4720', '4732', '4672', '1102', '4624')
} | 
ConvertTo-Json -Depth 10 | 
Out-File $outjson -Encoding utf8

Write-Host "Esportati eventi Security+System ultimi 24h in $outjson"
#eventi relativi ai servizi
$Time = (Get-Date).AddHours(-24)
Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Service Control Manager'; StartTime=$Time} | Format-Table TimeCreated, Message -AutoSize | ConvertTo-Json | Out-File $outjson -Append -Encoding utf8
#eventuali log PowerShell operativi
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-PowerShell/Operational'
    StartTime = (Get-Date).AddDays(-1)
} | Sort-Object TimeCreated -Descending | Format-Table -AutoSize
