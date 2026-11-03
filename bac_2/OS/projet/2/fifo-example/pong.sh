#!/usr/bin/env bash

# On lit les constantes
source constants.sh

# Si le dossier n'existe pas, on le crée
if [[ ! -e "$PIPE_DIR" ]]; then
  mkdir "$PIPE_DIR"
fi

# S'il existait mais n'est pas un dossier, erreur
if [[ ! -d "$PIPE_DIR" ]]; then
  echo "$PIPE_DIR devrait être un dossier"
  exit 1
fi

# Si le pipe nommé n'existe pas, on le crée
if [[ ! -e "$PONG_PIPE" ]]; then
  mkfifo "$PONG_PIPE"
fi

# Boucle infinie
while true; do
  # On lit la première ligne de pong_pipe (bloque tant qu'on n'a pas de ligne)
  text=$(head -n 1 "$PONG_PIPE")
  # Si le message est quit, on stoppe.
  if [[ "$text" == "quit" ]]; then
    break
  # Si le message est ping, on envoie pong, sinon on envoie wrong à ping.sh
  elif [[ "$text" == "ping" ]]; then
    echo "pong" >"$PING_PIPE"
  else
    echo "wrong" >"$PING_PIPE"
  fi
done

# Si pong_pipe existait, on le supprime avec confirmation (option -i)
if [[ -e "$PONG_PIPE" ]]; then
  rm -i "$PONG_PIPE"
fi

# Si pipe_dir existait et qu'il est vide, on le supprime
# rmdir ne supprime que des dossiers vide et ne peut pas supprimer un fichier
if [[ -d "$PIPE_DIR" ]]; then
  rmdir "$PIPE_DIR"
fi
