#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
int list[1000000];
long move = 1, i;
listint_t *forward;

	if (head == NULL)
		return (1);
	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);

	forward = *head, move = 0;
	while (forward != NULL)
		list[move] = forward->n, forward = forward->next, move++;

	for (i = 0; i < (move / 2); i++)
	{
		if (list[i] != list[move - i - 1])
			return (0);
	}

	return (1);
}
