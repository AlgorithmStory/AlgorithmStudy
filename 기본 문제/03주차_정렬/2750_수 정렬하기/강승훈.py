from sys import stdin

# 입력
n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]

# 버블정렬
for i in range(n-1):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            tmp_1 = arr[j]; tmp_2 = arr[j+1]
            arr[j] = tmp_2; arr[j+1] = tmp_1

# 출력
for crnt in arr:
    print(crnt)
