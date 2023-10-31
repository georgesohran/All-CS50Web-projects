#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long n = get_long("Number: ");

    int first_sum = 0;

    int second_sum = 0;

    for (int power1 = 1; power1 <= 8; power1 += 2)
    {
        second_sum += n % (long) pow(10, power1) / (long) pow(10, (power1 - 1));
    }

    for (int power2 = 2; power2 <= 8; power2 += 2)
    {
        int x = (n % (long) pow(10, power2) / (long) pow(10, (power2 - 1))) * 2;

        first_sum += x % 10;
        first_sum += (x % 100) / 10;

        }


    int final_sum = second_sum + first_sum;

    printf(" %i ", first_sum);

    if (final_sum % 10 != 0)
    {
        printf("INVALID\n");
    }
    else
    {
        printf("VISA\n");
    }

}
