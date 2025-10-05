#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <input_zip_path> [project_name_override]" >&2
  exit 1
fi
input_zip="$1"
name_override="${2:-}"
workspace_root="$(cd "$(dirname "$0")/.." && pwd)/workspace"
mkdir -p "$workspace_root"
tmp_dir="$(mktemp -d)"
unzip -q "$input_zip" -d "$tmp_dir"
project_path="$(find "$tmp_dir" -maxdepth 2 -type f -name .project -printf '%h\n' | head -n1)"
if [ -z "$project_path" ]; then
  echo "No Eclipse .project found in zip." >&2
  rm -rf "$tmp_dir"
  exit 2
fi
src_dir="$project_path"
base_name="$(basename "$src_dir")"
project_name="${name_override:-$base_name}"
rm -rf "$workspace_root/$project_name"
cp -a "$src_dir" "$workspace_root/$project_name"
rm -rf "$tmp_dir"
echo "Imported project to $workspace_root/$project_name"
