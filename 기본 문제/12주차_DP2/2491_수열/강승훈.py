from sys import stdin

# 입력.
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split(" ")))

# 바로 1칸 이전의 값만 필요하기 때문에, int 형으로 초기화.
increase_arr = 1
decrease_arr = 1

# 계산 하면서 매 순간 max 체크용 변수.
result_max = 1

for i in range(1, n):

    # 현재 배열과 이전의 배열을 비교해서, 조건에따라 처리함.
    if arr[i] > arr[i-1]:
        increase_arr += 1
        decrease_arr = 1
    elif arr[i] < arr[i-1]:
        decrease_arr += 1
        increase_arr = 1
    else:
        increase_arr += 1
        decrease_arr += 1

    # 매 순간 max 체크.
    if increase_arr > result_max:
        result_max = increase_arr
    if decrease_arr > result_max:
        result_max = decrease_arr

# 출력.
print(result_max)
