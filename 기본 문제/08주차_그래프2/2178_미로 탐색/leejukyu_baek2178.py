import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

m, n = map(int, input().split())

a = []
for _ in range(m):                                      # 행렬 만들기
    arr = []
    d = input()
    for i in d:
        i = int(i)
        arr.append(i)
    a.append(arr)    

def bfs(a):       
    que = deque([[0,0]])                                # 시작지점 que에 넣기
    while que:                                          # que가 있다면
        k = que.popleft()                               # 맨 왼쪽 출력
        if k[0] > 0 and a[k[0]-1][k[1]] == 1:           # 방문 안했으면
            que.append([k[0]-1,k[1]])                   # que에 위치값 넣기
            a[k[0]-1][k[1]] = a[k[0]][k[1]] + 1         # 한칸 움직였으니까 이전 위치값의 +1

        if k[1] > 0 and a[k[0]][k[1]-1] == 1:           # 4방향 탐색
            que.append([k[0],k[1]-1])
            a[k[0]][k[1]-1] = a[k[0]][k[1]] + 1
        
        if k[0]<=(m-2) and a[k[0]+1][k[1]] == 1:
            que.append([k[0]+1,k[1]])
            a[k[0]+1][k[1]] = a[k[0]][k[1]] + 1
        
        if k[1]<=(n-2) and a[k[0]][k[1]+1] == 1:
            que.append([k[0],k[1]+1])
            a[k[0]][k[1]+1] = a[k[0]][k[1]] + 1

    return a[m-1][n-1]                                   # 목적지 카운트값 출력
print(bfs(a))