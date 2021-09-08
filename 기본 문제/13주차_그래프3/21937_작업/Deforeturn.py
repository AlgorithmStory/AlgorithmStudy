from sys import stdin
import sys
sys.setrecursionlimit(300000)


# 최상단 노드를 만날때까지 재귀.
def my_dfs(node):
    global visited
    if len(tree[node]) == 0:
        return 0
    sub_sum = 0
    for crnt in tree[node]:
        if crnt not in visited:
            sub_sum += my_dfs(crnt)
            visited.add(crnt)
            sub_sum += 1
    return sub_sum

# 입력.
n, m = map(int, stdin.readline().split(" "))
tree = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, stdin.readline().split(" "))
    tree[b].append(a)
number = int(stdin.readline().strip())

# 방문 체크 변수.
visited = set()

# 최하단 리프 노드에서 최상단 노드까지 가면서 카운트 해줌.
result_sum = 0
for crnt in tree[number]:
    if crnt not in visited:
        result_sum += my_dfs(crnt)
        visited.add(crnt)
        result_sum += 1

# 출력.
print(result_sum)
