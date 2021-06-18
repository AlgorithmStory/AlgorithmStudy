from sys import stdin

n = int(input())
sticks = [int(stdin.readline()) for _ in range(n)]

height_save = sticks[-1]
cnt = 1

for crnt in reversed(sticks):
    if crnt > height_save:
        cnt += 1
        height_save = crnt
        
print(cnt)
