#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 스택을 직접 구현하고,
// 요구사항에 맞게 command가 들어오면
// 명령어를 비교 후 실행한다.

#define PUSH	"push"
#define POP		"pop"
#define SIZE	"size"
#define EMPTY	"empty"
#define TOP		"top"

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

void	push(t_stack *stack)
{
	g_node	*node;
	int		num;

	scanf("%d", &num);
	node = (g_node *)malloc(sizeof(node));
	node->num = num;
	node->next = stack->iter;
	stack->iter = node;
	stack->size++;
	return ;
}

void	st(char *cmd, t_stack *stack)
{
	if (!strcmp(PUSH, cmd))
		push(stack);
	else if(!strcmp(POP, cmd))
		printf("%d\n", pop(stack));
	else if(!strcmp(SIZE, cmd))
		printf("%d\n", size(stack));
	else if(!strcmp(EMPTY, cmd))
		printf("%d\n", empty(stack));
	else if(!strcmp(TOP, cmd))
		printf("%d\n", top(stack));
	return ;
}

int		main(void)
{
	t_stack stack;
	int n;
	char cmd[11];

	memset(&stack, 0, sizeof(t_stack));
	scanf("%d", &n);
	while (n--)
	{
		scanf("%s", cmd);
		st(cmd, &stack);
	}
	return (0);
}
