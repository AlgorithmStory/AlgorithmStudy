from sys import stdin

# 재귀 제한 늘림.
import sys
sys.setrecursionlimit(10000)

# 입력.
test_case = int(stdin.readline())

# 상하좌우 재귀 탐색 함수.
def recursuib(i,j):
    global local_dict
    key = str(i)+"|"+str(j)
    if key not in local_dict:
        return 0
    if key in local_dict and local_dict[key] == 1:
        return 0
    local_dict[key] = 1
    recursuib(i+1,j)
    recursuib(i,j+1)
    recursuib(i-1,j)
    recursuib(i,j-1)

# test_case 만큼 실행.
for _ in range(test_case):

    # 입력.
    m,n,k = map(int, stdin.readline().split(" "))

    # 방문체크 딕셔너리.
    local_dict = {}

    # 입력에 대해서 딕셔너리에 위치 키 값과 밸류 0으로 저장.
    for _ in range(k):
        a, b = map(str, stdin.readline().strip().split(" "))
        local_dict[a +"|"+ b] = 0

    # 결과.
    result_cnt = 0

    # 맵 크기 만큼 이중 포문 돔.
    for i in range(m+1):
        for j in range(n+1):
            key = str(i)+"|"+str(j) # 위치 키 값.
            if key in local_dict and local_dict[key] == 0: # 위치 값이 존재하면서, 키 값이 0일때만 함수 실행.
                result_cnt += 1
                recursuib(i,j)
                local_dict[key] = 1

    # 출력.
    print(result_cnt)
