#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the list
 * @number: the number to  be added
 * Return: the sorted linked list or null
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *next = *head;

	new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (next == NULL || next->n >= number)
	{
		new_node->next = next;
		*head = new_node;
		return (new_node);
	}

	while (next && next->next && next->next->n < number)
	{
		next = next->next;
	}

	new_node->next = next->next;
	next->next = new_node;

	return (new_node);
}
