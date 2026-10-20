#!/bin/bash
shopt -s globstar nullglob
path=$1
dest=$2
mkdir -p "$dest"
shift
shift

function search {
    local ext=$1
    local file

    for file in "$path"/**/*; do
        if [[ -f "$file" && "$file" == *"$ext" ]]; then
            echo "$(basename "$file")"
            cp "$file" "$dest/"
        fi
    done
}

while [[ 1 == 1 ]];do
    for ext in "$@"; do
        search "$ext"
    done
    sleep 3
done

