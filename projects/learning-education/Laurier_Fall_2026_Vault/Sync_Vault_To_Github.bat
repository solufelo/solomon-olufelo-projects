@echo off
cd /d "C:\Users\Administrator\.gemini\antigravity\scratch\solomon-olufelo-projects"
echo ==============================================
echo SYNCING LAURIER FALL 2026 VAULT TO GITHUB...
echo ==============================================
git pull origin main
git add projects/learning-education/Laurier_Fall_2026_Vault
git commit -m "docs(vault): auto-sync school notes"
git push origin main
echo ==============================================
echo SYNC COMPLETE! NOTES ARE LIVE ON GITHUB.
echo ==============================================
pause
