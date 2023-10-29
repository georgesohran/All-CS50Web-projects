#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{

    long n = get_long("Number: ");

    int first_sum = 0

    int second_sum = 0

    for(power, power >= 16, power++)
    {
        if power % 2 == 0
        {
            int x = n % pow(10 , power)

            if (10 < x) & (x > 100)
            {
                first_sum += x % 10
                first_sum += x % 100
            }

            else
            {
                first_sum += x
            }
        }
        else
        {
            second_sum += n % pow(10 , power)
        }
    }



    if
    {

    }
}
