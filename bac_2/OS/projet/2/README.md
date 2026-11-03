# Sandbox du projet 2

`sandbox.sh` ouvre trois terminaux dans une copie temporaire du dossier courant.
Les fichiers originaux sont visibles en lecture seule sous `/src`. Les tests se
font dans `/mnt` et les changements faits dans cette copie sont perdus à la
fermeture de la sandbox.

## Prérequis

Sur Linux, installer Bubblewrap (version 0.9.0 ou ultérieure) et tmux. Sous
Ubuntu :

```bash
sudo apt install bubblewrap tmux
```

## Lancement

Depuis le dossier du projet 2 :

```bash
cd /chemin/vers/bac_2/OS/projet/2
bash ./sandbox.sh
```

Lancez les programmes à tester dans les différents terminaux de la sandbox.
Pour changer de terminal, appuyez sur `Ctrl-b`, relâchez les touches, puis
appuyez sur une flèche. Pour terminer, arrêtez les programmes puis tapez `exit`
dans chacun des terminaux.

Modifiez et enregistrez toujours vos fichiers dans votre éditeur, en dehors de
la sandbox, puis relancez-la pour tester la nouvelle copie. Ne conservez pas de
travail uniquement sous `/mnt`, car il disparaît à la fermeture.

## Ubuntu 24.04 et AppArmor

Si Bubblewrap refuse de démarrer à cause de la restriction du réseau imposée par
AppArmor, une possibilité est d'ajouter `--share-net \` juste après
`--unshare-all \` dans `sandbox.sh`, puis de relancer le script. Cela partage le
réseau de l'hôte au lieu de l'isoler et réduit donc le niveau d'isolation de la
sandbox. N'activez cette option que si le lancement normal échoue et que vous
acceptez ce compromis.
