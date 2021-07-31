import sys
sys.setrecursionlimit(10 ** 6)

T = int(input())

for _ in range(T):
    m, n ,k = map(int, input().split())
    a = [[0]*m for _ in range(n)]

    for _ in range(k):                                              # 해당 위치만 1이고 나머지 0인 행렬 만들기
        x,y = map(int, input().split())
        a[y][x] = 1

    cnt = 0
    def graph(x,y):
        if x > -1 and y > -1 and x <= (n-1) and y <= (m-1):         # 행렬 크기를 벗어나지 않은 선에서 탐색
            if a[x][y] == 1:                                        # 해당 위치가 1이라면
                a[x][y] = 0                                         # 0으로 바꿔줌
                graph(x-1, y)                                       # 4방향 확인 반복
                graph(x, y-1)
                graph(x+1, y)
                graph(x, y+1)
        
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:                                        # 1인 경우에 
                graph(i,j)                                          # 함수 실행
                cnt += 1                                            # 함수가 다 돌면 인접한 배추가 없다는 것이므로 1마리 증가
    print(cnt)