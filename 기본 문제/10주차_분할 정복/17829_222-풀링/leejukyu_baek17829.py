import sys
import itertools

n = int(input())
a = []
for _ in range(n):
    a.append([int(x) for x in sys.stdin.readline().split()])

def div(x,y,n,arr):                                                         # 분할함수
    if n != 2:                                                              # 사각형이 2X2 행렬이 아니면
        div(x,y,n//2,arr)                                                   # 쿼드 분할
        div(x, y+n//2, n//2,arr)
        div(x+n//2, y, n//2,arr)
        div(x+n//2, y+n//2, n//2,arr)
        return
    arr.append([x,y])                                                       # 2X2 행렬들의 시작부분을 arr리스트에 저장


def com(save, n):                                                           # 합치는 함수
    if n != 1:                                                              # 1X1 행렬이 아니면
        m = n//2                                                            
        result = [[0]*m for _ in range(m)]                                  # 절반 사이즈로 풀링이 저장될 행렬
        arr = []
        div(0,0,n,arr)                                                      # 분할함수 실행

        for k, z in arr:                                                    # 2X2 행렬 좌표
            lst = []
            for i, j in itertools.product(range(k, k+2), range(z, z+2)):    # 2X2 행렬 탐색하는 이중 포문
                lst.append(save[i][j])                                      # lst에 저장해서 1차원으로
            lst.sort()                                                      # 오름차순으로 정렬
            result[k//2][z//2] = lst[-2]                                    # 2번째로 큰 값을 풀링 행렬에 저장
        save = result                                                       # 다음 탐색을 위해 풀링 행렬을 탐색행렬에 저장
        com(save, n//2)                                                     # 1X1행렬이 될 때까지 함수 재귀
        return
    print(save[0][0])                                                       

save = a                                                                    # 입력받은 행렬을 탐색행렬에 저장
com(save, n)                                                                # 함수 실행






