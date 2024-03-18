#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	static listint_t *tmp;

	if (cur == NULL)
	{
		return (1);
	}
	if (tmp == NULL)
	{
		tmp = cur;
	}
	if (is_palindrome(&cur->next) && tmp->n == cur->n)
	{
		tmp = tmp->next;
		return (1);
	}
	else
	{
		return (0);
	}
}
