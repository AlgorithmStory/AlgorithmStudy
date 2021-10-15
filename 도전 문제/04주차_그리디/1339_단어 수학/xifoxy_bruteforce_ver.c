#include <stdio.h>

// 단어들을 메모 해뒀다가,
// 모든 경우를 다 구하면 된다.

int		n;
int		cnt;
int		dp[26];
char	key[26];
char	check[26];
char	visit[26];
char	num[11][10];

int	max(int a, int b) { return (a > b ? a : b); }

int	getsum()
{
	char	*iter;
	int		ret;
	int		sum;

	ret = 0;
	for (int i = 0; i < n; ++i)
	{
		sum = 0;
		iter = *(num + i);
		while (*iter)
			sum = sum * 10 + *(dp + (*(iter++) - 'A'));
		ret += sum;
	}
	return (ret);
}

int	sol(int depth, int next, int size)
{
	const int	ch = *(key + depth) - 'A';
	int			ret;

	if (depth == size)
		return (getsum());
	ret = -1;
	for (int i = next; i < 10; ++i)
	{
		if (*(visit + i))
			continue ;
		*(dp + ch) = i;
		*(visit + i) = 1;
		ret = max(ret, sol(depth + 1, next + 1, size));
		*(visit + i) = 0;
	}
	for (int i = 0; i < next; ++i)
	{
		if (*(visit + i))
			continue ;
		*(dp + ch) = i;
		*(visit + i) = 1;
		ret = max(ret, sol(depth + 1, next + 1, size));
		*(visit + i) = 0;
	}
	return (ret);
}

int	main(void)
{
	char	*iter;

	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%s", *(num + i));
		iter = *(num + i);
		while (*iter)
		{
			if (!*(check + *iter - 'A'))
			{
				*(check + *iter - 'A') = 1;
				*(key + cnt++) = *iter;
			}
			++iter;
		}
	}
	printf("%d\n", sol(0, 0, cnt));
	return (0);
}
