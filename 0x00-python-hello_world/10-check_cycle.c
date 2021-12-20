#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t **tmp;

	if (list == NULL)
		return (0);

	tmp = &list;
	while ((*tmp)->next != NULL)
	{
		if (&list == tmp)
			return (1);
		*tmp = (*tmp)->next;
		printf("%d\n", (*tmp)->n);
	}
	return (0);
}
