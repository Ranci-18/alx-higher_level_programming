#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 *check_cycle: checks if a linked list has a cycle
 *@list: the first node
 *
 *
 *Return: 0 if there is no cycle, 1 if the is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *backward_node = list;
	listint_t *forward_node = list->next;

	if (list == NULL)
		return (0);

	while (forward_node != NULL && forward_node->next != NULL)
	{
		if (backward_node == forward_node)
		{
			return (1);
		}
		backward_node = backward_node->next;
		forward_node = forward_node->next->next;
	}

	return (0);
}
