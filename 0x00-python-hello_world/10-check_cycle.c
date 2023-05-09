#include "lists.h"
/**
 * check_cycle - function in C that checks if a
 * singly linked list has a cycle in it.
 * @list : list to check.
 * Return: 0 if no cycle detected 1 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);  /* cycle detected */
		}
	}

	return (0);  /* no cycle detected */
}
