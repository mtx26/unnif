#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    for (int j = 1; j < argc; j++) {

        FILE *file = fopen(argv[j], "r");

        if (file == NULL) {
            fprintf(stderr, "ucat: cannot open file\n");
            return EXIT_FAILURE;
        }

        int c;
        long debut = ftell(file);
        while ((c = fgetc(file)) != EOF) {
            if (c != '\n') {
                long debut = ftell(file);
            }
        }

        fclose(file);
    }

    return EXIT_SUCCESS;
}
