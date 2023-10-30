#include "lists.h"

/**
 * check_cycle - check if there's a cycle in the linked list
 * @list: pointer to list
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *p1 = list;
	listint_t *p2 = list;

	while (p1 && p2 && p2->next)
	{
		p1 = p1->next;
		p2 = p2->next->next;
		if (p1 == p2)
			return (1);
	}
	return (0);
}
