# 전형적인 DP문제
# https://www.acmicpc.net/problem/2670

n = int(input())
data = [float(input()) for _ in range(n)]

for i in range(1, n):
    data[i] = max(data[i], data[i-1]*data[i])

print("%.3f" % (max(data)))
