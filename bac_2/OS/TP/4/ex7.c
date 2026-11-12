#include <stdio.h> // printf(..)
#include <stdlib.h> // exit(..), EXIT_SUCCESS
#include <unistd.h> // execl(..), fork()
#include <sys/types.h> // pid_t
#include <sys/wait.h> // wait(..)

int main(int argc, char *argv[]) {
    pid_t fvalue = fork();
    if (fvalue != 0) { // Parent process
        wait(NULL);
        printf("Message après ls\n");
        exit(EXIT_SUCCESS);
    } else { // Child process
        execl("/bin/ls", "ls",(char *) NULL);
        perror("execl"); // seulement si execl échoue
        exit(EXIT_FAILURE);
    }
}