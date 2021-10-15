#include <stdio.h>
#include <string.h>

// 단어의 갯수가 2만개다.
// 그러니까 Worst case 가 O(N^2)인 quick sort 보다는 
// merge sort가 효율적이다.
// 단어를 정렬하되, 중복되는 단어가 있다면
// 구조체 안에 ans라는 변수에 flag값을 줘서 필터링을 해줬다.

typedef struct s_info
{
	char	word[55];
	int		len;
	char	ans;
}	t_info;

t_info	list[20000];
t_info	temp[20000];
int		n;

int		custom_strcmp(char *a, char *b)
{
	while (*a && *b)
	{
		if (*a != *b)
			break ;
		++a;
		++b;
	}
	return (*a - *b);
}

void	merge(t_info *arr, int left, int mid, int right)
{
	int	i;
	int	j;
	int	p;
	int	cmp;

	i = left;
	j = mid + 1;
	p = 0;
	while (i <= mid && j <= right)
	{
		if ((arr + i)->len < (arr + j)->len)
			*(temp + p++) = *(arr + i++);
		else if ((arr + i)->len > (arr + j)->len)
			*(temp + p++) = *(arr + j++);
		else
		{
			cmp = custom_strcmp((arr + i)->word, (arr + j)->word);
			if (!cmp)
				(arr + i)->ans = 1;
			if (cmp <= 0)
				*(temp + p++) = *(arr + i++);
			else if (cmp > 0)
				*(temp + p++) = *(arr + j++);
		}
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

int	main(void)
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		(list + i)->len = 0;
		(list + i)->ans = 0;
		scanf("%s", (list + i)->word);
		(list + i)->len = strlen((list + i)->word);
	}
	merge_sort(list, 0, n - 1);
	for (int i = 0; i < n; ++i)
		if (!(list + i)->ans)
			printf("%s\n", (list + i)->word);
	return (0);
}
