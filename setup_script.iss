[Setup]
AppName=collectWeb
AppVersion=1.0
DefaultDirName={pf}\collectWeb
DefaultGroupName=collectWeb
OutputBaseFilename=collectWebInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\collectWeb"; Filename: "{app}\start_app.exe"
Name: "{commondesktop}\collectWeb"; Filename: "{app}\start_app.exe"; Tasks: desktopicon


[Run]
Filename: "{app}\start_app.exe"; Description: "Launch collectWeb"; Flags: nowait postinstall skipifsilent
[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"