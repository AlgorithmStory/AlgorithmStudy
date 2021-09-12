#include <iostream>
#include <vector>
using namespace std;

// 숫자들이 중복되지 않게 수열을 만들어 주면 된다.
// 메모하고, 원하는 깊이만큼 재귀에 들어갔을때 출력
// 끝
int n, depth;
bool visit[10];
vector<int> vec;
void	sol(int dep)
{
	if (dep == depth)
	{
		for(auto &p : vec)
			cout << p << ' ';
		cout << '\n';
		return ;
	}
	for (int i = 1; i <= n; ++i)
	{
		if (visit[i]) continue;
		visit[i] = true;
		vec.push_back(i);
		sol(dep + 1);
		visit[i] = false;
		vec.pop_back();
	}
}

int		main()
{
	cin >> n >> depth;
	sol(0);
}