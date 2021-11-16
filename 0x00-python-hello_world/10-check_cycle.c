#include "lists.h"

/**
  * check_cycle - checks if a linked list has a cycle
  * @list: head of the list
  * Return: 1 if there is a cycle, 0 otherwise
  */
int check_cycle(listint_t *list)
{
	listint_t *fast_p, *slow_p;
	fast_p = slow_p = list;
	while (fast_p)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
			return (1);
	}

	return (0);
}
