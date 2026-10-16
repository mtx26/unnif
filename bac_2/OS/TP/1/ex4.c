#include <stdio.h>
#include <stdlib.h>

void delete(char string[], char target)
{
    int i = 0;
    int j = 0;

    while (string[i] != '\0')
    {
        if (string[i] != target)
        {
            string[j] = string[i];
            j++;
        }

        i++;
    }

    string[j] = '\0';
}

int main(int argc, char *argv[])
{
    delete(argv[1], argv[2][0]);
    printf("%s", argv[1]);
    return 0;
}
