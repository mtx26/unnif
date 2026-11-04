source "$(dirname "$0")/constants.sh"

echo "$$" > "$SERVER_PID_FILE"

cleanup() {
    rm -- "$SERVEUR_PIPE" "$SERVER_PID_FILE"

    if [[ -d "$PIPE_DIR" ]]; then
        rmdir -- "$PIPE_DIR"
    fi
    
}

trap cleanup EXIT
trap 'exit 0' TERM

max=$1
n=$(shuf -i "0-$max" -n 1)


while true; do
    message=$(head -n 1 "$SERVEUR_PIPE")
    client_pid=${message%|*}
    proposition=${message#*|}

    echo "Soumission de ${proposition}."

    CLIENT_PIPE="${CLIENT_PIPE_PREFIX}${client_pid}"
    result=""
    if (( proposition == n )); then
        result="egal"
    elif (( proposition < n )); then
        result="upper"
    else
        result="lower"
    fi
    echo "$result" > "$CLIENT_PIPE"
done
