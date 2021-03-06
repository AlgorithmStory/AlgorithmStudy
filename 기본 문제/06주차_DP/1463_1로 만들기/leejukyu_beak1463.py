n = int(input())

a = [0] * (n+1)                             # 최솟값이 기록될 리스트

for i in range(2, n+1):
    a[i] = a[i-1] + 1                       # 1을 뺀 경우를 저장

    if i%2 == 0:                            # 2로 나누어질 경우
        a[i] = min(a[i], a[i//2]+1)         # 1을 뺀 경우와 2로 나누어질 경우 중 적은 값을 기록
        
    if i%3 == 0:                            # 3으로 나누어질 경우, 2와 3 이 동시에 나누어질 경우 때문에 elif대신 if
        a[i] = min(a[i], a[i//3] + 1)       # 위에서 계산 된 최소값과 3으로 나누어질 경우 중 적은 값을 기록
        
print(a[n])