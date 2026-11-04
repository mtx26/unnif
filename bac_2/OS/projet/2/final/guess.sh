source "$(dirname "$0")/constants.sh"

CLIENT_PID=$$
# The PID lets the server route the reply to this client's FIFO.
CLIENT_PIPE="${CLIENT_PIPE_PREFIX}${CLIENT_PID}"

cleanup() {
    rm -- "$CLIENT_PIPE"

	if [[ -d "$PIPE_DIR" ]]; then
        rmdir -- "$PIPE_DIR"
    fi
}

trap cleanup EXIT
trap 'exit 0' TERM

if [[ ! -e "$CLIENT_PIPE" ]]; then
  	mkfifo "$CLIENT_PIPE"
fi

essais=0

while true; do
	printf "Introduire une proposition de nombre (-1 pour terminer) :\n"
	read -r proposition
	if [[ "$proposition" == "-1" ]]; then
        echo "Abandon après $essais essai(s)."
        break
    fi
	if [[ ! $proposition =~ ^[0-9]+$ ]]; then
		echo "Erreur : entrez un nombre entier positif ou -1 pour abandonner." >&2
		continue
	fi

	((essais += 1))

	if [[ ! -e "$SERVEUR_PIPE" ]]; then
		echo "Erreur : le serveur de quiz ne fonctionne plus correctement." >&2
		exit 1
	fi

	read -r server_pid < "$SERVER_PID_FILE"
	if ! kill -0 "$server_pid" 2>/dev/null; then
		echo "Erreur : le serveur de quiz ne fonctionne plus." >&2
		exit 1
	fi

	echo "$CLIENT_PID|$proposition" > "$SERVEUR_PIPE"
	reponse=$(head -n 1 "$CLIENT_PIPE")

	if [[ "$reponse" == "egal" ]]; then
        echo "Félicitations, vous avez trouvé en $essais tentatives !"
        break
    elif [[ "$reponse" == "upper" ]]; then
		echo "Le nombre à deviner est plus grand que $proposition, réessayez !"
	elif [[ "$reponse" == "lower" ]]; then
		echo "Le nombre à deviner est plus petit que $proposition, réessayez !"
	fi
done