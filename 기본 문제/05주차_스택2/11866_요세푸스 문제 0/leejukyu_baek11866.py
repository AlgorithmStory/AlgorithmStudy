n, k = map(int,input().split())

a = [i for i in range(1, n+1)]
idx = 0                                 # index

print('<', end = '')
while len(a) > 1:                       # a 길이가 1보다 클때
    idx += k - 1                        # k만큼 더해주고 하나씩 리스트에서 빠지기 때문에 인덱스에도 1씩 빼준다
    if idx >= len(a):                   # 만약 인덱스가 a 길이 보다 크다면
        idx %= len(a)                   # a 길이를 나눈 나머지가 인덱스가 된다

    print(a.pop(idx), end = ', ')       # 해당 인덱스를 pop으로 빼준다
print(f'{a.pop()}>')                    # a에 하나만 남았을땐 그냥 빼준다