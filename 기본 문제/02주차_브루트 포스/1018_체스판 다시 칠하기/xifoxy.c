#include <stdio.h>
#include <stdlib.h>

// 그냥 판때기 크기만큼 검사해보면 끝난다.

int	solution(int x, int y, char **map)
{
	int		ret;

	ret = 0;
	for (int i = x; i < x + 8; ++i)
	{
		for (int j = y; j < y + 8; ++j)
		{
			if ((i + j) % 2 == 0 && *(*(map + i) + j) != 'W')
				ret++;
			if ((i + j) % 2 && *(*(map + i) + j) != 'B')
				ret++;
		}
	}
	ret = ret > 64 - ret ? 64 - ret : ret;
	return (ret);
}

int	main(void)
{
	char	**map;
	int		ret;
	int		ans;
	int		n;
	int		m;

	ans = 99;
	scanf("%d %d", &n, &m);
	map = (char **)malloc(n * sizeof(char *));
	for (int i = 0; i < n; ++i)
	{
		*(map + i) = (char *)malloc(m * sizeof(char));
		scanf("%s", *(map + i));
	}
	for (int i = 0; i < n - 7; ++i)
	{
		for (int j = 0; j < m - 7; ++j)
		{
			ret = solution(i, j, map);
			ans = ans < ret ? ans : ret;
		}
		free(*(map + i));
	}
	free(map);
	printf("%d\n", ans);
	return (0);
}