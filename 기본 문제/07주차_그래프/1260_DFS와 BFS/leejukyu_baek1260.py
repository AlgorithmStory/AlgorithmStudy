from collections import deque

n, m, v = map(int, input().split())

a = [[]*m for _ in range(n+1)]

for _ in range(m):                      # 각각 위치에 연결된 번호 넣어주기
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

for i in range(len(a)):
    a[i].sort()                         # 오름차순으로 정렬

visit = [0] * (n+1)

def dfs(a, v, visit):
    print(v, end=' ')                   # 탐색 위치 프린트
    visit[v] = 1                        # 방문표시
    for i in a[v]:                      # 해당 위치에 연결 된 애들
        if visit[i] == 0:               # 방문 안했으면
            dfs(a,i,visit)              # 재귀

def bfs(a, v, visit):
    print('\n', end = '')
    queue=deque([v])                    # 탐색 위치 삽입
    visit[v] = 2                        # 방문했다고 표시

    while queue:                        
        k = queue.popleft()             # 탐색 위치 프린트
        print(k, end=' ')
        for i in a[k]:                  # 해당 위치에 연결 된 애들
            if visit[i] == 1:           # 방문 안했으면
                queue.append(i)         # 큐에 넣음
                visit[i] = 2            # 방문표시

dfs(a,v,visit)
bfs(a,v,visit)