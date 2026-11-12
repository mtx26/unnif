source "$(dirname "$0")/constants.sh"
#recup le pid
echo "$$" > "$SERVER_PID_FILE"

#clean final pour pouvoir recommencé
cleanup() {
    rm -- "$SERVEUR_PIPE" "$SERVER_PID_FILE"

	if [[ -d "$PIPE_DIR" ]]; then
        rmdir -- "$PIPE_DIR" 2>/dev/null
    fi
}
#lancement du cleanup lors de l'arret du serveur quand exit est declanché
trap cleanup EXIT
trap 'exit 0' TERM


max=$1
# generer nombre aléatoire
n=$(shuf -i "0-$max" -n 1)


while true; do
    #lire dernière ligne dans le pipe
    IFS= read -r message < "$SERVEUR_PIPE"

    #recup pid et proposition (pid|prop)
    client_pid=${message%|*}
    proposition=${message#*|}

    echo "Soumission de ${proposition}."

    #genere l'accés au pipe du client
    CLIENT_PIPE="${CLIENT_PIPE_PREFIX}${client_pid}"
    result=""
    # verif la proposition
    if (( proposition == n )); then
        result="egal"
    elif (( proposition < n )); then
        result="upper"
    else
        result="lower"
    fi
    # on ecrit dans le pipe du client corespondant
    echo "$result" > "$CLIENT_PIPE"
done
