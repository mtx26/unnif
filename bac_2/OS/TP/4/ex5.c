#include <stdio.h> // printf(..)
#include <stdlib.h> // exit(..), EXIT_SUCCESS
#include <unistd.h> // fork(), getpid()
#include <sys/wait.h> // wait(..)

int main(int argc, char *argv[]) {
    pid_t fvalue = fork();
    if (fvalue != 0) { // Parent process
        int status;
        wait(&status);
        printf("goodbye\n");
    } else { // Child process
        printf("hello\n");
    }
    exit(EXIT_SUCCESS);
}