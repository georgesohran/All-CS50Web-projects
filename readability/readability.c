#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text:");

    grade = get_grade(text);

}

int get_grade(string txt)
{
    int cer_count = 0;
    int word_count = 0;
    int sentence_count = 0;

    for (int i; i < strlen(txt); i++)
    {
        if ((txt[i] => 65 && txt[i] =< 90) || (txt[i] => 97 && txt[i] =< 122))
        {
            cer_count ++
        }
        if (txt[i] == "." || txt[i] == "?" || txt[i] == "!")
        {
            sentence_count ++
            word_count ++
        }
        if (txt[i] == " ")
        {
            word_count ++
        }
    printf("%i %i %i /n")
    }

}
