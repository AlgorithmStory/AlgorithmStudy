#include <stdio.h>

// 배열을 순회하면서 만들어질 수 있는 모든 모형을 검사해보면 된다.

const int	INF = -1e9;
int			board[505][505];
int			n, m;
const int	delta[] = {0, 1};
const int	dx_h[10][2] = {{0, 0}, {0, 1}, {0, 1}, {1, 1}, {0, -1}, {0, -1}, {-1, -1}, {-1, 0}, {1, 0}, {1, 1}};
const int	dy_h[10][2] = {{2, 3}, {2, 0}, {2, 1}, {0, 1}, {2,  2}, {2,  1}, { 1,  2}, { 0, 2}, {2, 2}, {1, 2}};
const int	dx_v[9][2] = {{2, 3}, {2,  0}, {2, 2}, {2, 1}, {2,  1}, {1, 2}, {2, 0}, { 2, 2}, { 1,  2}};
const int	dy_v[9][2] = {{0, 0}, {0, -1}, {0, 1}, {0, 1}, {0, -1}, {1, 1}, {0, 1}, {-1, 0}, {-1, -1}};

int	max(int a, int b) { return (a > b ? a : b); }
int	min(int a, int b) { return (a > b ? b : a); }
int	safe(int x, int y) { return (min(x, y) >= 0 && x < n && y < m); }

int	horizontal(int x, int y)
{
	int	ret;
	int	cmp;

	ret = 0;
	for (int direction = 0; direction < 2; ++direction)
	{
		int	ny = y + delta[direction];
		if (!safe(x, ny))
			continue ;
		ret += board[x][ny];
	}
	cmp = ret;
	for (int shape = 0; shape < 10; ++shape)
	{
		int	temp;
		temp = cmp;
		for (int direction = 0; direction < 2; ++direction)
		{
			int	nx = dx_h[shape][direction] + x;
			int	ny = dy_h[shape][direction] + y;
			if (!safe(nx, ny))
				continue ;
			temp += board[nx][ny];
		}
		ret = max(ret, temp);
	}
	return (ret);
}

int	vertical(int x, int y)
{
	int	ret;
	int	cmp;

	ret = 0;
	for (int direction = 0; direction < 2; ++direction)
	{
		int	nx = x + delta[direction];
		if (!safe(nx, y))
			continue ;
		ret += board[nx][y];
	}
	cmp = ret;
	for (int shape = 0; shape < 9; ++shape)
	{
		int	temp;
		temp = cmp;
		for (int direction = 0; direction < 2; ++direction)
		{
			int	nx = dx_v[shape][direction] + x;
			int	ny = dy_v[shape][direction] + y;
			if (!safe(nx, ny))
				continue ;
			temp += board[nx][ny];
		}
		ret = max(ret, temp);
	}
	return (ret);
}

int	main(void)
{
	int	ans;

	ans = INF;
	scanf("%d %d", &n, &m);
	for(int x = 0; x < n; ++x)
		for(int y = 0; y < m; ++y)
			scanf("%d", *(board + x) + y);
	for(int x = 0; x < n; ++x)
		for(int y = 0; y < m; ++y)
			ans = max(ans, max(horizontal(x, y), vertical(x, y)));
	printf("%d\n", ans);
	return (0);
}