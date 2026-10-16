#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void print_type_stats() {
    int int_n = sizeof(int);
    int unsigned_int_n = sizeof(unsigned int);
    int short_n = sizeof(short);
    int long_n = sizeof(long);
    int float_n = sizeof(float);
    int double_n = sizeof(double);
    printf("int a %i octets et peut contenir de %f valeur\n", int_n, pow(2, int_n*8));
    printf("unsigned int a %i octets et peut contenir de %f valeur\n", unsigned_int_n, pow(2, unsigned_int_n*8));
    printf("short a %i octets et peut contenir de %f valeur\n", short_n, pow(2, short_n*8));
    printf("long a %i octets et peut contenir de %f valeur\n", long_n, pow(2, long_n*8));
    printf("float a %i octets et peut contenir de %f valeur\n", float_n, pow(2, float_n*8));
    printf("double a %i octets et peut contenir de %f valeur\n", double_n, pow(2, double_n*8));
};

int main(int argc, char const *argv[])
{
    print_type_stats();
    return 0;
}

