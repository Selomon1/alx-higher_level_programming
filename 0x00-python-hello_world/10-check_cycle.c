#include "lists.h"

/**
 * check_cycle - checck if a linked list has a cycle or not
 * @list: the head of the linked list
 * Return: 1 if the list has a cycle, or 0 if it doestn't have
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr1;
	listint_t *ptr2;

	if (!list)
		return (0);

	ptr1 = ptr2 = list;

	while (ptr2 && ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (1);
	}

	return (0);
}
