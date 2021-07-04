import sys
N, K = map(int ,input().split())

coin = []
for i in range(N):
    coin.append(int(sys.stdin.readline().rstrip()))

count_coin = 0
for i in range(N-1, -1, -1): # coin리스트 역순으로 받아와줌
    count_coin = count_coin + (K // coin[i]) # 나머지값 받아옴
    # print(count_coin)
    K = K % coin[i] # 몫값 가져와줌
    # print(K)

print(count_coin)