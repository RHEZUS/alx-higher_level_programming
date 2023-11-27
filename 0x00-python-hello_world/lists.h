#ifndef __HEADER__
#define __HEADER__

#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int data;
    struct Node *next;
} list_t;

int check_cycle(list_t *list);

#endif
