source constants.sh

if [[ ! -e "$SERVEUR_PIPE" ]]; then
    echo "Please start serveur.sh first"
    exit 1
fi

CLIENT_PID=$$
# The PID lets the server route the reply to this client's FIFO.
CLIENT_PIPE="${CLIENT_PIPE_PREFIX}${CLIENT_PID}"

if [[ ! -e "$CLIENT_PIPE" ]]; then
  mkfifo "$CLIENT_PIPE"
fi