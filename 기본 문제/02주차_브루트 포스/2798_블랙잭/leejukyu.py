N, M = map(int, input().split())
card = [int(x) for x in input().strip().split()]

a = 0

for i in range(0, N):
    for j in range(0, N):
        for k in range(0, N):
            if i != j and j != k and k != i:      # 숫자 세개가 겹치지 않는 순열 조합
                sum = card[i] + card[j] + card[k] # 숫자 세개 조합의 합
                if a <= sum <= M:               
                    a = sum                       # sum이 a 보다 크고 M보다 작으면 a 업데이트
print(a)                                          # for문이 다 돌았을 때 M보다 작은 가장 큰 값 프린트