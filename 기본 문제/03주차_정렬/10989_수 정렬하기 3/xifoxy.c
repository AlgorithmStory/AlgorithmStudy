#include <stdio.h>

// 아이디어 문제이다.
// 잘 살펴보면 정렬을 위한 시간은 5초이고,
// N이 1e7개가 주어지는데 사용 가능한 메모리는 8mb 이다.
// 그리고 후보수는 기껏해야 중복가능한 1e4이기 때문에, 메모만 해두면 된다.

int	arr[10001];
int	n;

int	main(void)
{
	scanf("%*d");
	while (scanf("%d", &n) != EOF)
		(*(arr + n))++;
	for (int i = 1; i <= 10000; ++i)
		while ((*(arr + i))--)
			printf("%d\n", i);
	return (0);
}