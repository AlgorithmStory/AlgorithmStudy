import sys
N = int(input())
T = []
P = []
for _ in range(N):
    t,p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

result = [0] * (N+1)                                        # 금액이 기록될 리스트

for i in range(N):
    n = i + T[i]                                            # i일에 T[i] 상담 일정을 더함 = 상담이 끝나는 날
    if result[i] < result[i-1]:                             # 당일이 전날보다 금액이 적으면
        result[i] = result[i-1]                             # 전날 금액으로 업데이트
    if n < (N+1):                                           # 퇴사 전날까지 상담이 끝나는 조건
        result[n] = max(P[i]+result[i] , result[n])         # 기록된 상담 금액과 새로운 상담 금액 중 큰 값을 저장

print(max(result))                                          # 가장 큰 값 프린트