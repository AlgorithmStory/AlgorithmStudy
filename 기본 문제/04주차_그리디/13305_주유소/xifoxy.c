#include <stdio.h>

// 기름값이 싼 도시가 나올때마다 가격을 갱신하면 된다.

typedef long long ll;

ll	dist[100000];
ll	value[100000];
int	n;

int	main(void)
{
	ll	sum;
	ll	val;

	scanf("%d", &n);
	for (int i = 0; i < n - 1; ++i)
		scanf("%lld", (dist + i));
	for (int i = 0; i < n; ++i)
		scanf("%lld", (value + i));
	val = 1e9;
	sum = 0;
	for (int i = 0; i < n - 1; ++i)
	{
		if (val > *(value + i))
			val = *(value + i);
		sum += *(dist + i) * (val);
	}
	printf("%lld\n", sum);
	return (0);
}
