#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <ProjectName> [outDir=exports]" >&2
  exit 1
fi
PN="$1"
OUTDIR="${2:-exports}"
mkdir -p "$OUTDIR"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
"$HERE/scripts/export_eclipse_zip.sh" "$PN" "$HERE/$OUTDIR/${PN}.zip"
echo "Exported to $OUTDIR/${PN}.zip"
