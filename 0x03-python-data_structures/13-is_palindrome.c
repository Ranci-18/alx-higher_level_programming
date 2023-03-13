#include "lists.h"
/**
 *reverse_l_list - reverses a linked list
 *@h: head node of linked list
 *
 *
 *
 *Return: nothing
 */
void reverse_l_list(listint_t **h)
{
	listint_t *current;
	listint_t *prev;
	listint_t *next;

	current = *h;
	prev = NULL;
	next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*h = prev;
}
/**
 *compare - compares linked list values
 *@h1: head node of first linked list
 *@h2: head node of second linked list
 *
 *Return: 1 if equal, 0 if not
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp1;
	listint_t *tmp2;

	tmp1 = h1;
	tmp2 = h2;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}
	if (tmp1 == NULL && tmp2 == NULL)
	{
		return (1);
	}
	return (0);
}
/**
 *is_palindrome - checks if linked list is palindrome
 *@head: pointer to head pointer
 *
 *
 *
 *Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *middle;
	int i;

	slow = fast = prev_slow = *head;
	middle = NULL;
	i = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}
		scn_half = slow;
		prev_slow->next = NULL;
		reverse_l_list(&scn_half);
		i = compare(*head, scn_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}
	return (i);
}
