# SaraAI 5.0 - Windows Build Script
# Builds all modules in the correct order

param(
    [string]$Configuration = "Debug",
    [switch]$Clean = $false,
    [switch]$SkipTests = $false,
    [string]$Module = ""
)

$ErrorActionPreference = "Stop"

# Colors for output
function Write-ColoredOutput {
    param([string]$Message, [string]$Color = "White")
    Write-Host $Message -ForegroundColor $Color
}

function Write-Success { param([string]$Message) Write-ColoredOutput "✅ $Message" "Green" }
function Write-Info { param([string]$Message) Write-ColoredOutput "ℹ️ $Message" "Cyan" }
function Write-Warning { param([string]$Message) Write-ColoredOutput "⚠️ $Message" "Yellow" }
function Write-Error { param([string]$Message) Write-ColoredOutput "❌ $Message" "Red" }

Write-ColoredOutput "🤖 SaraAI 5.0 - Multi-Language Build System" "Magenta"
Write-ColoredOutput "=============================================" "Magenta"
Write-Info "Configuration: $Configuration"
Write-Info "Clean build: $Clean"
Write-Info "Skip tests: $SkipTests"

if ($Module) {
    Write-Info "Building specific module: $Module"
}

# Get the script directory and project root
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir

# Function to check if a command exists
function Test-Command {
    param([string]$Command)
    try {
        if (Get-Command $Command -ErrorAction Stop) { return $true }
    } catch {
        return $false
    }
}

# Function to build a module
function Invoke-ModuleBuild {
    param(
        [string]$Name,
        [string]$Path,
        [scriptblock]$BuildScript,
        [scriptblock]$TestScript = $null
    )
    
    if ($Module -and $Module -ne $Name) {
        Write-Info "Skipping $Name (not selected)"
        return
    }
    
    Write-Info "Building $Name module..."
    $ModulePath = Join-Path $ProjectRoot $Path
    
    if (-not (Test-Path $ModulePath)) {
        Write-Error "Module path not found: $ModulePath"
        return $false
    }
    
    Push-Location $ModulePath
    try {
        if ($Clean) {
            Write-Info "Cleaning $Name..."
            # Module-specific clean commands will be in the build script
        }
        
        # Execute the build script
        & $BuildScript
        if ($LASTEXITCODE -ne 0) {
            throw "Build failed for $Name"
        }
        
        # Run tests if enabled and test script provided
        if (-not $SkipTests -and $TestScript) {
            Write-Info "Running tests for $Name..."
            & $TestScript
            if ($LASTEXITCODE -ne 0) {
                Write-Warning "Tests failed for $Name (continuing anyway)"
            }
        }
        
        Write-Success "$Name built successfully"
        return $true
    }
    catch {
        Write-Error "Failed to build ${Name}: $($_.Exception.Message)"
        return $false
    }
    finally {
        Pop-Location
    }
}

# Check prerequisites
Write-Info "Checking prerequisites..."

$Prerequisites = @{
    "Python" = { python --version }
    "Node.js" = { node --version }
    "Java" = { java --version }
    "Maven" = { mvn --version }
    "CMake" = { cmake --version }
    ".NET" = { dotnet --version }
    "Rust" = { cargo --version }
}

$MissingPrereqs = @()
foreach ($prereq in $Prerequisites.Keys) {
    try {
        & $Prerequisites[$prereq] | Out-Null
        Write-Success "$prereq found"
    }
    catch {
        Write-Warning "$prereq not found or not in PATH"
        $MissingPrereqs += $prereq
    }
}

if ($MissingPrereqs.Count -gt 0) {
    Write-Error "Missing prerequisites: $($MissingPrereqs -join ', ')"
    Write-Info "Please install missing tools and ensure they're in your PATH"
    exit 1
}

# Build modules in dependency order
$BuildResults = @{}

# 1. Rust Knowledge Database (no dependencies)
$knowledgeParams = @{
    Name = "Knowledge Database"
    Path = "knowledge-rust"
    BuildScript = {
        if ($Clean) {
            cargo clean
        }
        if ($Configuration -eq "Release") {
            cargo build --release
        } else {
            cargo build
        }
    }
    TestScript = {
        cargo test
    }
}
$BuildResults["knowledge"] = Invoke-ModuleBuild @knowledgeParams

# 2. C++ Speech Recognition (no dependencies)
$speechParams = @{
    Name = "Speech Recognition"
    Path = "speech-cpp"
    BuildScript = {
        $BuildDir = "build"
        if ($Clean -and (Test-Path $BuildDir)) {
            Remove-Item -Recurse -Force $BuildDir
        }
        if (-not (Test-Path $BuildDir)) {
            New-Item -ItemType Directory $BuildDir
        }
        Set-Location $BuildDir
        
        $CMakeConfig = if ($Configuration -eq "Release") { "Release" } else { "Debug" }
        cmake .. -DCMAKE_BUILD_TYPE=$CMakeConfig
        cmake --build . --config $CMakeConfig
    }
}
$BuildResults["speech"] = Invoke-ModuleBuild @speechParams

