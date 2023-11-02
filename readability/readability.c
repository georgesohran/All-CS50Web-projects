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
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            sentence_count ++;
            word_count ++;
        }
        if (text[i] == 32)
        {
            word_count ++;
        }

    printf("%i %i %i /n", cer_count, word_count, sentence_count);

    }

}


