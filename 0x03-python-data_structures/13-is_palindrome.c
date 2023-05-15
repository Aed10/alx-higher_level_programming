#include "lists.h"

/**
 * is_palindrome - Function to check if a singly linked list is a palindrome.
 * @head: head pointer.
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t	*tmp;
	int i = 0, j = 0, k = 0, l = 0;
	int arr[10000];

	tmp = *head;
	if (!head || !*head)
		return (1);
	while (tmp)
	{
		arr[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	j = i - 1;
	while (k < j)
	{
		if (arr[k] != arr[j])
			l++;
		k++;
		j--;
	}
	if (l == 0)
		return (1);
	else
		return (0);
}
