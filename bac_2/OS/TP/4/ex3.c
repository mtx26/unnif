#include <stdio.h> // printf(..)
#include <stdlib.h> // exit(..), EXIT_SUCCESS
#include <unistd.h> // fork(), getpid()

int main(int argc, char *argv[]) {
    FILE *f = fopen("output.txt", "w");
    pid_t fvalue = fork();
    if (fvalue != 0) { // Parent process
        for (int i = 0; i < 5; i++) {
            fprintf(f, "hello parent(%d)\n", i);
            //fflush(f); // retirer pour voir le comportement sans flush
        }
    } else { // Child process
        for (int i = 0; i < 5; i++) {

            fprintf(f, "hello child(%d)\n", i);
            //fflush(f);
        }
    }
    fclose(f);
    exit(EXIT_SUCCESS);
}