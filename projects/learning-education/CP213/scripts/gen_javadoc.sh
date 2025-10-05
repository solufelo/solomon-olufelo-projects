#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <ProjectName>" >&2
  exit 1
fi
PN="$1"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/workspace/$PN/src"
OUT="$ROOT/workspace/$PN/javadoc"
mkdir -p "$OUT"
javadoc -d "$OUT" -sourcepath "$SRC" -subpackages cp213
echo "Javadoc generated at workspace/$PN/javadoc"
