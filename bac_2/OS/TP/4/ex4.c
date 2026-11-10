#include <stdio.h> // printf(..)
#include <stdlib.h> // exit(..), EXIT_SUCCESS
#include <unistd.h> // fork(), getpid()
#include <sys/wait.h> // wait(..)

int main(int argc, char *argv[]) {
    pid_t fvalue = fork();
    if (fvalue != 0) { // Parent process
        int status;
        pid_t w = wait(&status);
        printf("[parent %ld] wait() = %ld (enfant = %ld), status = %d\n",
               (long) getpid(), (long) w, (long) fvalue, WEXITSTATUS(status));
    } else { // Child process
        pid_t w = wait(NULL); // pas d'enfant à attendre
        printf("[enfant %ld] wait() = %ld\n", (long) getpid(), (long) w);
        exit(42);
    }
    exit(EXIT_SUCCESS);
}