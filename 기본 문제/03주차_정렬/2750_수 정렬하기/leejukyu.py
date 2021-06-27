import sys

N = int(input())
a = [int(sys.stdin.readline()) for _ in range(N)]

for i in range(1, len(a)):
    for j in range(0,len(a)-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

for k in range(len(a)):
    print(a[k])