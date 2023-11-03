#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int count_letters(string txt);
int count_words(string txt);
int count_sentances(string txt);


int main(void)
{
    string text = get_string("Text:");

    int letter_count = count_letters(text);
    int word_count = count_words(text);
    int sentence_count = count_sentances(text);

    float L = round(((float) letter_count / (float) word_count) * 100);
    float S = ((float) sentence_count / (float) word_count) * 100;

    float index = 0.0588 * L - 0.296 * S - 15.8;

    printf("%i %i %i \n%f %f %f\n", letter_count, word_count, sentence_count, L, S, index);

}

int count_letters(string txt)
{
    int count = 0;

    for(int i = 0; i < strlen(txt); i++)
    {
        if ((txt[i] >= 97 && txt[i] <= 122) || (txt[i] >= 65 && txt[i] <= 90))
        {
            count ++;
        }
    }

    return(count);
}

int count_words(string txt)
{
    int count = 0;

    for(int i = 0; i < strlen(txt); i++)
    {
        if (!(txt[i] >= 97 && txt[i] <= 122) && !(txt[i] >= 65 && txt[i] <= 90) &&
            !(txt[i] == 39) && !(txt[i] == 45) &&
            ((txt[i-1] >= 97 && txt[i-1] <= 122) || (txt[i-1] >= 65 && txt[i-1] <= 90)))
        {
            count ++;
        }
    }

    return(count);
}

int count_sentances(string txt)
{
    int count = 0;

    for(int i = 0; i < strlen(txt); i++)
    {
        if (txt[i] == 33 || txt[i] == 46 || txt[i] == 63 )
        {
            count ++;
        }
    }

    return(count);
}


