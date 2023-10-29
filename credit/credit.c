#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{

    long n = get_long("Number: ");

    int first_sum = 0;

    int second_sum = 0;

    int final_sum = second_sum + first_sum;

    if (final_sum % 10 == 0)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
