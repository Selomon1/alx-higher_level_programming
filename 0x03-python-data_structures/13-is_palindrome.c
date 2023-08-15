#include "lists.h"

/**
 * is_palindrome - a function that checks if the list is palindrome or not.
 * @head: a pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *first = *head;
	listint_t *second = *head;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	while (1)
	{
		first = first->next->next;
		if (first->next == NULL)
			start_second = second->next, break;
		if (first == NULL)
			start_second = second->next, break;
		second = second->next;
	}
	second->next = NULL;
}

/**
 * reverse_list - reverses the linked list
 * @head: a pointer
 * Return: integer
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *cur, *pre = NULL, *next;
	cur = head;

	while (cur != NULL)
	{
		next = cur->next;
		cur->next = pre;
		pre = cur;
		cur = next;
	}
	return (pre);
}