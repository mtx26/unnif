On a deux scripts Bash : `ping.sh` et `pong.sh`.

`pong.sh` agit comme un serveur et attend de recevoir un message sur son pipe nommé. Il se charge de créer le dossier qui contiendra les pipes nommés et de le supprimer ensuite. C'est lui qui doit être lancé en premier.

`ping.sh` agit comme un client. Il attend de recevoir du texte depuis le terminal et transmet le texte à `pong.sh`. Il doit être lancé après `pong.sh`.

Dans chacun des deux terminaux, placez-vous dans le même répertoire `fifo-example/`, qui contient les scripts et `constants.sh` :

```bash
cd /chemin/vers/fifo-example
```

Dans le premier terminal, lancez le serveur :

```bash
./pong.sh
```

Dans le second terminal, lancez le client :

```bash
./ping.sh
```

Si nécessaire, rendez les scripts exécutables avec `chmod u+x ping.sh pong.sh`.

On peut alors écrire du texte dans le terminal du client `ping.sh` et chaque ligne sera envoyée à `pong.sh`. Si on envoie "ping" à `pong.sh`, celui-ci répondra "pong". Sinon, il répondra "wrong". Pour terminer les programmes, envoyer "quit" à `ping.sh` qui va l'envoyer à `pong.sh` (qui se terminera) avant de se terminer lui-même. Les deux vont demander l'autorisation de supprimer leurs pipes nommés. Pour que `pong.sh` puisse supprimer le dossier, vide, contenant les pipes nommés, il faut d'abord permettre à `ping.sh` de supprimer le sien.

Les constantes (nom des pipes nommés et dossier les contenant) sont définies dans `constants.sh` afin que les deux scripts aient accès aux mêmes valeurs.

Cet exemple suppose un seul client et un arrêt avec `quit` ; les arrêts inattendus des processus ne sont pas gérés.
