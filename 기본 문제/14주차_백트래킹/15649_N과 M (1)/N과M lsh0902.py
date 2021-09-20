from itertools import permutations
N, S = map(int, input().split())
for n in permutations([i for i in range(1, N+1)], S):
    for num in n :
        print(num, end=' ')
    print()