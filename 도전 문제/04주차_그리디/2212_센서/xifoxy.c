#include <stdio.h>

// 번역을 개같이 해놨다.
// 문제 예제대로 라면,
// 6
// 2
// 1 6 9 3 6 7
// 센서가 6개인데, 기지국을 가장 효율적으로 설치하라는 말이다.
// 정렬을 해보면, 1 3 6 6 7 9
// [1 3] [6 9] 저 범위 사이에 두개의 기지국을 설치하면,
//   2     3 이라는 값이 나오기에 답이 5가 된다.
// 이를 효율적으로 행하기 위해 센서의 값들을 정렬해주고,
// 센서들 간의 거리를 구한다. 그 이후에 K개의 기지국을 세워야 하기 때문에,
// N - K개의 거리만 구해주면 된다.

int	arr[10000];
int	temp[10000];
int	dist[10000];
int	n;
int	k;

void	merge(int *arr, int left, int mid, int right)
{
	int	i;
	int	j;
	int	p;

	i = left;
	j = mid + 1;
	p = 0;
	while (i <= mid && j <= right)
	{
		if (*(arr + i) <= *(arr + j))
			*(temp + p++) = *(arr + i++);
		else
			*(temp + p++) = *(arr + j++);
	}
	while (i <= mid)
		*(temp + p++) = *(arr + i++);
	while (j <= right)
		*(temp + p++) = *(arr + j++);
	for (int idx = left, p = 0; idx <= right; ++idx)
		*(arr + idx) = *(temp + p++);
	return ;
}

void	merge_sort(int *arr, int left, int right)
{
	int	mid;

	if (!(left < right))
		return ;
	mid = (left + right) / 2;
	merge_sort(arr, left, mid);
	merge_sort(arr, mid + 1, right);
	merge(arr, left, mid, right);
	return ;
}

int		main(void)
{
	int	ans;

	scanf("%d %d", &n, &k);
	for (int i = 0; i < n; ++i)
		scanf("%d", (arr + i));
	merge_sort(arr, 0, n - 1);
	for (int i = 0; i < n - 1; ++i)
		*(dist + i) = *(arr + i + 1) - *(arr + i);
	merge_sort(dist, 0, n - 2);
	ans = 0;
	for (int i = 0; i < n - k; ++i)
		ans += *(dist + i);
	printf("%d\n", ans);
	return (0);
}
