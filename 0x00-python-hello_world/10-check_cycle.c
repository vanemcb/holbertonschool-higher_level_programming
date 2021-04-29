#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: head pointer
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *next_1pos = list, *next_2pos = list;

	while (next_1pos && next_2pos && next_2pos->next)
	{
		next_1pos = next_1pos->next;
		next_2pos = next_2pos->next->next;
		if (next_1pos == next_2pos)
			return (1);
	}
	return (0);
}
