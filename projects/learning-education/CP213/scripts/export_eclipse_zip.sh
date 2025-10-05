#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <project_name> <output_zip_path>" >&2
  exit 1
fi
project_name="$1"
output_zip="$2"
workspace_root="$(cd "$(dirname "$0")/.." && pwd)/workspace"
project_dir="$workspace_root/$project_name"
if [ ! -d "$project_dir" ]; then
  echo "Project not found: $project_dir" >&2
  exit 2
fi
(
  cd "$workspace_root"
  zip -r -q "$output_zip" "$project_name" \
    -x "*/.git/*" "*/target/*" "*/bin/*" "*/.metadata/*"
)
echo "Exported $project_name -> $output_zip"
