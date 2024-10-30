$exclude = @("venv", "bot-tkinter-atividade-13.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-tkinter-atividade-13.zip" -Force