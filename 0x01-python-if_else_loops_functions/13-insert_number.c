#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Insert into a sorted linked llist
 * @head: pointer the head list
 * @number: number to insert
 * Return: address null or result
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *num, *temp, *previous;

	num = malloc(sizeof(listint_t));
	if (!num)
		return (NULL);
	num->n = number;
	if (*head == NULL)
	{
		num->next = NULL;
		*head =num;
		return (num);
	}
	if ((*head)->n > number)
	{
		num->next = *head;
		*head = num;
		return (num);
	}
	temp = *head;
	while (temp && temp->n < number)
	{
		previous = temp;
		temp = temp->next;
	}
	if (temp == NULL)
	{
		previous->next = num;
		num->next = NULL;
		return (num);
	}
	else
	{
		previous->next = num;
		num->next = temp;
		return (num);
	}
	return (NULL);
}
