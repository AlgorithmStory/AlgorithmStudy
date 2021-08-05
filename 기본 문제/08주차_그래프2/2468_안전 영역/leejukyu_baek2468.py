import sys
sys.setrecursionlimit(10 ** 6)
import copy

n = int(input())
a = [[int(x) for x in input().split()] for _ in range(n)]       # 해당 지점 높이 저장

arr = []
for i in range(n):                                              
    for j in a[i]:
        arr.append(j)
a_set = set(arr)                                                # 높이 중복값 없이 저장
a_set = list(a_set)                                             # 리스트로 바꿔줌

def graph(x,y):
    if x > -1 and y > -1 and x <= (n-1) and y <= (n-1):         # 행렬 안의 위치일때
        if b[x][y] >= k:                                        # 물에 잠기는 지점보다 높다면
            b[x][y] = 0                                         # 0 으로 바꿔줌
            graph(x-1, y)                                       # 4방향 탐색
            graph(x, y-1)
            graph(x+1, y)
            graph(x, y+1)

result = []
for k in a_set:                                                 # 물이 차는 높이는 지점 높이 중에서 탐색
    cnt = 0             
    b = copy.deepcopy(a)                                        # b에 a 리스트 복사
    for i in range(n):
        for j in range(n):
            if b[i][j] >= k:                                    # 물 높이보다 지점이 높다면
                graph(i,j)                                      # 함수 실행
                cnt += 1                                        # 함수가 끝나면 사방이 막혔으니까 다음 실행시 +1
    result.append(cnt)                                          # 물 높이마다 안전지대 카운트한거 리스트에 저장
print(max(result))                                              # 리스트의 가장 큰 값이 안전지대 가장 큰 수