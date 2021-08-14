# 입력.
n,m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

# start ~ end 사이에 답이 있음.
start = 1
end = max(arr)

# start와 end가 역전 될때까지.
while start <= end:

    # 중앙 값 구해주고.
    mid = (start+end)//2

    # 먹인 조카 카운트.
    nehpew_cnt = 0
    for crnt in arr:
        if crnt >= mid:
            nehpew_cnt += crnt//mid

    # 만약 모든 조카에게 다 먹였다면, 막대과자를 더 먹을 수 있는 여지가 있음.
    if nehpew_cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

# 출력.
print(end)
