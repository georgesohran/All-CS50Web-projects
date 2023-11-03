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

}

int count_letters(string txt)
{

    int count = 0

    for(int i = 0; i < strlen(txt); i++)
    {
        if (txt[i])
    }
}


