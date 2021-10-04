#include <stdio.h>

// quick sort
// N이 1000이기 떄문에
// θ(NlogN)인 알고리즘을 이용하면 무난하게 풀수 있다.

# define swap(x, y, temp) ( (temp) = (x), (x) = (y), (y) = (temp) )
int	arr[1001];
int	n;

int partition(int *arr, int left, int right){
	const int	pivot = *(arr + left);
	int			temp;
	int			low; 
	int			high;

	low = left;
	high = right + 1;
	do
	{
		do
		{
			low++;
		} while (low <= right && *(arr + low) < pivot);
		do
		{
			high--;
		} while (high >= left && *(arr + high) > pivot);
		if (low < high)
			swap(*(arr + low), *(arr + high), temp);
	} while (low < high);
	swap(*(arr + left), *(arr + high), temp);
	return (high);
}

void	quicksort(int *arr, int left, int right)
{
	int	pi;

	if (left < right)
	{
		pi = partition(arr, left, right);
		quicksort(arr, left, pi - 1);
		quicksort(arr, pi + 1, right);
	}
	return ;
}

int	main(void)
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%d", (arr + i));
	quicksort(arr, 0, n - 1);
	for (int i = 0; i < n; ++i)
		printf("%d\n", *(arr + i));
	return (0);
}
