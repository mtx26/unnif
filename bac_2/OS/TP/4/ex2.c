#include <stdio.h> // printf(..)
#include <stdlib.h> // exit(..), EXIT_SUCCESS
#include <unistd.h> // fork(), getpid()

int main(int argc, char *argv[]) {
    pid_t fvalue = fork();
    if (fvalue != 0) { // Parent process
        printf("[%ld] parent\n", getpid());
    } else { // Child process
        close(STDOUT_FILENO);
        printf("[%ld] child\n", getpid());
    }
    exit(EXIT_SUCCESS);
}