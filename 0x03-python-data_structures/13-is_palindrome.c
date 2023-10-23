#include "lists.h"

/**
 * is_palindrome - palindrome list
 * @head: head of list
 * Return: 0 if it not a palindrome
 * and 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palindrome(head, *head));
}

/**
 * aux_palindrome - if list is a palindrome
 * @head: head of list
 * @end: end of list
 * Return: 0 or 1
 */
int aux_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
