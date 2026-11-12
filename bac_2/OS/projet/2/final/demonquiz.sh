source "$(dirname "$0")/constants.sh"

# verif si le nombre d'argument = 1 et si c'est un nombre
if (( $# != 1 )) || [[ ! $1 =~ ^[0-9]+$ ]] ; then
    echo "Entrez un max valide"
    exit 1
fi

max=$1;
# verif que 1 < max < 32767
if (( max < 1 || max > 32767 )); then
    echo "max doit être entre 1 et 32767"
    exit 1
fi

# creatioon du dossier pour les pipe
if [[ ! -e "$PIPE_DIR" ]]; then
    mkdir "$PIPE_DIR"
fi

# creation du pipe serveur
if ! mkfifo "$SERVEUR_PIPE"; then
    echo "Impossible de créer le pipe : un serveur tourne peut-être déjà."
    exit 1
fi
# lancement du serveur
exec bash "$(dirname "$0")/server.sh" "$max"

