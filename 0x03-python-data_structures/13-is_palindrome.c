#include "lists.h"

/**
 * reverse_list - reverse a linked list
 * @head: pointer to the starting node
 * Return: pointer to the new head
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *curr = head;
	listint_t *next;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the list
 * Return: 1 or 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *first_half = *head;
	listint_t *second_half;

	if (!*head || (*head)->next == 0)
		return (1);
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (!fast)
		slow = slow->next;
	second_half = reverse_list(slow);
	while (second_half)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}
