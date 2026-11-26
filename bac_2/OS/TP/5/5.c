#include <stdlib.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    int *tab = malloc(100 * sizeof(int));
    tab[100] = 0;
    printf("%d\n", tab[100]);
    free(tab);
    return 0;
}