# 3. Java Text-to-Speech (no dependencies)
$ttsParams = @{
    Name = "Text-to-Speech"
    Path = "tts-java"
    BuildScript = {
        if ($Clean) {
            mvn clean
        }
        if ($Configuration -eq "Release") {
            mvn package -DskipTests=$SkipTests
        } else {
            mvn compile -DskipTests=$SkipTests
        }
    }
    TestScript = {
        mvn test
    }
}
$BuildResults["tts"] = Invoke-ModuleBuild @ttsParams

# 4. C# System Control (no dependencies)
$systemParams = @{
    Name = "System Control"
    Path = "system-csharp"
    BuildScript = {
        if ($Clean) {
            dotnet clean
        }
        $BuildConfig = if ($Configuration -eq "Release") { "Release" } else { "Debug" }
        dotnet build --configuration $BuildConfig
    }
    TestScript = {
        dotnet test --configuration $Configuration
    }
}
$BuildResults["system"] = Invoke-ModuleBuild @systemParams

# 5. JavaScript Dashboard (no dependencies on other modules for build)
$dashboardParams = @{
    Name = "Dashboard"
    Path = "dashboard-js"
    BuildScript = {
        if ($Clean -and (Test-Path "node_modules")) {
            Remove-Item -Recurse -Force "node_modules"
        }
        if ($Clean -and (Test-Path "public/js")) {
            Remove-Item -Recurse -Force "public/js"
        }
        
        npm install
        if ($Configuration -eq "Release") {
            npm run build
        } else {
            npm run build:dev
        }
    }
    TestScript = {
        npm test
    }
}
$BuildResults["dashboard"] = Invoke-ModuleBuild @dashboardParams

# 6. Python Core Orchestrator (depends on other modules being built)
$coreParams = @{
    Name = "Core Orchestrator"
    Path = "core-python"
    BuildScript = {
        # Create virtual environment if it doesn't exist
        if (-not (Test-Path "venv")) {
            Write-Info "Creating Python virtual environment..."
            python -m venv venv
        }
        
        # Activate virtual environment
        $VenvActivate = if ($IsWindows -or $env:OS -eq "Windows_NT") { 
            "venv\Scripts\Activate.ps1"
        } else { 
            "venv/bin/activate"
        }
        
        if (Test-Path $VenvActivate) {
            & $VenvActivate
        }
        
        # Install dependencies
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
    }
    TestScript = {
        if (Test-Path "venv\Scripts\Activate.ps1") {
            & "venv\Scripts\Activate.ps1"
        }
        python -m pytest tests/ -v
    }
}
$BuildResults["core"] = Invoke-ModuleBuild @coreParams

# Summary
Write-Info "Build Summary:"
Write-Info "============="

$SuccessCount = 0
$FailureCount = 0

foreach ($module in $BuildResults.Keys) {
    if ($BuildResults[$module]) {
        Write-Success "${module}: SUCCESS"
        $SuccessCount++
    } else {
        Write-Error "${module}: FAILED"
        $FailureCount++
    }
}

Write-Info "Total: $($SuccessCount + $FailureCount) modules"
Write-Success "Successful: $SuccessCount"
if ($FailureCount -gt 0) {
    Write-Error "Failed: $FailureCount"
}

# Create run scripts
Write-Info "Creating run scripts..."
$RunScript = @"
# SaraAI 5.0 - Run All Modules
# Generated by build script

Write-Host "🤖 Starting SaraAI 5.0..." -ForegroundColor Cyan

# Start all modules in background
Start-Process -FilePath "knowledge-rust\target\$($Configuration.ToLower())\knowledge-server.exe" -WorkingDirectory "knowledge-rust"
Start-Process -FilePath "speech-cpp\build\$Configuration\saraai_speech.exe" -WorkingDirectory "speech-cpp" 
Start-Process -FilePath "java" -ArgumentList "-jar", "tts-java\target\saraai-tts-1.0.0.jar" -WorkingDirectory "."
Start-Process -FilePath "dotnet" -ArgumentList "run", "--project", "system-csharp\SystemControl.csproj" -WorkingDirectory "."
Start-Process -FilePath "node" -ArgumentList "dashboard-js\src\app.js" -WorkingDirectory "."

# Wait a moment for services to start
Start-Sleep -Seconds 5

# Start the orchestrator (main process)
Set-Location core-python
if (Test-Path "venv\Scripts\Activate.ps1") {
    & "venv\Scripts\Activate.ps1"
}
python main.py
"@

$RunScript | Out-File -FilePath (Join-Path $ProjectRoot "run.ps1") -Encoding UTF8

Write-Success "Build complete! Use 'run.ps1' to start all modules."

if ($FailureCount -gt 0) {
    exit 1
} else {
    exit 0
}
