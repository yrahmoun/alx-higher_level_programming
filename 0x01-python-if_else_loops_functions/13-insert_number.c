#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * insert_node - inserts a node in the linked list
 * @head: pointer to list
 * @number: list data
 * Return: pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curr;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	if (!*head || (*head)->n > number)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	curr = *head;
	while (curr->next && curr->next->n < number)
		curr = curr->next;
	new->n = number;
	new->next = curr->next;
	curr->next = new;
	return (new);
}
