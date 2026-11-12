source "$(dirname "$0")/constants.sh"

# verif si le pid est toujours conservé
if [[ ! -r "$SERVER_PID_FILE" ]]; then
    echo "Erreur : fichier PID introuvable. Le serveur est-il lancé ?" >&2
    exit 1
fi

# recup le pid du serveur
read -r server_pid < "$SERVER_PID_FILE"

# verif si le server exist tourjours
if ! kill -0 "$server_pid" 2>/dev/null; then
    echo "Erreur : le processus serveur n'existe plus." >&2
    exit 1
fi

# kill le server
kill -TERM "$server_pid" || {
    echo "Erreur : impossible d'arrêter le serveur." >&2
    exit 1
}