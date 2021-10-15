#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 문제에서 설명하는대로,
// 오른쪽에서 봤을때 보이는 오름차순의 개수를 구하면 된다.

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

int		main(void)
{
	t_stack	stack;
	int		n;
	int		ans;
	int		temp;

	scanf("%*d");
	memset(&stack, 0, sizeof(stack));
	while (scanf("%d", &n) != EOF)
		push(&stack, n);
	ans = 0;
	n = -1;
	while (size(&stack))
	{
		temp = top(&stack);
		if (temp > n)
		{
			n = temp;
			ans++;
		}
		pop(&stack);
	}
	printf("%d", ans);
	return (0);
}