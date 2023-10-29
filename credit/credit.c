#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{

    long n = get_long("Number: ");

    int first_sum = 0;

    int second_sum = 0;

    for(int power = 0; power >= 16; power++)
    {
        if (power % 2 == 0)
        {
            long x = n % (long) pow(10 , power);
            // - n % (long) pow(10 , power-1)
            if ((10 < x) & (x > 100))
            {
                first_sum += x % 10;
                first_sum += x % 100 //- x % 10;
            }

            else
            {
                first_sum += x;
            }
        }
        else
        {
            second_sum += n % (long) pow(10 , power);
        }
    }

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
