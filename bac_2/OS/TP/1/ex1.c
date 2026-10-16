#include <stdio.h>
#include <stdlib.h>

unsigned int string_length(char string[]) {
    int i = 0;
    while (string[i] != '\0')
    {
        i++;
    }
    return i;
}
int main(int argc, char *argv[])
{
    printf("%i\n", string_length(argv[1]));
}
