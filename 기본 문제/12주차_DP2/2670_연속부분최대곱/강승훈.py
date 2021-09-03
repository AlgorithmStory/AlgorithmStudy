from sys import stdin

# 입력.
n = int(stdin.readline())
arr = list(float(stdin.readline()) for _ in range(n))

# 탐색하면서 바로 이전의 값만 필요하므로, int 형으로 초기화.
pre_value = arr[0]

# 매 순간 max를 담을 변수.
result_max = arr[0]

for i in range(1, n):

    # 현재 값과, 이전까지의 최대값과 곱한거 중 큰거를 담음.
    pre_value = max(arr[i], pre_value*arr[i])

    # 매번 max 체크.
    if pre_value > result_max:
        result_max = pre_value

# 소수점 4째 반올림 출력.
# ex) 1.3이 아니라 1.300으로 출력해야 한다는게 함정 이었음.
print("%.3f" % result_max)
