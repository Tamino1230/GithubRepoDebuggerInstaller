REM starting file

@echo off
    echo Installing Python packages...
    pip install requests
    echo Installation complete.

    timeout 4
    echo -
python mainDebugger.py
pause

echo you can close this window now.

pause