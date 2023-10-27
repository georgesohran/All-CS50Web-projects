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
    while((height < 1) || (height > 8));



    for(int count = 1; count <= height; count ++)
    {
        for(int a = 0; a < height - count; a++)
        {
            printf(" ");
        }

        for(int a = 0; a < count; a++)
        {
            printf("#");
        }

        printf("  ");

        for(int a = 0; a < count; a++)
        {
            printf("#");
        }
        printf("\n");

    }
}
