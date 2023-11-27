#include "lists.h"

int check_cycle(list_t *list)
{
	list_t *hare = list;
	list_t *tortoise = list;

	if (list == NULL && list->next == NULL)
		return (0);
	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return(1);
	}

	return (0);
}
