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

	while (1)
	{
		*first = *first->next->next;
		if (*first->next == NULL)
			start_second = *second->next, break;
		if (*first == NULL)
			start_second = *second->next, break;
		*second = *second->next;
	}
	*second->next = NULL;
}
