# 💿 Sara AI - Windows Installer Guide

## 🌟 **Overview**

This guide shows you how to create a professional Windows installer (.exe) for Sara AI that can be distributed to end users. The installer will handle .NET dependencies, create shortcuts, and provide an easy installation experience.

---

## 🎯 **What You'll Create**

- **Professional .exe installer** for Sara AI
- **Automatic .NET 6.0 installation** (if missing)
- **Desktop and Start Menu shortcuts**
- **Uninstaller support**
- **Administrative privileges handling**
- **File associations and registry entries**

**Result:** Single .exe file that installs Sara AI completely

---

## 🛠️ **Method 1: Using Inno Setup (Recommended)**

### **Step 1: Install Inno Setup**

#### **Download and Install**
```bash
# Download from: https://www.jrsoftware.org/isinfo.php
# Or using package manager:
winget install JRSoftware.InnoSetup
```

### **Step 2: Prepare Sara AI for Distribution**

#### **Create Self-Contained Build**
```bash
# Navigate to Sara AI project folder
cd C:\Users\%USERNAME%\Desktop\SaraAI_CSharp

# Create self-contained executable (includes .NET runtime)
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true

# Alternative: Framework-dependent (smaller, requires .NET installed)
dotnet publish -c Release -r win-x64 --self-contained false -p:PublishSingleFile=true
```

#### **Output Location**
The built executable will be in:
```
bin\Release\net6.0-windows\win-x64\publish\SaraAI.exe
```

### **Step 3: Create Inno Setup Script**

#### **Create SaraAI-Installer.iss**
```pascal
; Sara AI Installer Script for Inno Setup

[Setup]
AppName=Sara AI
AppVersion=4.0
AppPublisher=Selva.Ux
AppPublisherURL=https://github.com/SelvaUx
AppSupportURL=https://github.com/SelvaUx/SaraAI_CSharp/issues
AppUpdatesURL=https://github.com/SelvaUx/SaraAI_CSharp/releases
DefaultDirName={autopf}\Sara AI
DefaultGroupName=Sara AI
AllowNoIcons=yes
LicenseFile=LICENSE.txt
OutputDir=installer
OutputBaseFilename=SaraAI-v4.0-Setup
SetupIconFile=assets\sara-icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1

[Files]
; Main executable
Source: "bin\Release\net6.0-windows\win-x64\publish\SaraAI.exe"; DestDir: "{app}"; Flags: ignoreversion

; Documentation
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "How to Run.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "Dual Mode Operation.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "Windows Installer.md"; DestDir: "{app}"; Flags: ignoreversion

; Assets
Source: "assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs createallsubdirs

; .NET 6.0 Runtime installer (optional)
Source: "redist\dotnet-6.0-runtime-win-x64.exe"; DestDir: "{tmp}"; Flags: ignoreversion deleteafterinstall; Check: NeedsDotNet

[Icons]
Name: "{group}\Sara AI"; Filename: "{app}\SaraAI.exe"
Name: "{group}\{cm:UninstallProgram,Sara AI}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Sara AI"; Filename: "{app}\SaraAI.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Sara AI"; Filename: "{app}\SaraAI.exe"; Tasks: quicklaunchicon

[Run]
; Install .NET 6.0 if needed
Filename: "{tmp}\dotnet-6.0-runtime-win-x64.exe"; Parameters: "/quiet"; StatusMsg: "Installing .NET 6.0 Runtime..."; Check: NeedsDotNet

; Run Sara AI after installation
Filename: "{app}\SaraAI.exe"; Description: "{cm:LaunchProgram,Sara AI}"; Flags: nowait postinstall skipifsilent

[Registry]
; Register Sara AI
Root: HKLM; Subkey: "Software\Microsoft\Windows\CurrentVersion\Uninstall\Sara AI"; ValueType: string; ValueName: "DisplayName"; ValueData: "Sara AI v4.0"
Root: HKLM; Subkey: "Software\Microsoft\Windows\CurrentVersion\Uninstall\Sara AI"; ValueType: string; ValueName: "Publisher"; ValueData: "Selva.Ux"
Root: HKLM; Subkey: "Software\Microsoft\Windows\CurrentVersion\Uninstall\Sara AI"; ValueType: string; ValueName: "DisplayVersion"; ValueData: "4.0"

[Code]
function NeedsDotNet(): Boolean;
var
  Version: String;
begin
  Result := not RegQueryStringValue(HKLM, 'SOFTWARE\dotnet\Setup\InstalledVersions\x64\sharedhost', 'Version', Version);
end;

function InitializeSetup(): Boolean;
begin
  Result := True;
  if not IsWin64 then
  begin
    MsgBox('Sara AI requires a 64-bit version of Windows.', mbError, MB_OK);
    Result := False;
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // Configure Windows Firewall exception for LM Studio integration
    Exec('netsh', 'advfirewall firewall add rule name="Sara AI" dir=in action=allow program="' + ExpandConstant('{app}') + '\SaraAI.exe"', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
  end;
end;
```

