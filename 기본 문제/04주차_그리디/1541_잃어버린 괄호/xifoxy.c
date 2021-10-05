#include <stdio.h>

// minus가 등장한 부분부터 모조리 다 빼주면 된다.

int		num[55];
char	oper[55];

int	main(void)
{
	int	idx;
	int	ans;
	int	minus;

	idx = 0;
	scanf("%d", (num + idx));
	while (scanf("%c ", (oper + idx++)) != EOF)
		scanf("%d", (num + idx));
	ans = *(num);
	minus = 0;
	for (int i = 1; i < idx; ++i)
	{
		if (*(oper + i - 1) == '-')
			minus = 1;
		if (minus)
			ans -= *(num + i);
		else
			ans += *(num + i);
	}
	printf("%d\n", ans);
	return (0);
}