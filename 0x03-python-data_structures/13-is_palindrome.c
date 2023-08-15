#include "lists.h"
#include <stdio.h>

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
	while (second != NULL && first != NULL && first->next != NULL)
	{
		second = second->next;
		first = first->next->next;
	}
	second = reverse_list(&second);
	first = *head;
	while (first != NULL && second != NULL)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = second->next;
	}
	return (1);
}

/**
 * reverse_list - reverses the linked list
 * @head: a pointer
 * Return: integer
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *next = *head, *pre = NULL;

	while ((*head) != NULL)
	{
		next = *head->next;
		*head->next = pre;
		pre = *head;
		*head = next;
	}
	*head = pre
	return (*head);
}
