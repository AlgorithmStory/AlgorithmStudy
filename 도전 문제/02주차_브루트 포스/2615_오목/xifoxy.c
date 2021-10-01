#include <stdio.h>

// 오목이 되는 조건 6목은 안된다.

int			board[19][19];
int			dx[4] = {1, 0, 1, -1};
int			dy[4] = {0, 1, 1, 1};
int	min(int x, int y)
{
	return (x > y ? y : x);
}

int	max(int x, int y)
{
	return (x > y ? x : y);
}

int	safe(int x, int y)
{
	return (min(x, y) >= 0 && max(x, y) < 19);
}

int	sol(int x, int y)
{
	int	ret;
	int	nx;
	int	ny;
	int	cnt;

	ret = 0;
	for (int direction = 0; direction < 4; ++direction)
	{
		nx = x;
		ny = y;
		cnt = 0;
		while (safe(nx, ny) && board[x][y] == board[nx][ny])
		{
			++cnt;
			nx += dx[direction];
			ny += dy[direction];
		}
		nx = x - dx[direction];
		ny = y - dy[direction];
		if (cnt == 5 && (!safe(nx, ny) || board[nx][ny] != board[x][y]))
		{
			ret = 1;
			printf("%d\n%d %d\n", board[x][y], x + 1, y + 1);
		}
		if (ret)
			break ;
	}
	return (ret);
}

int	main(void)
{
	int	ans;

	ans = 0;
	for (int i = 0; i < 19; ++i)
		for (int j = 0; j < 19; ++j)
			scanf("%d", *(board + i) + j);
	for (int x = 0; x < 19; ++x)
	{
		for (int y = 0; y < 19 && !ans; ++y)
		{
			if (!board[x][y])
				continue ;
			ans = sol(x, y);
		}
	}
	if (!ans)
		puts("0");
	return (0);
}
