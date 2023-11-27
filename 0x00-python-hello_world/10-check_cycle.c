#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the list in which cycle is checked
 * Return: 0 if no cycle and 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	if (list == NULL && list->next == NULL)
		return(0);
	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}
	return (0);
}

