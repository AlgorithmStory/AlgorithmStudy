#include <stdio.h>

// 내림차순으로 정렬해서 큰거부터 빼주면 된다.

# define swap(x, y, temp) ( (temp) = (x), (x) = (y), (y) = (temp) )

int	coin[10];
int	n;
int	k;

void	sorting(int *arr, int size)
{
	int	temp;

	for (int i = 0; i < size; ++i)
		for (int j = i + 1; j < size; ++j)
			if (*(arr + i) < *(arr + j))
				swap(*(arr + i), *(arr + j), temp);
	return ;
}

int		main(void)
{
	int	ans;

	scanf("%d %d", &n, &k);
	for (int i = 0; i < n; ++i)
		scanf("%d", (coin + i));
	sorting(coin, n);
	ans = 0;
	for (int i = 0; i < n; ++i)
	{
		ans += (k / *(coin + i));
		k %= *(coin + i);
	}
	printf("%d\n", ans);
	return (0);
}
