import sys
N, L = map(int ,input().split())

holes = list(map(int, sys.stdin.readline().split()))
holes.sort() # 구멍위치 가까운 데 부터  들고옴
# print(holes)

tape_count = 0
start = 0
for i in holes: # 1, 2, 100, 101
    if start < i: # 순서대로 들고와서 start가 i보다 작으면
        # 0 < 1, 2 < 2 X, 2 <  100, 101 < 101 X = 2
        start = i + L -1 # 1 + 2 - 1 = 2, X, 100 + 2 - 1 = 101, X
        # 만약에 위치 1, 2에 구멍이 있으면 길이가 1이여서 L2인 테이프 하나로 막아짐
        # 위치 100, 101도 동일 
        tape_count = tape_count + 1# 1, 1, 2, 2

print(tape_count)# 2
