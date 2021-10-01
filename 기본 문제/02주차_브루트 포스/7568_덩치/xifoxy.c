#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 조건에 맞게 잘 비교해주면 끝난다.

typedef struct	s_info
{
	int	height;
	int	weight;
	int	ans;
}	t_info;

t_info	*arr;
int	main(void)
{
	int	n;

	scanf("%d", &n);
	arr = (t_info *)malloc(sizeof(t_info) * n);
	memset(arr, 0, sizeof(t_info));
	for (int i = 0; i < n; ++i)
		scanf("%d %d", &(arr + i)->height, &(arr + i)->weight);
	for (int i = 0; i < n; ++i)
	{
		(arr + i)->ans = 1;
		for (int j = 0; j < n; ++j)
		{
			if (i == j)
				continue ;
			if ((arr + i)->height < (arr + j)->height && (arr + i)->weight < (arr + j)->weight)
				(arr + i)->ans++;
		}
	}
	for (int i = 0; i < n; ++i)
		printf("%d ", (arr + i)->ans);
	free(arr);
	return (0);
}