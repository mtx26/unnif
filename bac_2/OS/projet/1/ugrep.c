#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        //si il n'y a pas de fichier
        fprintf(stderr, "ugrep: searchterm [file ...]\n");
        return 1;
    }
    int stdin_input = argc == 2;
    for (int j = stdin_input ? 1 : 2; j < argc; j++) {
        FILE *file;
        if (stdin_input) {
            file = tmpfile();
            if (file == NULL) { // test si le fichier est bien creer
                fprintf(stderr, "ugrep: cannot create temporary file\n");
                return EXIT_FAILURE;
            }
            int input;
            while ((input = fgetc(stdin)) != EOF) { // ecrit tant que c'est pas la fin
                if (fputc(input, file) == EOF) { //ecriture dans le fichier et erreur si pas ecrit
                    fprintf(stderr, "ugrep: cannot write to temporary file\n");
                    fclose(file);
                    return EXIT_FAILURE;
                }
            }
            rewind(file);
        } else {
            file = fopen(argv[j], "r");
        }
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
        long debut = 0;// début de la ligne actuelle
        //début de l'essaie si premiere lettre correspond. ftell permet d'avoir l'indice de l'endroit ou on se trouve
        while ((c = fgetc(file)) != EOF) {
            if (c == '\n') {
                debut = ftell(file);
            }
            long reprise = ftell(file);  // position après le caractère courant
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
                fseek(file, reprise, SEEK_SET);
            }
        }
        fclose(file);
    }
    return EXIT_SUCCESS;
}