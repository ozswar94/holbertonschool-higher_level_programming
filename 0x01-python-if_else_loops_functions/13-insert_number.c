#include "lists.h"
#include <stdlib.h>

/**
* insert_node - insert node in list
* @head: head of list
* @number: n in list
* Return: new node otherwise NULL
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *next_node;
	listint_t *prev_node;

	if (head == NULL || *head == NULL)
		return (NULL);

	node = (listint_t *)malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;

	prev_node = *head;
	next_node = (*head)->next;
	while (prev_node != NULL)
	{
		if (next_node->n > number)
		{
			node->next = next_node;
			prev_node->next = node;
			return (node);
		}
		if (next_node != NULL)
			next_node = next_node->next;
		prev_node = prev_node->next;
	}
	return (node);
}
