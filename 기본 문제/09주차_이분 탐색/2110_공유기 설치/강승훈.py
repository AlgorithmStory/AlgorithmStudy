from sys import stdin

# 입력.
n,c  = map(int, stdin.readline().split(" "))
houses = [int(stdin.readline()) for _ in range(n)]

# 오름차순 정렬.
houses.sort()

# start와 end로 탐색할 범위 설정.
start = 1
end = houses[-1]-houses[0]

while start <= end:

    # 중앙값 구하고,
    mid = (start + end) // 2
    cnt = 1
    previous_value = houses[0]

    # houses를 순차적으로 탐색하는데, 중앙 값과, 이전의 house_value를 합친거보다 크거나 같으면 실행.
    for i in range(1, n):
        if houses[i] >= previous_value + mid:
            cnt += 1
            previous_value = houses[i]

    # 조건에 따라 분기.
    if cnt >= c:
        start = mid+1
    else:
        end = mid-1

# 출력.
print(end)
