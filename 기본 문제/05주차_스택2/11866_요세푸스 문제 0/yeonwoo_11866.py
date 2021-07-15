import sys
N, K = map(int ,sys.stdin.readline().split())

result = [] # result는 1~N까지 순서대로 배열
for i in range(1, N + 1):
    result.append(i)

pop_index = 0
prt = []
while result: # result가 빈 배열이 아닐때 까지
    pop_index = pop_index + (K - 1) 
    # 2, 4, 6, 3
    if pop_index > len(result) - 1:#2 > 6X, 4 > 5X, 6 > 4O...
        pop_index = pop_index % len(result) # 1
    
    prt.append(result.pop(pop_index)) 
    # [12 4567] [12 45 7] [1 45 7]
    # 3, 6, 2, 7...

# 출력 형식 안맞으면 틀렸다고 나옴...
print('<', end = '')
for i in prt[0:N-1]:
    print(i, end = ', ')

print(prt[N-1], end='')
print('>')