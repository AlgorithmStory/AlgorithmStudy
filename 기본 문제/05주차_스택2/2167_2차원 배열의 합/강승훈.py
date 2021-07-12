from sys import stdin

# 입력.
n,m = map(int, stdin.readline().split(" "))
arr = list(list(map(int, stdin.readline().split())) for _ in range(n))
test_case = int(stdin.readline().strip())

for _ in range(test_case):
    i1, j1, i2, j2 = map(int, stdin.readline().split(" ")) # 좌표 입력.
    sub_sum = 0 # 결과 저장 할 변수.
    for i in range(i1-1, i2): # 일단, 입력으로 들어온 i1와 i2 넣으면 col연산 되고,
        for j in range(j1-1, j2): # 포문 마다, j1부터 j2 까지 더하면 row연산 됨.
            sub_sum += arr[i][j]

    # 매번 출력.
    print(sub_sum)
