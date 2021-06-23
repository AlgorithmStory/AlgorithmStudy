import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    k = list(map(int, sys.stdin.readline().split()))
    lst.append(k)
num = []
 
for i in range(N):
    cnt = 1
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt +=1
    num.append(cnt)
print(*num)