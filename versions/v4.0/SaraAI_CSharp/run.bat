@echo off
echo 🤖 Sara AI v4.0 - Voice-Controlled PC Assistant
echo ================================================
echo.

echo 🔄 Building Sara AI...
dotnet build

if %ERRORLEVEL% neq 0 (
    echo ❌ Build failed! Please check the errors above.
    pause
    exit /b 1
)

echo ✅ Build successful!
echo.

echo 🚀 Starting Sara AI...
echo Say "Hey Sara" to wake up the assistant!
echo Press Ctrl+C or 'Q' in the application to quit.
echo.

dotnet run

pause
