#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //gEtTinG HeIghT FroM ThE USer
    int height;

    do
    {
        height = get_int("Height:");
    }
    while((hight < 1) or (height > 8))

    int count = 1;

    for(count, count <= height, count ++)
    {
        for(a, a < hight - count, a++)
        {
            printf(" ");
        }

        for(a, a < count, a++)
        {
            printf("#");
        }

        printf("  ");

        for(a, a < count, a++)
        {
            printf("#");
        }


    }
}
