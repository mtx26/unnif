# Attention, pas d'espaces autour du =
# Dossier où stocker les pipes nommés
PIPE_DIR="./localpipe"

# "$nomvar" crée une chaîne de caractères où $nomvar est remplacé par le contenu de la variable nomvar
# Pipe nommé pour envoyer un message à ping
PING_PIPE="$PIPE_DIR/ping"

# Pipe nommé pour envoyer un message à pong
PONG_PIPE="$PIPE_DIR/pong"
