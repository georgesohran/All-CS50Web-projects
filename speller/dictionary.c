// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26 * 26;

// Hash table
node *table[N];

//Number of words in dictionary
int wcount = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int indx = hash(word);

    node* cursor = table[indx];
    while(cursor != 0)
    {
        if(strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int asum = 0;

    for(int i = 0; i < strlen(word); i++)
    {
        asum += (toupper(word[i]) - atoi("A"));
    }

    return ((toupper(word[0]) - atoi("A")) * (toupper(word[1]) - atoi("A")) + asum) % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE* dictptr = fopen(dictionary,"r");
    if (dictptr == NULL)
    {
        return false;
    }

    char new_word[LENGTH + 1];

    while (fscanf(dictptr,"%s",new_word) != EOF)
    {
        int indx = hash(new_word);

        node* new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            return false;
        }
        strcpy(new_node->word, new_word);

        if (table[indx] == NULL)
        {
            new_node->next = NULL;
        }
        else
        {
            new_node->next = table[indx]->next;
        }
        table[indx] = new_node;

        wcount ++;
    }

    fclose(dictptr);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return wcount;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            node* cursor = table[i]->next;
            while(cursor != NULL)
            {
                node* temp_cursor = cursor;
                cursor = cursor->next;
                free(temp_cursor);
            }
            free(cursor);
        }

    }
    return false;
}


