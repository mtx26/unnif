#include <stdlib.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    int *n = malloc(sizeof(int));
    *n = 10;
    printf("%d\n", *n);
    free(n);
    return 0;
}
