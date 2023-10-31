#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long n = get_long("Number: ");

    int first_sum = 0;

    int second_sum = 0;

    for (int power1 = 1; power1 <= 16; power1 += 2)
    {
        second_sum += n % (long) pow(10, power1) / (long) pow(10, (power1 - 1));
    }

    for (int power2 = 2; power2 <= 16; power2 += 2)
    {
        int x = (n % (long) pow(10, power2) / (long) pow(10, (power2 - 1))) * 2;

        first_sum += x % 10;
        first_sum += (x % 100) / 10;

        }


    int final_sum = second_sum + first_sum;

    int lengh = 0;

    long cd = n;

    while( cd > 0 )
    {
        cd /= 10;
        lengh ++;
    }

    int cdnum = n;

    for(int a = 0; a < lengh - 1; a++)
    {
        cdnum /= 10;
    }

    printf("%i %i ",cdnum,lengh);

    if (final_sum % 10 != 0)
    {
        if ((lengh == 13) & (cdnum == 4))
        {
            printf("VISA\n")
        }
        else if ((lengh == 16) & (cdnum == 4))
        {
            printf("VISA\n")
        }
        else if ((lengh == 15) & (cdnum == 3))
        {
            printf("AMEX\n")
        }
        else if ((lengh == 13) & (cdnum == 4))
        {
            printf("VISA\n")
        }
    }
    else
    {
        printf("VISA\n");
    }

}
