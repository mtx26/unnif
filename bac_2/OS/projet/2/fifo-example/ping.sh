#!/usr/bin/env bash

# On lit les constantes
source constants.sh

# Attention aux espaces après et avant les [[ ]]
# Si pong_pipe n'existe pas, pong.sh n'est pas lancé et on ne peut rien faire
# -e teste si un fichier existe, le ! inverse le test (en python: not)
if [[ ! -e "$PONG_PIPE" ]]; then
    echo "Please start pong.sh first"
    exit 1
fi

# S'il n'existe pas, on crée le pipe nommé
if [[ ! -e "$PING_PIPE" ]]; then
  mkfifo "$PING_PIPE"
fi

# Boucle infinie
while true; do
    # On lit une ligne en console et on stocke le texte dans la variable text
    # Le -r permet de conserver les backslashes "\" littéralement
    read -r text
    # On envoie le texte vers pong_pipe
    echo "$text" > "$PONG_PIPE"
    # Si le texte est quit, on stoppe
    if [[ "$text" == "quit" ]]; then
        break
    fi
    # On lit la première ligne de ping_pipe (bloque tant qu'on n'a pas de ligne)
    reply=$(head -n 1 "$PING_PIPE")
    # On affiche la réponse de pong
    echo "$reply"
done

# Si ping_pipe existait, on le supprime avec confirmation (option -i)
if [[ -e "$PING_PIPE" ]]; then
  rm -i "$PING_PIPE"
fi
