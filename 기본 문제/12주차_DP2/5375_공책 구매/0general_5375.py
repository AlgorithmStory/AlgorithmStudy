'''
https://www.acmicpc.net/problem/5375
'''
# Test case
t = int(input())

for _ in range(t):
    g = []
    n, m = map(int, input().split())  # 공책 수, 쇼핑몰 수
    for _ in range(m):
        g.append(list(map(int, input().split())))  # 개수, 가격, 배송비
    sum = 0
    i = 0
    while n:
        #print("현재 장바구니 상태 : ", g)
        g.sort()
        min = 100000001
        idx = i
        x = g[i][0]
        if n < x:
            x = n
        for c in range(i, m):
            if x*g[c][1] + g[c][2] < min:
                min = x*g[c][1] + g[c][2]
                idx = c
        sum += min
        n -= x
        g[idx][0], g[idx][2] = g[idx][0]-x, 0
        if g[idx][0] == 0:
            i += 1

    print(sum)
