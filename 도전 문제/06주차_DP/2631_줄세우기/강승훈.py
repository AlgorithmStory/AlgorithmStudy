# 입력으로 주어진 배열에서 가장 긴 증가하는 수열(예제에선 3,5,6)의 길이를 n에다가 뺀 값이 정답임.
from sys import stdin

# 입력.
n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]

# 가장 긴 증가하는 수열을 구하는데 필요한 변수 배열.
lis_arr = [1 for _ in range(n)]
max_check = 1

for i in range(1, n): # 두번째 부터 n까지 돌면서,
    sub_max = 1

    # 매 포문마다 i-1 부터, 처음까지 왼쪽으로 탐색함.
    for j in range(i):
        if arr[i] > arr[-(n-i+j+1)] and lis_arr[-(n-i+j+1)]+1 > sub_max:
            sub_max = lis_arr[-(n-i+j+1)]+1
    lis_arr[i] = sub_max
    if lis_arr[i] > max_check:
        max_check = lis_arr[i]

# 출력.
print(n-max_check)
