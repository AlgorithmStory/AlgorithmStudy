from sys import stdin

# 입력.
n_main = int(stdin.readline())
arr = list(list(map(int, stdin.readline().split(" "))) for _ in range(n_main))

# 재귀.
def recursion(arr_sub):
    if len(arr_sub) <= 0:
        return
    global minus_cnt
    global zero_cnt
    global one_cnt
    arr_sub = arr_sub.copy()

    # 배열의 크기가 3x3이면,
    if len(arr_sub) == 3:
        break_check = 0
        for i in range(3):
            for j in range(3):
                # 탐색하다가 다른 값 나오면,
                if arr_sub[i][j] != arr_sub[0][0]:
                    break_check = 1
                    break
            if break_check == 1: # 나와서,
                break
        # 3x3 요소에 대한 카운트 해줌.
        if break_check == 1:
            for i in range(3):
                for j in range(3):
                    if arr_sub[i][j] == -1:
                        minus_cnt += 1
                    elif arr_sub[i][j] == 0:
                        zero_cnt += 1
                    elif arr_sub[i][j] == 1:
                        one_cnt += 1
            return
    else: # 배열의 크기가 3x3이 아니면,
        for i in range(len(arr_sub)):
            for j in range(len(arr_sub)):
                # 탐색하다가 다른 값 발견하면, 분할해서 재귀 돌림.
                if arr_sub[i][j] != arr_sub[0][0]:
                    div_len = len(arr_sub) // 3
                    next_arr_2 = []; next_arr_3 = []; next_arr_4 = []; next_arr_5 = []; next_arr_6 = [];
                    next_arr_1 = []; next_arr_7 = []; next_arr_8 = []; next_arr_9 = []
                    for sub_i in range(div_len):
                        next_sub_1 = []; next_sub_2 = []; next_sub_3 = []; next_sub_4 = []; next_sub_5 = [];
                        next_sub_6 = []; next_sub_7 = []; next_sub_8 = []; next_sub_9 = [];
                        for sub_j in range(div_len):
                            next_sub_1.append(arr_sub[sub_i][sub_j]); next_sub_2.append(arr_sub[sub_i][sub_j+div_len]); next_sub_3.append(arr_sub[sub_i][sub_j+div_len+div_len]);
                            next_sub_4.append(arr_sub[sub_i+div_len][sub_j]); next_sub_5.append(arr_sub[sub_i+div_len][sub_j+div_len]); next_sub_6.append(arr_sub[sub_i+div_len][sub_j+div_len+div_len]);
                            next_sub_7.append(arr_sub[sub_i+div_len+div_len][sub_j]); next_sub_8.append(arr_sub[sub_i+div_len+div_len][sub_j+div_len]); next_sub_9.append(arr_sub[sub_i+div_len+div_len][sub_j+div_len+div_len])
                        next_arr_1.append(next_sub_1.copy()); next_arr_2.append(next_sub_2.copy()); next_arr_3.append(next_sub_3.copy())
                        next_arr_4.append(next_sub_4.copy()); next_arr_5.append(next_sub_5.copy()); next_arr_6.append(next_sub_6.copy())
                        next_arr_7.append(next_sub_7.copy()); next_arr_8.append(next_sub_8.copy()); next_arr_9.append(next_sub_9.copy())
                    recursion(next_arr_1); recursion(next_arr_2); recursion(next_arr_3)
                    recursion(next_arr_4); recursion(next_arr_5); recursion(next_arr_6)
                    recursion(next_arr_7); recursion(next_arr_8); recursion(next_arr_9)
                    return

    if arr_sub[0][0] == -1:
        minus_cnt += 1
    elif arr_sub[0][0] == 0:
        zero_cnt += 1
    elif arr_sub[0][0] == 1:
        one_cnt += 1
minus_cnt = 0
zero_cnt = 0
one_cnt = 0

# 함수 실행.
recursion(arr)

# 출력.
print(minus_cnt)
print(zero_cnt)
print(one_cnt)
