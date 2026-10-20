#!/bin/bash
set -euo pipefail

repo_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)
volume=/Volumes/CIRCUITPY

if [[ ! -d "$volume" ]]; then
    echo "CIRCUITPY is not mounted at $volume" >&2
    exit 1
fi

if ! ls "$volume" >/dev/null 2>&1; then
    echo "Cannot access $volume. Allow cmux access to Removable Volumes in System Settings > Privacy & Security > Files & Folders." >&2
    exit 1
fi

if [[ ! -f "$volume/boot_out.txt" ]]; then
    echo "$volume does not look like a CircuitPython drive" >&2
    exit 1
fi

rsync -r --exclude='.git' --exclude='.DS_Store' "$repo_dir/" "$volume/"
sync
echo "Installed RP2040_Buttons to $volume"
