# Attention, pas d'espaces autour du =
# Dossier où stocker les pipes nommés
PIPE_DIR="./localpipe"

# "$nomvar" crée une chaîne de caractères où $nomvar est remplacé par le contenu de la variable nomvar
# Pipe nommé pour envoyer un message à serveur
CLIENT_PIPE_PREFIX="$PIPE_DIR/client"

# Pipe nommé pour envoyer un message à client
SERVEUR_PIPE="$PIPE_DIR/serveur"

SERVER_PID_FILE="$PIPE_DIR/serveur.pid"
