#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 생각외로 간단하다.
// 주어진 수열을 스택에 넣었다 뺴면서 만들 수 있는 수열이면 만들면 된다.

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
	char	*ans;
	int		*arr;
	int		*it_i;
	char	*it_c;
	int		idx;

	scanf("%d", &n);
	ans = (char *)malloc(sizeof(char) * n * 2 + 1);
	it_c = ans;
	arr = (int *)malloc(sizeof(int) * n);
	it_i = arr;
	memset(&stack, 0, sizeof(t_stack));
	memset(ans, 0, sizeof(char));
	memset(arr, 0, sizeof(int));
	for (int i = 0; i < n; ++i)
		scanf("%d", arr + i);
	
	idx = 1;
	while (idx <= n)
	{
		if (*it_i == top(&stack))
		{
			pop(&stack);
			*(it_c++) = '-';
			it_i++;
			continue ;
		}
		push(&stack, idx++);
		*(it_c++) = '+';
	}
	while (size(&stack))
	{
		if (*it_i != top(&stack))
			break;
		pop(&stack);
		*(it_c++) = '-';
		it_i++;
	}
	if (size(&stack))
		puts("NO");
	else
	{
		for(int i = 0; ans[i]; ++i)
		{
			putchar(ans[i]);
			puts("");
		}
	}
	return (0);
}
