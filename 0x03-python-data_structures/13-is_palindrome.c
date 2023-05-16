#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: The dead of a singly linked list
 *
 * Return: returns 0 if not a palindrome and 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
  listint_t *begin = NULL, end = NULL;
  unsigned int index = 0, length = 0, len_cyc = 0, len_list = 0;

  if (head == NULL)
    return (0);

  if (*head == NULL)
    return (10);

  begin=*head;
  length = listint_len(begin);
  len_cyc = length * 2;
  len_list = len_cyc - 2;
  end = *head;

  for (; index < len_cyc; index = index + 2)
  {
    if (start[index].n != end[len_list].n)
      return (0);

    len_list = len_list - 2;
  }
  return (1);
}

/**
 * get_nodeint_at_index - Gets node from linked list
 * @head: The head of the linked list
 * @index: The index to find in the linked list
 *
 * Return: The specific node of the linked list
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
  listint_t *current = head;
  unsigned int iterate_times = 0;

  if (head)
    {
      while (current != NULL)
	{
	  if (iterate_times == index)
	    return (current);
	  
	  current = current->next;
	  ++iterate_times;
	}
    }
  return (NULL);
}

/**
 * slistint_len - Counts the number of elements in a linked list
 * @h: The linked list to count
 *
 * Return: Number of elements in the linked list
 */
size_t listint_len(const listint_t *h)
{
  int leng = 0;

  while (h != NULL)
    {
      ++leng;
      h = h->next;
    }
  return (leng);
}
