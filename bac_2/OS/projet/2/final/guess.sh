source "$(dirname "$0")/constants.sh"

#recup du pid
CLIENT_PID=$$
# The PID lets the server route the reply to this client's FIFO.
#gen le pid final du client
CLIENT_PIPE="${CLIENT_PIPE_PREFIX}${CLIENT_PID}"

# cleanup final
cleanup() {
    rm -- "$CLIENT_PIPE"

	if [[ -d "$PIPE_DIR" ]]; then
        rmdir -- "$PIPE_DIR" 2>/dev/null
    fi
}

#lancement du cleanup lors de l'arret du serveur quand exit est declanché
trap cleanup EXIT
trap 'exit 0' TERM

# creation du pipe si il n'existe pas
if [[ ! -e "$CLIENT_PIPE" ]]; then
  	mkfifo "$CLIENT_PIPE"
fi

essais=0

while true; do
	printf "Introduire une proposition de nombre (-1 pour terminer) :\n"
	# read le chiffre entrée
	read -r proposition

	# arrét du guess
	if [[ "$proposition" == "-1" ]]; then
        echo "Abandon après $essais essai(s)."
        break
    fi
	# verif si c'est un nombre
	if [[ ! $proposition =~ ^[0-9]+$ ]]; then
		echo "Erreur : entrez un nombre entier positif ou -1 pour abandonner." >&2
		continue
	fi

	((essais += 1))

	#verif si le serveur tourne toujour
	if [[ ! -e "$SERVEUR_PIPE" ]]; then
		echo "Erreur : le serveur de quiz ne fonctionne plus correctement." >&2
		exit 1
	fi
	#verif si le serveur tourne toujour meme si le pipe exist toujour(probleme de supresission)
	read -r server_pid < "$SERVER_PID_FILE"
	if ! kill -0 "$server_pid" 2>/dev/null; then
		echo "Erreur : le serveur de quiz ne fonctionne plus correctement." >&2
		exit 1
	fi

	#envois de (pid|prop) au pipe du serveur
	echo "$CLIENT_PID|$proposition" > "$SERVEUR_PIPE"

	# reception de la reponse
	reponse=$(head -n 1 "$CLIENT_PIPE")

	#analise de la reponse du serveur
	if [[ "$reponse" == "egal" ]]; then
        echo "Félicitations, vous avez trouvé en $essais tentatives !"
        break
    elif [[ "$reponse" == "upper" ]]; then
		echo "Le nombre à deviner est plus grand que $proposition, réessayez !"
	elif [[ "$reponse" == "lower" ]]; then
		echo "Le nombre à deviner est plus petit que $proposition, réessayez !"
	fi
done