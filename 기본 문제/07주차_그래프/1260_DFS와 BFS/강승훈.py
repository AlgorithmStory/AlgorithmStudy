from sys import stdin

# 입력.
n, m, k = map(int, stdin.readline().split(" "))

graph_arr = [[0] * (n + 1) for _ in range(n + 1)] # 연결을 나타낸 2차원 배열.
visited = [False for _ in range(n+1)] # 방문 체크 배열.

# 입력.
for _ in range(m):
    a, b = map(int, stdin.readline().split(" "))
    graph_arr[a][b] = 1
    graph_arr[b][a] = 1

# dfs 함수.
def my_dfs(node):
    visited[node] = True # 받자마자 방문 체크.
    print(node, end=' ') # 출력.
    # 2차원 배열의 node 행 탐색.
    for i in range(1, n + 1):
        if not visited[i] and graph_arr[node][i] == 1: # 아직 방문 안했고, 1이란건 연결됬다는 의미.
            my_dfs(i) # 재귀.

# bfs 함수.
def my_bfs(node):
    sub_arr = [node] # 처음 입력으로 받은 k가 처음 들어감.
    visited[node] = False # 앞서 탐색한 dfs에 의해서, 모두 True가 되었기 때문에, 반대(False)로 의미 부여.
    # sub_arr이 비어질때까지 돔.
    while sub_arr:
        node = sub_arr.pop(0) # 첫번째 요소 가져와서,
        print(node, end=' ') # 일단 출력해주고,
        for i in range(1, n + 1): # 1부터 도는데,
            if visited[i] and graph_arr[node][i] == 1: # node번째 행의 1인 값의 위치 값을 다 넣어줌.
                sub_arr.append(i)
                visited[i] = False # 방문 체크.

# 출력.
my_dfs(k)
print()
my_bfs(k)
