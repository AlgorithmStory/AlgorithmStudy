#include <stdio.h>

// 그냥 스티커 예쁘게 잘 붙여주면 된다.

int	arr[1000];
int	temp[1000];
int	n;
int	l;

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
	int	len;
	int	ans;

	scanf("%d %d", &n, &l);
	for (int i = 0; i < n; ++i)
		scanf("%d", (arr + i));
	merge_sort(arr, 0, n - 1);
	ans = 1;
	len = *(arr);
	for (int i = 0; i < n; ++i)
	{
		if (*(arr + i) < len + l)
			continue ;
		len = *(arr + i);
		ans++;
	}
	printf("%d\n", ans);
	return (0);
}
