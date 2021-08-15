# 입력.
n = int(input())
countrys_arr = list(map(int, input().split(" ")))
budget = int(input())

# 이 범위 안에서 답을 찾을 거임.
init_min = 1
init_max = max(countrys_arr)

# init 값이 역전이 될때까지.
while init_min <= init_max:

    # 중앙 값 구해주고.
    mid = (init_min + init_max) // 2

    # sum_sub에 조건에따라 집행된 예산을 구함.
    sum_sub = 0
    for country in countrys_arr:
        if country <= mid:
            sum_sub += country
        else:
            sum_sub += mid
        if sum_sub > budget:
            break

    # 예산을 덜 썼으면, init_min값을 증가 시켜줌으로써, 최대 값을 찾아감.
    if sum_sub <= budget:
        init_min = mid + 1
    else: # 예산 초과면, init_max 값을 줄임으로써, 연산을 계속 함.
        init_max = mid - 1

# 출력.
print(init_max)
