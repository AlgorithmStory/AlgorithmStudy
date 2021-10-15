#include <stdio.h>

// 숫자의 개수가 100만개다.
// θ(NlogN) O(N^2)인 quick sort는 적합하지 않다.
// 그렇다면 O(NlogN)이 보장되는 알고리즘을 써야하기 때문에 merge sort 구현.

int	arr[1000000];
int	temp[1000000];
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

int	main(void)
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%d", (arr + i));
	merge_sort(arr, 0, n - 1);
	for(int i = 0; i < n; ++i)
		printf("%d\n", *(arr + i));
	return (0);
}