### **Step 4: Create Supporting Files**

#### **Create LICENSE.txt**
```text
MIT License

Copyright (c) 2024 Selva Pandi Francis (Selva.Ux)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

#### **Create Application Icon (Optional)**
1. Create or download a 256x256 PNG icon for Sara AI
2. Convert to .ico format using online converters
3. Save as `assets/sara-icon.ico`

### **Step 5: Build the Installer**

#### **Compile with Inno Setup**
1. **Open Inno Setup Compiler**
2. **File** → **Open** → Select `SaraAI-Installer.iss`
3. **Build** → **Compile** (or press F9)
4. Wait for compilation to complete

#### **Output**
The installer will be created as:
```
installer/SaraAI-v4.0-Setup.exe
```

---

## 🛠️ **Method 2: Using WiX Toolset (Advanced)**

### **Step 1: Install WiX Toolset**

#### **Download and Install**
```bash
# Download from: https://wixtoolset.org/releases/
# Or using package manager:
winget install WiXToolset.WiXToolset
```

### **Step 2: Create WiX Project**

#### **Create SaraAI.wxs**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Wix xmlns="http://schemas.microsoft.com/wix/2006/wi">
  <Product Id="*" 
           Name="Sara AI" 
           Language="1033" 
           Version="4.0.0.0" 
           Manufacturer="Selva.Ux" 
           UpgradeCode="PUT-GUID-HERE">
    
    <Package InstallerVersion="200" 
             Compressed="yes" 
             InstallScope="perMachine" 
             Platform="x64" />

    <MajorUpgrade DowngradeErrorMessage="A newer version of Sara AI is already installed." />
    <MediaTemplate EmbedCab="yes" />

    <Feature Id="ProductFeature" Title="Sara AI" Level="1">
      <ComponentGroupRef Id="ProductComponents" />
      <ComponentRef Id="ApplicationShortcut" />
      <ComponentRef Id="DesktopShortcut" />
    </Feature>

    <!-- UI Configuration -->
    <UIRef Id="WixUI_InstallDir" />
    <Property Id="WIXUI_INSTALLDIR" Value="INSTALLFOLDER" />
    
    <!-- License Agreement -->
    <WixVariable Id="WixUILicenseRtf" Value="License.rtf" />
    
    <!-- Application Icon -->
    <Icon Id="SaraAI.exe" SourceFile="assets\sara-icon.ico" />
    <Property Id="ARPPRODUCTICON" Value="SaraAI.exe" />
  </Product>

  <Fragment>
    <Directory Id="TARGETDIR" Name="SourceDir">
      <Directory Id="ProgramFiles64Folder">
        <Directory Id="INSTALLFOLDER" Name="Sara AI" />
      </Directory>
      <Directory Id="ProgramMenuFolder">
        <Directory Id="ApplicationProgramsFolder" Name="Sara AI"/>
      </Directory>
      <Directory Id="DesktopFolder" Name="Desktop" />
    </Directory>
  </Fragment>

  <Fragment>
    <ComponentGroup Id="ProductComponents" Directory="INSTALLFOLDER">
      <!-- Main executable -->
      <Component Id="SaraAI.exe" Guid="PUT-GUID-HERE">
        <File Id="SaraAI.exe" 
              Source="bin\Release\net6.0-windows\win-x64\publish\SaraAI.exe" 
              KeyPath="yes" />
      </Component>
      
      <!-- Documentation -->
      <Component Id="Documentation" Guid="PUT-GUID-HERE">
        <File Id="README.md" Source="README.md" />
        <File Id="HowToRun.md" Source="How to Run.md" />
        <File Id="DualMode.md" Source="Dual Mode Operation.md" />
      </Component>
      
      <!-- Assets folder -->
      <Component Id="Assets" Guid="PUT-GUID-HERE">
        <File Id="VoiceModelsReadme" Source="assets\voiceModels\README.md" />
      </Component>
    </ComponentGroup>
    
    <!-- Start Menu Shortcut -->
    <Component Id="ApplicationShortcut" Directory="ApplicationProgramsFolder" Guid="PUT-GUID-HERE">
      <Shortcut Id="ApplicationStartMenuShortcut"
                Name="Sara AI"
                Description="Voice-Controlled PC Assistant"
                Target="[#SaraAI.exe]"
                WorkingDirectory="INSTALLFOLDER"/>
      <RemoveFolder Id="ApplicationProgramsFolder" On="uninstall"/>
      <RegistryValue Root="HKCU" 
                     Key="Software\Microsoft\Sara AI" 
                     Name="installed" 
                     Type="integer" 
                     Value="1" 
                     KeyPath="yes"/>
    </Component>
    
    <!-- Desktop Shortcut -->
    <Component Id="DesktopShortcut" Directory="DesktopFolder" Guid="PUT-GUID-HERE">
      <Shortcut Id="DesktopShortcut"
                Name="Sara AI"
                Description="Voice-Controlled PC Assistant"
                Target="[#SaraAI.exe]"
                WorkingDirectory="INSTALLFOLDER"/>
      <RegistryValue Root="HKCU" 
                     Key="Software\Microsoft\Sara AI" 
                     Name="desktop" 
                     Type="integer" 
                     Value="1" 
                     KeyPath="yes"/>
    </Component>
  </Fragment>
</Wix>
```

