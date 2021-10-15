#include <stdio.h>

// 분해합 문제 특성상 n을 넘을 수 없기 떄문에,
// n까지 순회하면서 분해합을 만들어보면 된다.

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