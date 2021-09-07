# 상하좌우 탐색 함수.
def my_dfs(index):
    global visited
    key = str(index)
    if index[0] < 0 or index[1] < 0 or index[0] >= n or index[1] >= m or key in visited:
        return
    visited.add(key)
    if arr[index[0]][index[1]] == 1:
        return
    if index[0] == n-1:
        print("YES")
        exit(0)
    my_dfs([index[0], index[1] + 1])
    my_dfs([index[0], index[1] - 1])
    my_dfs([index[0] + 1, index[1]])
    my_dfs([index[0] - 1, index[1]])



import sys
sys.setrecursionlimit(1000000)
from sys import stdin

# 입력.
n,m = map(int, stdin.readline().split(" "))
arr = list(list(map(int, stdin.readline().strip())) for _ in range(n))

# 방문 기록.
visited = set()

# 첫번째 행에 대해서만 탐색함.
for i in range(m):

    # 값이 0이면 실행.
    if arr[0][i] == 0:

        # 방문 확인.
        key = str([0, i])
        if key not in visited:
            my_dfs([0, i])
            visited.add(key)

# my_dfs 함수 안에서 도착점에 도달했으면, "YES" 출력하고 프로그램 종료되게 했음.
# 만약 저 for가 끝났는대도 프로그램이 종료되지 않는다면, "NO" 출력.
print("NO")
