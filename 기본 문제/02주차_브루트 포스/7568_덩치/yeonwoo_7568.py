import sys

N = int(sys.stdin.readline().rstrip()) # 백준 제출용

result = []

for i in range(N):
    x, y = map(int, input().split())
    result.append([x,y])


for j in result:
    ranking = 1
    
    for k in result:
        if j[0] < k[0] and j[1] < k[1]:
            ranking = ranking + 1
            
    print(ranking, end = " ")