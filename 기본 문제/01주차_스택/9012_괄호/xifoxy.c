#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 괄호 문제의 핵심은, 괄호의 페어가 맞아야 한다는것이다.
// 열리는 괄호는 스택에 담고, 닫히는 괄호가 들어올땐
// 스택에서 열린괄호를 빼준다.
// 스택에 괄호가 없는 상태에서 닫히는 괄호가 들어오거나,
// 솔루션이 끝난 후 괄호가 스택에 남아 있다면 fail이다.

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

int		sol(char *str)
{
	t_stack	stack;

	memset(&stack, 0, sizeof(stack));
	while (*str)
	{
		if (*str == '(')
			push(&stack, *str);
		else if (!size(&stack))
			return (1);
		else
			pop(&stack);
		++str;
	}
	return (size(&stack));
}

int		main(void)
{
	char	str[55];

	scanf("%*d");
	while (scanf("%s", str) != EOF)
	{
		if (sol(str))
			puts("NO");
		else
			puts("YES");
	}
	return (0);
}