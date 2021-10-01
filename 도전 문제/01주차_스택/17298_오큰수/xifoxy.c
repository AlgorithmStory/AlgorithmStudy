#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 큰녀석이 나오면 갱신해주면 된다.
// 그리고 다시 큐에 집어넣으면 된다 끝.

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

#define MAX 1000002

int arr[MAX];
int ans[MAX];
int n;
int		main(void)
{
	t_stack	stack;

	memset(&stack, 0, sizeof(t_stack));
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i)
		scanf("%d", &arr[i]);

	for (int i = n; i >= 1; --i)
	{
		ans[i] = -1;
		while(top(&stack) < arr[i] && size(&stack))
			pop(&stack);
		if (size(&stack))
			ans[i] = top(&stack);
		if (top(&stack) > arr[i] || !size(&stack))
			push(&stack, arr[i]);
	}
	for(int i = 1; i <= n; ++i)
		printf("%d ", ans[i]);
	return (0);
}