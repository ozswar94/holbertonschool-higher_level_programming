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

	node = (listint_t *)malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	if (*head == NULL)
	{
		node->next = NULL;
		*head = node;
		return (node);
	}
	prev_node = *head;
	next_node = (*head)->next;

	if (prev_node->n > number)
	{
		node->next = prev_node;
		*head = node;
		return (node);
	}
	while (prev_node->next != NULL)
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
	prev_node->next = node;
	node->next = next_node;
	return (node);
}
