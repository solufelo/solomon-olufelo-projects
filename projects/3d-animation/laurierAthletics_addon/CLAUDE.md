# Claude Assistant Guide - Laurier Athletics Videoboard Addon

## Context & SSOT
- Root Knowledge Hub: [[../../VAULT_INDEX.md|Root Vault Index]]
- Local Status: [[PROJECT_STATUS.md|Local Status]]
- Version: `v3.4.0` (Production Release)
- Blender Target: 5.2.1 LTS

## Validation & Testing
```powershell
# Run validation suite
& "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --python "test_addon.py"

# Quick syntax check
& "C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -m py_compile blender_addon/golden_hawks_shuffle_addon.py
```

## Production Constraints
1. **Broadcast Sandwich**: Kicker (+Y=+0.58m), Hero (Y=0.00m), Sponsor (-Y=-0.58m) pitched at 61.74°.
2. **Centered Exits**: No asymmetric rightward tilt. Exits are centered with X=0.0 and rot_z=0.0°.
3. **Timesheet**: Log all hours in [[LAURIER_TIMESHEET_LOG.md|LAURIER_TIMESHEET_LOG.md]] ($19.03/hr, 40h/wk cap).
