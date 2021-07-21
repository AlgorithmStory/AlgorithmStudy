import sys
n = int(input())

a = [int(sys.stdin.readline()) for _ in range(n)]

result = [0] * (n+1)                                                    # 최대값을 담을 리스트

for i in range(1, len(a)+1):
    if i == 1:
        result[i] = a[0]                                                # 첫번째 칸은 a[0] 가 최대값
    elif i == 2:
        result[i] = a[0] + a[1]                                         # 두번째 칸은 앞에 두개 밟은게 최대값
    else:
        result[i] = max(result[i-3]+a[i-2], result[i-2]) + a[i-1]       # 세번째 부터는 한 칸 전을 밟지 않고 그 전 두칸을 밟은 것과 직전 칸을 밟은 경우 중 큰 값이 최대값
print(result[-1])