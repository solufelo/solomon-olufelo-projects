@echo off
title Laurier Mobile Study Hub Server (Port 8080)
echo ========================================================
echo   LAURIER FALL 2026 - MOBILE STUDY HUB SERVER
echo   Solomon Olufelo (210729170)
echo ========================================================
echo.
echo Starting local web server on port 8080...
echo Phone Access URL: http://192.168.8.235:8080
echo.
cd /d "C:\Users\Administrator\.gemini\antigravity\scratch\mobile_server"
python -m http.server 8080 --bind 0.0.0.0
pause
