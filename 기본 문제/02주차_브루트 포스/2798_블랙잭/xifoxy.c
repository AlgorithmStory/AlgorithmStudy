#include <stdio.h>
#include <stdlib.h>

const int	M = -1e9;
int			*arr;
int			n;
int			m;
int	solution(int idx, int depth, int sum, int *arr)
{
	int	ret;
	int	temp;

	if (depth == 3)
		return (sum > m ? M : sum);	
	ret = M;
	for (int i = idx; i < n; ++i)
	{
		temp = solution(i + 1, depth + 1, sum + *(arr + i), arr);
		ret = ret < temp ? temp : ret;
	}
	return (ret);
}

int main(void)
{
	scanf("%d %d", &n, &m);
	arr = (int *)malloc(sizeof(int) * n);
	for (int i = 0; i < n; ++i)
		scanf("%d", arr + i);
	printf("%d\n", solution(0, 0, 0, arr));
	free(arr);
	return (0);
}