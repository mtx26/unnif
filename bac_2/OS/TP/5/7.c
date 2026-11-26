#include <stdlib.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    int *tab = malloc(100 * sizeof(int));
    free(&tab[50]);
    return 0;
}
