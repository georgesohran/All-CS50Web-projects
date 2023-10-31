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

    long visa = n;
    long mstr = n;
    long amex = n;

    while(visa >= 10)
    {
        visa /= 10;
    }
    while(mstr >= 100000000000000)
    {
        mstr /= 100000000000000;
    }
    while(amex >= 10000000000000)
    {
        amex /= 10000000000000;
    }

    if (final_sum % 10 != 0)
    {
        printf("INVALID\n");
    }
    else
    {
        if ((lengh == 13) & (visa == 4))
        {
            printf("VISA\n");
        }
        else if ((lengh == 16) & (visa == 4))
        {
            printf("VISA\n");
        }
        else if ((lengh == 15) & (amex == 34 || amex == 37))
        {
            printf("AMEX\n");
        }
        else if ((lengh == 16) & (mstr == 51 || mstr == 52 || mstr == 53 || mstr == 54 || mstr == 55))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }

}
