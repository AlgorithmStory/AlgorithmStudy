#include <stdio.h>

// 각 자릿수의 값들을 치환해서 메모 해준다.
// 그런 다음 내림차순으로 정렬하여,
// digit을 추가해주면 된다.
// ex) ABC BBB BB BB BB
// A = 100, B = 154, C = 1

typedef struct	s_info
{
	char		ch;
	int			num;
}				t_info;

int		n;
int		digit[26];
char	num[11][10];
t_info	info[26];
t_info	temp[26];

int		strlen(char *str)
{
	char	*iter;
	int		ret;

	iter = str;
	ret = 0;
	while (*(iter++))
		ret++;
	return (ret);
}

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
		if ((arr + i)->num >= (arr + j)->num)
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
	char	*iter;
	int		len;
	int		digit_value;
	int		idx;
	int		ans;
	int		sum;

	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%s", *(num + i));
	for (int i = 0; i < n; ++i)
	{
		digit_value = 1;
		iter = *(num + i);
		len = strlen(iter);
		for (int j = len - 1; j >= 0; --j)
		{
			idx = *(iter + j) - 'A';
			(info + idx)->ch = *(iter + j);
			(info + idx)->num += digit_value;
			digit_value *= 10;
		}
	}
	merge_sort(info, 0, 25);
	for (int i = 0; i < 10; ++i)
	{
		if (!(info + i)->num)
			break ;
		*(digit + (info + i)->ch - 'A') = 9 - i;
	}
	ans = 0;
	for (int i = 0; i < n; ++i)
	{
		iter = *(num + i);
		len = strlen(iter);
		digit_value = 1;
		sum = 0;
		for (int j = len - 1; j >= 0; --j)
		{
			idx = *(iter + j) - 'A';
			sum += *(digit + idx) * digit_value;
			digit_value *= 10;
		}
		ans += sum;
	}
	printf("%d\n", ans);
	return (0);
}
