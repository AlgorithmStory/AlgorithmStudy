from sys import stdin

# 입력.
n = int(stdin.readline())
arr = list(list(stdin.readline().strip()) for _ in range(n))

# 제출 변수.
result = ""

# 재귀 함수.
def recursion(sub_arr):
    global result
    sub_arr = sub_arr.copy() # 복사 시킴.
    sub_arr_len = len(sub_arr) # 일단 들어온 파라미터에 대한 길이 구해 놓음.

    # 길이가 1이면 요소 담아주고 끝냄.
    if sub_arr_len == 1:
        result += sub_arr[0][0]
        return

    # 파라미터로 들어온 2차원 배열의 모든 요소를 탐색.
    for i in range(sub_arr_len):
        for j in range(sub_arr_len):
            # 4등분 해야되는 상황이 발생한다면,
            if sub_arr[i][j] != sub_arr[0][0]:
                result += "("
                next_arr_1 = []
                next_arr_2 = []
                next_arr_3 = []
                next_arr_4 = []
                for i_ in range(sub_arr_len//2):
                    next_sub_1 = []
                    next_sub_2 = []
                    next_sub_3 = []
                    next_sub_4 = []
                    for j_ in range(sub_arr_len // 2):
                        half_len = sub_arr_len//2
                        next_sub_1.append(sub_arr[i_][j_])
                        next_sub_2.append(sub_arr[i_][j_+half_len])
                        next_sub_3.append(sub_arr[i_+half_len][j_])
                        next_sub_4.append(sub_arr[i_+half_len][j_+half_len])
                    next_arr_1.append(next_sub_1.copy())
                    next_arr_2.append(next_sub_2.copy())
                    next_arr_3.append(next_sub_3.copy())
                    next_arr_4.append(next_sub_4.copy())

                # 담아서 재귀 실행.
                recursion(next_arr_1)
                recursion(next_arr_2)
                recursion(next_arr_3)
                recursion(next_arr_4)

                # 마지막은 괄호 닫아주기.
                result += ")"
                return

    # 만약 위의 탐색 포문에서, 모든 값이 같다면, 요소가 하나인 2차원 배열을 집어넣어줌.
    recursion([[sub_arr[0][0]]])

# 함수 실행.
recursion(arr)

# 출력.
print(result)
