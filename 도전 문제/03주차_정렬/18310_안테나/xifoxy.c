#include <stdio.h>

// 단순한 논리다, 집들을 일렬로 나열했을대 중간에 있는 집을 고르면 된다.
// N이 짝수일떈 인덱스 놀이가 필요하다.

int	arr[200000];
int	temp[200000];
int	n;

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

	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%d", (arr + i));
	merge_sort(arr, 0, n - 1);
	ans = *(arr + (n / 2));
	if (!(n % 2))
		ans = *(arr + (n / 2) - 1);
	printf("%d\n", ans);
	return (0);
}
