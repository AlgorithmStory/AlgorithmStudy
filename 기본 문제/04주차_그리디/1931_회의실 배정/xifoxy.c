#include <stdio.h>

// 예쁘게 정렬하면 된다.
// end의 시간이 같다면, 시작시간이 빠른 순으로,
// 그리고 end가 낮은 순으로 정렬하면 된다.

typedef struct	s_info
{
	int			start;
	int			end;
}				t_info;

t_info	info[100000];
t_info	temp[100000];
int		n;

void	merge(t_info *arr, int left, int mid, int right)
{
	int	i;
	int	j;
	int	p;

	i = left;
	j = mid + 1;
	p = 0;
	while (i <= mid && j <= right)
	{
		if ((arr + i)->end < (arr + j)->end || \
			((arr + i)->end == (arr + j)->end && \
			(arr + i)->start < (arr + j)->start))
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

void	merge_sort(t_info *arr, int left, int right)
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
	int	st;
	int	ans;

	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%d %d", &(info + i)->start, &(info + i)->end);
	merge_sort(info, 0, n - 1);
	st = -1;
	ans = 0;
	for (int i = 0; i < n; ++i)
	{
		if ((info + i)->start < st)
			continue ;
		st = (info + i)->end;
		ans++;
	}
	printf("%d\n", ans);
	return (0);
}
