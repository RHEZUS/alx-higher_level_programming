#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *stack_top = NULL;


	while (fast != NULL && fast->next != NULL)
	{
		listint_t *newNode = malloc(sizeof(listint_t));

		if (newNode == NULL)
			return (0);

		newNode->n = slow->n;
		newNode->next = stack_top;
		stack_top = newNode;

		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
		slow = slow->next;

	while (slow != NULL)
	{

		if (stack_top == NULL || stack_top->n != slow->n)
			return (0);
		listint_t *temp = stack_top;

		stack_top = stack_top->next;
		free(temp);
		slow = slow->next;
	}
	return (1);
}
