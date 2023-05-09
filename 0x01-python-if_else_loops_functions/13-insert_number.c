#include "lists.h"

/**
 * insert_node - function in C that inserts a number into
 * a sorted singly linked list.
 * @head: Pointer to the Head Pointer.
 * @number: A number to insert.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;
	listint_t *prev;

	new_node = NULL;
	current = NULL;
	prev = NULL;
	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current != NULL)
	{
		if (current->n > number)
		{
			if (prev == NULL)
			{
				new_node->next = current;
				*head = new_node;
				return (new_node);
			}
			prev->next = new_node;
			new_node->next = current;
			return (new_node);
		}
		prev = current;
		current = current->next;
	}
	prev->next = new_node;
	return (new_node);
}
