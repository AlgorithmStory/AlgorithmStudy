from sys import stdin

# 입력.
n,m = map(int, stdin.readline().split(" "))
lines_arr = [int(stdin.readline()) for _ in range(n)]

# 1과, 랜선중 가장 긴 길이를 초기 변수 값으로.
start = 1
end = max(lines_arr)

# start이 end 보다 작거나 같을때까지 while.
while start <= end:

    # start와 end의 중앙 값을 우선 구함.
    mid = (start+end)//2

    # 그 중앙 길이로 전체 랜선에 대해서 몇번 토막 낼수 있는지 구함.
    cut_cnt = 0
    for line in lines_arr:
        cut_cnt += line//mid

    # 그 토막낸 갯수가 구해야하는 갯수보다 적으면, end를 현재의 mid-1값으로 줄여서, 추후의 mid값도 줄어들게함.
    if cut_cnt < m:
        end = mid-1
    # 토막낸 갯수가 구해야하는 갯수보다 많으면, 토막나는 길이를 늘려서, 토막 갯수를 줄일 필요가 있음.
    else:
        start = mid+1

# 출력.
print(end)