### **Step 3: Build WiX Installer**

#### **Compile MSI Package**
```bash
# Navigate to project directory
cd C:\Users\%USERNAME%\Desktop\SaraAI_CSharp

# Compile WiX source to object file
candle SaraAI.wxs

# Link object file to create MSI
light SaraAI.wixobj -ext WixUIExtension -out SaraAI-Installer.msi
```

---

## 🛠️ **Method 3: Using NSIS (Alternative)**

### **Step 1: Install NSIS**

#### **Download and Install**
```bash
# Download from: https://nsis.sourceforge.io/
# Or using package manager:
winget install Nullsoft.NSIS
```

### **Step 2: Create NSIS Script**

#### **Create SaraAI-Installer.nsi**
```nsis
; Sara AI NSIS Installer Script

!define APPNAME "Sara AI"
!define COMPANYNAME "Selva.Ux"
!define DESCRIPTION "Voice-Controlled PC Assistant"
!define VERSIONMAJOR 4
!define VERSIONMINOR 0
!define VERSIONBUILD 0
!define HELPURL "https://github.com/SelvaUx/SaraAI_CSharp"
!define UPDATEURL "https://github.com/SelvaUx/SaraAI_CSharp/releases"
!define ABOUTURL "https://github.com/SelvaUx"
!define INSTALLSIZE 50000

RequestExecutionLevel admin
InstallDir "$PROGRAMFILES64\${APPNAME}"
LicenseData "LICENSE.txt"
Name "${APPNAME}"
Icon "assets\sara-icon.ico"
outFile "SaraAI-v4.0-Installer.exe"

!include LogicLib.nsh

page license
page directory
page instfiles

!macro VerifyUserIsAdmin
UserInfo::GetAccountType
pop $0
${If} $0 != "admin"
    messageBox mb_iconstop "Administrator rights required!"
    setErrorLevel 740
    quit
${EndIf}
!macroend

function .onInit
    setShellVarContext all
    !insertmacro VerifyUserIsAdmin
functionEnd

section "install"
    # Files to install
    setOutPath $INSTDIR
    file /r "bin\Release\net6.0-windows\win-x64\publish\SaraAI.exe"
    file "README.md"
    file "How to Run.md"
    file "Dual Mode Operation.md"
    file /r "assets"
    
    # Uninstaller
    writeUninstaller "$INSTDIR\uninstall.exe"
    
    # Start Menu
    createDirectory "$SMPROGRAMS\${COMPANYNAME}"
    createShortCut "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk" "$INSTDIR\SaraAI.exe" "" "$INSTDIR\assets\sara-icon.ico"
    
    # Desktop shortcut
    createShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\SaraAI.exe" "" "$INSTDIR\assets\sara-icon.ico"
    
    # Registry information for add/remove programs
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "DisplayName" "${APPNAME}"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "InstallLocation" "$\"$INSTDIR$\""
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "DisplayIcon" "$\"$INSTDIR\assets\sara-icon.ico$\""
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "Publisher" "${COMPANYNAME}"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "HelpLink" "${HELPURL}"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "URLUpdateInfo" "${UPDATEURL}"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "URLInfoAbout" "${ABOUTURL}"
    writeRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "DisplayVersion" "${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}"
    writeRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "VersionMajor" ${VERSIONMAJOR}
    writeRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "VersionMinor" ${VERSIONMINOR}
    writeRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "NoModify" 1
    writeRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "NoRepair" 1
    writeRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "EstimatedSize" ${INSTALLSIZE}
sectionEnd

# Uninstaller
function un.onInit
    SetShellVarContext all
    MessageBox MB_OKCANCEL "Permanently remove ${APPNAME}?" IDOK next
        Abort
    next:
    !insertmacro VerifyUserIsAdmin
functionEnd

section "uninstall"
    # Remove Start Menu launcher
    delete "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk"
    rmDir "$SMPROGRAMS\${COMPANYNAME}"
    
    # Remove Desktop shortcut
    delete "$DESKTOP\${APPNAME}.lnk"
    
    # Remove files
    delete "$INSTDIR\SaraAI.exe"
    delete "$INSTDIR\README.md"
    delete "$INSTDIR\How to Run.md"
    delete "$INSTDIR\Dual Mode Operation.md"
    rmDir /r "$INSTDIR\assets"
    delete "$INSTDIR\uninstall.exe"
    rmDir "$INSTDIR"
    
    # Remove uninstaller information from the registry
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}"
sectionEnd
```

