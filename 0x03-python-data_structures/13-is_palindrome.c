#include "lists.h"

/**
 * is_palindrome - Function to check if a singly linked list is a palindrome.
 * @head: head pointer.
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int	is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int i = 0, j = 0, k = 0, l = 0;
	int *array;

	tmp = *head;
	array = NULL;
	if (*head == NULL)
		return (1);
	while (tmp != NULL)
	{
		tmp = tmp->next;
		i++;
	}
	array = malloc(sizeof(int) * i);
	if (array == NULL)
		return (0);
	tmp = *head;
	i = 0;
	while (tmp != NULL)
	{
		array[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	j = i - 1;
	while (k < j)
	{
		if (array[k] != array[j])
			l++;
		k++;
		j--;
	}
	free(array);
	if (l == 0)
		return (1);
	else
		return (0);
}
