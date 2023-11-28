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
	listint_t *prev = *head;
	listint_t *next = *head;

	next = next->next;
	new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	while (next != NULL && next->next != NULL)
	{
		if (next->n >= number || next->next == NULL)
		{
			prev->next = new_node;
			new_node->next = next;
			break;
		}
		prev = next;
		next = next->next;
	}
	if (head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
	}
	return (*head);
}
