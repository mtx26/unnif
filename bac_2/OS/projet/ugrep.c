#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        //si il n'y a pas de fichier
        fprintf(stderr, "ugrep: searchterm [file ...]\n");
        return 1;
    }
    for (int j = 2; j < argc; j++) {
        FILE *file = fopen(argv[j], "r");
        if (file == NULL) {
            //si le fichier est null
            fprintf(stderr, "ugrep: cannot open file\n");
            return EXIT_FAILURE;
        }

        if (argv[1][0] == '\0') {
            //verifie si le mot rechercher est une chaine vide 
            int c;
            while ((c = fgetc(file)) != EOF) {
                putchar(c);
            }
            fclose(file);
            continue;
        }

        int c;
        long debut;// début de la ligne actuelle
        //début de l'essaie si premiere lettre correspond. ftell permet d'avoir l'indice de l'endroit ou on se trouve
        long depart = ftell(file);
        while ((c = fgetc(file)) != EOF) {
            if (c == '\n') {
                debut = ftell(file);
            }
            int n = 0;
            int flag = 1;
            while (argv[1][n] != '\0') {
                if (argv[1][n] == c || (argv[1][n] == '?' && c != '\n' && c != EOF)) {
                    c = fgetc(file); //passe au caractère suivant dans le fichier
                    n++; //avance de caractère dans la chaine a chercher
                } else {
                    flag = 0;
                    break;
                }
            }
            //si flag = 1 ca veut dire que le mot a été trouvé 
            if (flag == 1) {
                fseek(file, debut, SEEK_SET); //retourne la ou la phrase a commencer pour l'écrire
                while ((c = fgetc(file)) != EOF) {
                    putchar(c);
                    if (c == '\n') {
                        break;
                    }
                }
                debut = ftell(file); //on passe a la ligne suivante pour continuer le parcour
            } else {
                //si le flag est a 0 le mot n'est pas trouvé donc on retourne au caractère juste apres le debut de la recherche du mot donc depart + 1
                fseek(file, depart + 1, SEEK_SET);
            }
            depart = ftell(file);//on attribut le nouveau depart
        }
        fclose(file);
    }
    return EXIT_SUCCESS;
}