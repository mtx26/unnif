#include <stdio.h>
#include <stdlib.h>

unsigned int count_char_occurrences(char string[], char target) {
    int i = 0;
    int counter = 0;
    while (string[i] != '\0')
    {
        if (string[i] == target)
        {
            counter++;
        }
        i++;
    }
    return counter;
    
};

int main(int argc, char *argv[])
{
    printf("%i\n", count_char_occurrences(argv[1], argv[2][0]));
    return EXIT_SUCCESS;
}
