#include "lists.h"

/**
 * check_cycle - check the cycle exist in a linked list
 * @list: the head of the linked list
 * Return: 1 if ther is or 0 if not 
 */

int check_cycle(listint_t *list)
{
	listint_t *first, *last;

	if(!list)
	{
		return (0);
	}

	last = first = list;
	while(last && first && first ->next)
	{
		last = last -> next;
		first = first -> next -> next;

		if(last == first)
		{
			return (1);
		}
	}
	return (0);
}
