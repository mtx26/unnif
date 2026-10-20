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
        while ((c = fgetc(file)) != EOF) {
            putchar(c);
        }

        fclose(file);
    }

    return EXIT_SUCCESS;
}