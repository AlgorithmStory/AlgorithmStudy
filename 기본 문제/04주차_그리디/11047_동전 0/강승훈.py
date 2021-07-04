from sys import stdin

# 입력.
n, m = map(int, stdin.readline().split(" "))
coin = [int(stdin.readline()) for _ in range(n)]
cnt = 0 # 필요한 동전의 개수.

# 뒤에서부터 동전 탐색.
for i in range(1, n+1):
    if m == 0:
        break
    if m >= coin[-i]: # 현재 가리키고 있는 동전이, 목표 값 보다 작거나 같으면,
        add_count = m//coin[-i] # 현재 동전에서 몇개를 가져 올건지 계산.
        m -= coin[-i]*add_count # 그 횟수 만큼, 동전과 곱하고, 목표 값 변수에 갱신 시킴.
        cnt += add_count # 몇개의 동전을 가져왔는지, cnt에 매번 갱신.

# 출력.
print(cnt)
