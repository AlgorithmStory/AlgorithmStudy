#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// 예쁘게 잘 뒤집으면 된다.

typedef struct		s_node
{
	int				num;
	struct s_node	*next;
}					g_node;

typedef struct		s_stack
{
	int				size;
	struct s_node 	*iter;
}					t_stack;

int		top(t_stack *stack)
{
	return (stack->size ? stack->iter->num : -1);
}

int		empty(t_stack *stack)
{
	return (!stack->size);
}

int		size(t_stack *stack)
{
	return (stack->size);
}

int		pop(t_stack *stack)
{
	int		ret;
	g_node	*node;

	if (stack->size)
	{
		ret = stack->iter->num;
		node = stack->iter;
		stack->iter = stack->iter->next;
		ret = node->num;
		free(node);
		node = NULL;
		stack->size--;
	}
	else
		ret = -1;
	return (ret);
}

void	push(t_stack *stack, int num)
{
	g_node	*node;

	node = (g_node *)malloc(sizeof(node));
	node->num = num;
	node->next = stack->iter;
	stack->iter = node;
	stack->size++;
	return ;
}

void	reverse(char *msg, char *iter)
{
	static t_stack	stack;
	char *temp = iter;

	while (*msg)
	{
		if (isspace(*msg))
			*(iter++) = *(msg++);
		else
		{
			while (*msg && !isspace(*msg))
			{
				push(&stack, *msg);
				++msg;
			}
			while (size(&stack))
				*(iter++) = pop(&stack);
		}
	}
	while (size(&stack))
		*(iter++) = pop(&stack);
	return ;
}

int		main(void)
{
	char	str[1005];
	int		n;
	char	*ans;
	int		len;

	memset(str, 0, sizeof(str));
	scanf("%d\n", &n);
	while (gets(str))
	{
		len = strlen(str);
		ans = (char *)malloc(len + 1);
		*(ans + len) = '\0';
		reverse(str, ans);
		puts(ans);
		free(ans);
	}
	return (0);
}
