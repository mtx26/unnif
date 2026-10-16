#include <stdio.h>
#include <stdlib.h>

void capitalize(char string[]) {

    int i = 0;
    while (string[i] != '\0')
    {
        string[i] = string[i] - 32;
        i++;
    }
};

int main(int argc, char *argv[])
{
    capitalize(argv[1]);
    printf("%s\n", argv[1]);
    return 0;
}


