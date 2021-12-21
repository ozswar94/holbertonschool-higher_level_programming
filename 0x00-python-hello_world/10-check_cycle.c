#include <stdio.h>
#include "lists.h"

/**
* check_cycle - mock interview
* @list: list
*
* Return: 1 if cycle else 0
*/
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list == NULL)
		return (0);

	tmp = list->next;
	while (tmp->next != NULL)
	{
		if (list == tmp)
			return (1);

		tmp = tmp->next;
	}
	return (0);
}
