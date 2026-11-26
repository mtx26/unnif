#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    char speed = 125;
    int progress = 0;
    int num = 0;
    while (progress < 1000) {
        progress += speed;
        num++;
        printf("New progress: %i\n", progress);
        if (num == 5) {
            num = 0;
            speed += 10;
            printf("Level-Up! Speed increased by 10!\n");
        }
        sleep(1);
    }
    printf("Finished!\n");
    return EXIT_SUCCESS;
}
