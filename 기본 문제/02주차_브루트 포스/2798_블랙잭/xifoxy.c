#include <stdio.h>
#include <stdlib.h>

// 카드 3개의 합이 m에 가까운것을 찾아서 출력하면 된다.
// depth가 정해져 있는 문제는 재귀가 편하다.

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