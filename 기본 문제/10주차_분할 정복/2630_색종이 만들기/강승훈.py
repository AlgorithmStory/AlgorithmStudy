from sys import stdin

# 출력.
n = int(input())
arr = list(list(map(int, stdin.readline().split(" "))) for _ in range(n))

# 핵심 함수.
def recursion(arr):
    arr_len = len(arr)
    break_check = 0
    init_value = arr[0][0]
    # 들어온 배열의 모든 값이 같은지, 다른지 체크 하는 이중 포문.
    for i in range(arr_len):
        for j in range(arr_len):
            if arr[i][j] != init_value:
                break_check = 1
                break
        if break_check == 1:
            break

    # 모든 값이 같으면, 분기해서 카운트 해줌.
    if break_check == 0:
        if init_value == 0:
            global white_cnt
            white_cnt += 1
        else:
            global blue_cnt
            blue_cnt += 1
    else: # 그게 아니라면,
        next_1 = []
        next_2 = []
        next_3 = []
        next_4 = []
        bias = arr_len//2
        for i in range(arr_len // 2):
            sub_1 = []
            sub_2 = []
            sub_3 = []
            sub_4 = []
            for j in range(arr_len // 2):
                sub_1.append(arr[i][j])
                sub_2.append(arr[i][j+bias])
                sub_3.append(arr[i+bias][j])
                sub_4.append(arr[i+bias][j+bias])
            next_1.append(sub_1)
            next_2.append(sub_2)
            next_3.append(sub_3)
            next_4.append(sub_4)

        # 영역을 나눠서 재귀 시작.
        recursion(next_1)
        recursion(next_2)
        recursion(next_3)
        recursion(next_4)

white_cnt = 0
blue_cnt = 0

# 입력 받은 배열을 파라미터로 넣음.
recursion(arr)

# 출력.
print(white_cnt)
print(blue_cnt)
