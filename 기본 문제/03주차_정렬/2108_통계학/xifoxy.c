#include <stdio.h>

// 요구하는대로 구현하되,
// 메모하는 배열에 대해 주의를 해야한다.
// |INPUT| = 4000 이기에, 음수를 고려할 필요가 있다.
// 그리고 정렬해야 하는 후보수는 총 50만개이기 때문에,
// Merge Sort가 적절하다.

int	arr[500000];
int	temp[500000];
int	cnt[8080];
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

int	upper(double num)
{
	int	ret;

	ret = (int)(num * 10) % 10;
	if (ret < 0 && ret <= -5)
		ret = -1;
	else if (ret > 0 && ret >= 5)
		ret = 1;
	else
		ret = 0;
	return (num + ret);
}

int	main(void)
{
	int	total;
	int	count;
	int	idx;
	int	mode;
	int	a;

	count = 0;
	total = 0;
	idx = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", (arr + i));
		a = *(arr + i);
		total += a;
		*(cnt + (a + 4000)) += 1;
		if (*(cnt + (a + 4000)) > count)
			count = *(cnt + (a + 4000));
	}
	merge_sort(arr, 0, n - 1);
	printf("%d\n", upper(1.0 * total / n));
	printf("%d\n", *(arr + (n / 2)));
	for (int i = 0, flag = 0; i <= 8000; ++i)
	{
		if (*(cnt + i) == count)
		{
			mode = i - 4000;
			if (flag++)
				break ;
		}
	}
	printf("%d\n", mode);
	printf("%d\n", *(arr + n - 1) - *(arr));
	return (0);
}
