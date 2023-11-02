#include <cs50.h>
#include <stdio.h>
#include <string.h>



int main(void)
{
    string text = get_string("Text:");

    int cer_count = 0;
    int word_count = 0;
    int sentence_count = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122))
        {
            cer_count ++;
        }
        else if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            sentence_count ++;
            word_count ++;
        }
        else if (text[i] == 32 && text[i - 1] != 33 && text[i - 1] != 46 && text[i - 1] != 63)
        {
            word_count ++;
        }
    }

    float L = ((float) cer_count / (float)word_count) * 100;

    float S = ((float) sentence_count / (float)word_count) * 100;

    int res = 0.0588 * L - 0.296 * S - 15.8;

    //printf("%i %i %i ... %f %f\n", cer_count, word_count, sentence_count, L, S );

    if (res > 16)
    {
        printf("Grade 16+\n");
    }
    else if (res < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", res);
    }

}


