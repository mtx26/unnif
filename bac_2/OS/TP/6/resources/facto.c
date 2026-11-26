#include <stdio.h>
#include <stdlib.h>

int factorial_rec(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial_rec(n - 1);
    }
}

unsigned int fibo_rec(unsigned int n, unsigned int *mem) {
    if (mem[n] > 0) {
        return mem[n];
    } else {
        unsigned int res = fibo_rec(n - 1, mem) + fibo_rec(n - 2, mem);
        mem[n] = res;
        return res;
    }
}

int fibo(unsigned int n) {
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    unsigned int *mem = calloc(n + 1, sizeof(unsigned int));
    mem[0] = 0;
    mem[1] = 1;
    return fibo_rec(n, mem);
}

int main(int argc, char *argv[])
{
    int n = 10;
    printf("factorial of %i = %i\n", n, factorial_rec(n));
    printf("fibo of %i = %i\n", n, fibo(n));
    return EXIT_SUCCESS;
}
