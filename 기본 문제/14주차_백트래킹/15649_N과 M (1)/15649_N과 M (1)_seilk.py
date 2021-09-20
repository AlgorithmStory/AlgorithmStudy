```python
from sys import stdin
n , m = map(int, stdin.readline().split())
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
tot = [i for i in range(1, n + 1)] #[1, 2, 3, 4, ...]
dfs = [0 for i in range(n)] #[0, 0, 0, 0, ...]
series = [0]

def f(depth):
    if depth == m: #depth는 수열의 길이
        print(*series[1:], sep=" ")
        return
    for i in range(0, n):
        if not dfs[i] and series[-1] < tot[i]: #dfs[i] == 0
            dfs[i] = 1
            series.append(tot[i])
            f(depth + 1)
            series.pop()
            dfs[i] = 0

f(0)
```
