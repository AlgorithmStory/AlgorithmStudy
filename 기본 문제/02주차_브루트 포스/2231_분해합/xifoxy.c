#include <stdio.h>

int	solution(int num)
{
	int	ret;

	ret = num;
	while (num)
	{
		ret += (num % 10);
		num /= 10;
	}
	return (ret);
}

int	main(void)
{
	int	n;
	int	ans;

	ans = -1;
	scanf("%d", &n);
	for(int i = 1; i <= n; ++i)
	{
		if (solution(i) == n)
		{
			ans = i;
			break;
		}
	}
	printf("%d\n", ans == -1 ? 0 : ans);
	return (0);
}