#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int main(void)
{

    int n;

    do
    {
        n = get_long("Number: ");
    }
    while(!isallnum(n) , !(len(n) == 16))


}
