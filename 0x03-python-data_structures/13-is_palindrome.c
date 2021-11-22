#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
  * is_palindrome - checks if a linked list is a palindrome
  * @head: the list
  * Return: 1 if list is palindrome, 0 otherwise
  */
int is_palindrome(listint_t **head)
{
	listint_t *curr, **arr;
	ssize_t len, i, pal;

	if (head == NULL)
		return (0);
	curr = *head;
	len = 0;
	while (curr)
	{
		len++;
		curr = curr->next;
	}

	arr = malloc(sizeof(listint_t) * len);
	if (arr == NULL)
		return (0);

	curr = *head;
	for (i = len - 1; i >= 0; i--)
	{
		arr[i] = curr;
		curr = curr->next;
	}

	curr = *head;
	for (i = 0; i < len; i++)
	{
		pal = 1;
		if (arr[i]->n != curr->n)
		{
			pal = 0;
			break;
		}
		curr = curr->next;
	}

	free(arr);
	if (pal == 1)
		return (1);
	return (0);
}
