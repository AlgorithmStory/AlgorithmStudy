from sys import stdin

# dp배열 초기화.
dp_arr = [[1,0,0], [1,1,0], [2,1,1]]

# 테스트 케이스 입력.
test_case = int(stdin.readline())

# 테스트 케이스 만큼 실행.
for _ in range(test_case):

    # 입력.
    n = int(stdin.readline())

    # dp배열의 길이.
    dp_arr_len = len(dp_arr)

    # 입력 받은 n이 dp배열의 길이보다 크다면, 아직 계산 되지 않은 값이므로, 계산.
    if n > dp_arr_len:

        # dp배열의 마지막부터 계산을 재개.
        for i in range(dp_arr_len, n):

            # coin[j]원으로 n원을 만들기 위한 횟수는 n-coin[j...k]원을 만들기 위한 횟수의 합임.
            dp_arr.append([sum(dp_arr[i-1]), sum(dp_arr[i-2]), sum(dp_arr[i-3])])

        # 출력.
        print(sum(dp_arr[n-1]))

    # 입력 받은 n이 dp배열보다 작으면, 저장된 값을 바로 출력.
    else:
        #출력.
        print(sum(dp_arr[n-1]))
