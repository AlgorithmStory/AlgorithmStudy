#include <stdio.h>

// N = 5e3이다.
// 3개를 골라야 하는데 N^3로는 불가능하다.
// 그럼 N^2로 줄여야 한다는 말인데,
// 무작위로 고르는 3개의 수를 0에 최대한 수렴하게 한다는게 키포인트다.
// 그러니 배열을 정렬된 상태로 만들어주고,
// 2중 반복문으로 구현하되 하나는 투 포인터를 이용하면 쉽게 해결된다.
// |INPUT|이 최대 1e9라는 걸 명심해야한다.

typedef long long ll;

int	arr[5000];
int	temp[5000];
int	ans[3];
ll	res;
int	n;

ll		llabs(ll num) { return (num > 0 ? num : -num); }
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

void	solution(int idx)
{
	ll	sum;
	int	left;
	int	right;

	left = idx + 1;
	right = n - 1;
	while (left < right)
	{
		sum = 1LL * *(arr + idx) + *(arr + left) + *(arr + right);
		if (llabs(res) > llabs(sum))
		{
			res = sum;
			*(ans) = *(arr + idx);
			*(ans + 1) = *(arr + left);
			*(ans + 2) = *(arr + right);
		}
		if (sum >= 0)
			right--;
		else
			left++;
	}
	return ;
}

int		main(void)
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%d", (arr + i));
	merge_sort(arr, 0, n - 1);
	res = 4e9;
	for (int i = 0; i < n - 2; ++i)
		solution(i);
	printf("%d %d %d\n", *(ans), *(ans + 1), *(ans + 2));
	return (0);
}
