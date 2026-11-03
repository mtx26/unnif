if (( $# != 1 )) || [[ ! $1 =~ ^[0-9]+$ ]] ; then
    echo "Entrez un max valide"
    exit 1
fi

max=$1;
if (( max < 1 || max > 32767 )); then
    echo "max doit être entre 1 et 32767"
    exit 1
fi

if ! mkfifo "$SERVEUR_PIPE"; then
    echo "Impossible de créer le pipe : un serveur tourne peut-être déjà."
    exit 1
fi

exec bash "$(dirname "$0")/serveur.sh" "$max"

