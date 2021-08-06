import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque


m,n,h = map(int, input().split())
a = [[[int(x) for x in input().split()] for _ in range(n)] for _ in range(h)]
cnt = 0                                                                             # 날짜 카운트

def dfs(z,x,y):                                                                     
    que = []                                                                        # 연결된 위치 저장 리스트
    if x > 0 and a[z][x-1][y] == 0:                                                 # 연결된 위치값이 0이고 행렬을 벗어나지 않았다면
        a[z][x-1][y] = 1                                                            # 해당 위치 1로 바꾸고
        que.append([z,x-1,y])                                                       # 리스트에 저장

    if y > 0 and a[z][x][y-1] == 0:                                                 # 6방향 탐색
        a[z][x][y-1] = 1        
        que.append([z,x,y-1])

    if x<=(n-2) and a[z][x+1][y] == 0:
        a[z][x+1][y] = 1   
        que.append([z,x+1,y])
    
    if y<=(m-2) and a[z][x][y+1] == 0:
        a[z][x][y+1] = 1   
        que.append([z,x,y+1])
    
    if z > 0 and a[z-1][x][y] == 0:        
        a[z-1][x][y] = 1   
        que.append([z-1,x,y])                  

    if z<=(h-2) and a[z+1][x][y] == 0:
        a[z+1][x][y] = 1   
        que.append([z+1,x,y])
    return que

arr_list = []                                                                       # 처음 익은 토마토 위치 저장 리스트
for z in range(h):
    for i in range(n):
        for j in range(m):
            if a[z][i][j] == 1:                                                     # 익은 토마토가 있으면
                arr_list.append([z,i,j])                                            # 저장

while arr_list:                                                                     # 위치가 저장되어 있으면
    que_list = []                                                                   # 함수에 저장된 위치 저장 리스트
    for z, x, y in arr_list:                                                        # 익은 토마토가 위치를 변수로 
        for i in dfs(z,x,y):                                                        # 함수 실행하고 연결 리스트 하나씩 빼옴
            que_list.append(i)                                                      # 리스트 차원을 2차원으로 고정하기 위해 빼온걸 리스트에 넣기
    cnt += 1                                                                        # 한칸씩 움직일때마다 +1
    arr_list = que_list                                                             # 새로 받아온 위치 리스트를 처음 리스트에 넣어서 반복

def fun(a, cnt):                                                                    # 0이 있는지 확인하는 함수
    for i in range(h):
        for j in range(n):
            if 0 in a[i][j]:                                                        # 리스트 안에 0이 있으면
                return False                                                        # False 
    return True                                                                     # 없으면 True

if fun(a, cnt):                                                                     # True면
    print(cnt-1)                                                                    # 날짜 프린트
else:
    print(-1)                                                                       # False면 -1 