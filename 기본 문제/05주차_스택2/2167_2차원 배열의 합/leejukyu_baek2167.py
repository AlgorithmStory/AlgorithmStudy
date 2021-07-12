import sys

N, M = map(int,input().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K = int(input())
n_sum = []                                                                  # 누적합을 저장할 리스트

for n in range(N):
    sum = 0
    arr = [0]                                                               # (1,1) 부터 시작할때를 계산하기 위해 행의 처음은 0을 넣어줌
    for m in range(M):
        sum += a[n][m]                                                      # x축 방향으로 누적합 
        arr.append(sum)                                                     # 누적합을 리스트에 넣어서
    n_sum.append(arr)                                                       # 누적합으로 이루어진 행렬을 만듦 [[0,1,3,7],[0,8,24,56]]

for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    result = 0
    for k in range(i-1, x):                                                 # 행 범위, i부터 x까지의 위치
        result += (n_sum[k][y] - n_sum[k][j-1])                             # 열 범위, j부터 y까지의 위치
    print(result)                                                           # (x,y)에서 (i-1,j-1) 위치의 누적합을 빼면 원하는 위치 만큼의 부분합을 구할 수 있음