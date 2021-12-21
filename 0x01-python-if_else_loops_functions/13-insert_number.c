#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node
	listint_t *next_node;
	listint_t *prev_node;

	node = (listint_t *)malloc(sizeof(listint_t))
	if (node == NULL)
		return (NULL);

	node->n = number;

	prev_node = *head;
	next_node = (*head)->next;
	while (prev_node!= NULL)
	{
		if (prev_node->next->n > number)
		{
			
		}
	}
}
