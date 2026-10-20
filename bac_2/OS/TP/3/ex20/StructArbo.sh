#!/bin/bash
racine=$1
destination=$2

shopt -s nullglob dotglob

function copy {
    mkdir -p "$1"
}

function create_index {
    local source_courant=$1
    local destination_courante=$2
    local index="$destination_courante/index.txt"

    if [[ ! -r "$source_courant" || ! -x "$source_courant" ]]; then
        echo "ERROR: source directory is not accessible" > "$index"
        return
    fi

    local fichier_trouve=0
    : > "$index"
    for fichier in "$source_courant"/*; do
        if [[ -f "$fichier" && ! -L "$fichier" ]]; then
            fichier_trouve=1
            nom=$(basename -- "$fichier")
            taille=$(du -h -s -- "$fichier" | cut -f1)
            mime=$(file --mime-type -b -- "$fichier")
            printf '%s | %s | %s\n' "$nom" "$taille" "$mime" >> "$index"
        fi
    done
    if [[ "$fichier_trouve" -eq 0 ]]; then
        printf 'EMPTY' > "$index"
    fi
}

boucle() {
    local source_courant=$1
    local destination_courante=$2

    copy "$destination_courante"
    create_index "$source_courant" "$destination_courante"

    for dossier in "$source_courant"/*/; do
        if [[ -d "$dossier" ]]; then
            boucle "$dossier" "$destination_courante/$(basename "$dossier")"
        fi
    done
}

boucle "$racine" "$destination"