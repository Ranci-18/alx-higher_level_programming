#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 *insert_node - inserts a new value in a sorted linked list
 *@head: pointer to head pointer
 *@number: value to be inserted
 *
 *
 *Return: address to new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *prev = NULL;

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (current != NULL)
	{
		if (current->n > number)
			break;
		prev = current;
		current = current->next;
	}

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = current;
		if (current == *head)
			*head = new;
		else
			prev->next = new;

	}
	return (new);
}
