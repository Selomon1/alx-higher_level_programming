#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singlg linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description - singly list node structure
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t

int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_noseint(listint_t **head, const int n);
void fee_listint(listint_t *head);

#endif /* LISTS */