### **Step 3: Build NSIS Installer**

#### **Compile NSIS Script**
```bash
# Right-click SaraAI-Installer.nsi → "Compile NSIS Script"
# Or use command line:
makensis SaraAI-Installer.nsi
```

---

## 📦 **Advanced Installer Features**

### **Auto-Update Functionality**

#### **Add Update Checker to Sara AI**
```csharp
// Add to Utilities.cs
public async Task<bool> CheckForUpdates()
{
    try
    {
        using (var client = new HttpClient())
        {
            var response = await client.GetStringAsync("https://api.github.com/repos/SelvaUx/SaraAI_CSharp/releases/latest");
            var release = JsonSerializer.Deserialize<GitHubRelease>(response);
            
            var currentVersion = new Version("4.0.0");
            var latestVersion = new Version(release.tag_name.Replace("v", ""));
            
            return latestVersion > currentVersion;
        }
    }
    catch
    {
        return false;
    }
}

public class GitHubRelease
{
    public string tag_name { get; set; }
    public string html_url { get; set; }
}
```

### **Silent Installation Options**

#### **Add to Inno Setup Script**
```pascal
[Setup]
; Allow silent installation
SilentInstall=yes
SetupLogging=yes

[Run]
; Don't show launch option in silent mode
Filename: "{app}\SaraAI.exe"; Description: "{cm:LaunchProgram,Sara AI}"; Flags: nowait postinstall skipifsilent
```

#### **Silent Install Commands**
```bash
# Silent installation
SaraAI-v4.0-Setup.exe /SILENT

# Very silent (no progress dialog)
SaraAI-v4.0-Setup.exe /VERYSILENT

# Silent with log file
SaraAI-v4.0-Setup.exe /SILENT /LOG="install.log"
```

### **Multi-Language Support**

#### **Add Languages to Inno Setup**
```pascal
[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"
```

---

## 🔧 **Deployment Strategies**

### **Strategy 1: GitHub Releases**

#### **Automated Release with GitHub Actions**
```yaml
# .github/workflows/release.yml
name: Create Release

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: windows-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup .NET
      uses: actions/setup-dotnet@v3
      with:
        dotnet-version: 6.0.x
        
    - name: Publish
      run: dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true
      
    - name: Build Installer
      run: |
        # Install Inno Setup
        choco install innosetup -y
        # Compile installer
        iscc SaraAI-Installer.iss
        
    - name: Create Release
      uses: actions/create-release@v1
      with:
        tag_name: ${{ github.ref }}
        release_name: Sara AI ${{ github.ref }}
        body: |
          Sara AI Voice Assistant Release
          
          ## Download Options:
          - **Installer**: SaraAI-v4.0-Setup.exe (Recommended)
          - **Portable**: SaraAI.exe (Advanced users)
          
          ## System Requirements:
          - Windows 10/11 (64-bit)
          - Microphone and speakers
          - Optional: LM Studio for AI features
        draft: false
        prerelease: false
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        
    - name: Upload Installer
      uses: actions/upload-release-asset@v1
      with:
        upload_url: ${{ steps.create_release.outputs.upload_url }}
        asset_path: ./installer/SaraAI-v4.0-Setup.exe
        asset_name: SaraAI-v4.0-Setup.exe
        asset_content_type: application/octet-stream
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### **Strategy 2: Microsoft Store**

#### **Prepare for Microsoft Store**
```xml
<!-- Add to SaraAI.csproj -->
<PropertyGroup>
  <WindowsPackageType>MSIX</WindowsPackageType>
  <WindowsAppSDKSelfContained>true</WindowsAppSDKSelfContained>
  <UseWinUI>true</UseWinUI>
