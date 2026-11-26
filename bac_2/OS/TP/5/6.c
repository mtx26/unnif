#include <stdlib.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    int *tab = malloc(100 * sizeof(int));
    tab[99] = 10;
    free(tab);
    printf("%d\n", tab[100]);
    return 0;
}   
