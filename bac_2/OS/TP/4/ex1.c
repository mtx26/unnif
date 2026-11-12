#include <stdio.h> // printf(..)
#include <stdlib.h> // exit(..), EXIT_SUCCESS
#include <unistd.h> // fork(), getpid()

int main(int argc, char *argv[]) {
    int x = 100;
    pid_t fvalue = fork();
    if (fvalue != 0) { // Parent process
        x -= 10;
        printf("[%ld] x = %d\n", getpid(), x);
    } else { // Child process
        x += 20;
        printf("[%ld] x = %d\n", getpid(), x);
    }
    exit(EXIT_SUCCESS);
}