</PropertyGroup>
```

### **Strategy 3: Chocolatey Package**

#### **Create Chocolatey Package**
```powershell
# Create chocolatey package
choco new saraai

# Edit saraai.nuspec
# Build package
choco pack

# Publish to Chocolatey
choco push saraai.4.0.0.nupkg --source https://push.chocolatey.org/
```

---

## 🧪 **Testing Your Installer**

### **Automated Testing**

#### **Create Test Script**
```powershell
# test-installer.ps1

Write-Host "Testing Sara AI Installer..." -ForegroundColor Green

# Test silent installation
Write-Host "Testing silent installation..."
Start-Process "SaraAI-v4.0-Setup.exe" -ArgumentList "/VERYSILENT" -Wait

# Verify installation
if (Test-Path "C:\Program Files\Sara AI\SaraAI.exe") {
    Write-Host "✅ Installation successful" -ForegroundColor Green
} else {
    Write-Host "❌ Installation failed" -ForegroundColor Red
    exit 1
}

# Test application launch
Write-Host "Testing application launch..."
$process = Start-Process "C:\Program Files\Sara AI\SaraAI.exe" -PassThru
Start-Sleep 5
if (!$process.HasExited) {
    Write-Host "✅ Application launches successfully" -ForegroundColor Green
    $process.Kill()
} else {
    Write-Host "❌ Application failed to launch" -ForegroundColor Red
}

# Test uninstallation
Write-Host "Testing uninstallation..."
Start-Process "C:\Program Files\Sara AI\unins000.exe" -ArgumentList "/VERYSILENT" -Wait

if (!(Test-Path "C:\Program Files\Sara AI")) {
    Write-Host "✅ Uninstallation successful" -ForegroundColor Green
} else {
    Write-Host "❌ Uninstallation failed" -ForegroundColor Red
}

Write-Host "Installer testing complete!" -ForegroundColor Green
```

### **Manual Testing Checklist**

#### **Installation Testing**
- [ ] Installer runs without errors
- [ ] Admin privileges requested appropriately
- [ ] All files copied correctly
- [ ] Shortcuts created (Desktop, Start Menu)
- [ ] Registry entries added
- [ ] .NET dependency handled
- [ ] Application launches after installation

#### **Functionality Testing**
- [ ] Voice recognition works
- [ ] Basic commands execute
- [ ] File operations succeed
- [ ] LM Studio integration (if available)
- [ ] All modules function correctly

#### **Uninstallation Testing**
- [ ] Uninstaller removes all files
- [ ] Shortcuts removed
- [ ] Registry entries cleaned
- [ ] No leftover folders or files

---

## 📈 **Distribution Best Practices**

### **Code Signing**

#### **Sign Your Installer**
```bash
# Using SignTool (requires code signing certificate)
signtool sign /f "certificate.pfx" /p "password" /t "http://timestamp.comodoca.com" "SaraAI-v4.0-Setup.exe"

# Verify signature
signtool verify /pa "SaraAI-v4.0-Setup.exe"
```

### **Installer Size Optimization**

#### **Reduce Installer Size**
1. **Use framework-dependent deployment** (requires .NET installed)
2. **Compress assets** using 7-zip or similar
3. **Remove unnecessary files** from publish output
4. **Use external downloads** for large dependencies

### **Version Management**

#### **Semantic Versioning**
```
MAJOR.MINOR.PATCH
4.0.0 - Initial release
4.0.1 - Bug fixes
4.1.0 - New features
5.0.0 - Breaking changes
```

---

## 🎯 **Quick Summary**

### **Recommended Approach**
1. **Use Inno Setup** for maximum compatibility
2. **Create self-contained build** with `dotnet publish`
3. **Include .NET runtime check** in installer
4. **Test thoroughly** on clean Windows installations
5. **Sign installer** for security and trust

### **File Sizes (Approximate)**
- **Self-contained installer**: 60-80MB
- **Framework-dependent installer**: 15-25MB
- **Portable executable**: 50-70MB

### **Distribution Channels**
- **GitHub Releases** (Primary)
- **Direct download** from website
- **Package managers** (Chocolatey, Winget)
- **Microsoft Store** (Future consideration)

---

**Congratulations! You now know how to create professional Windows installers for Sara AI! 🎉💿**
