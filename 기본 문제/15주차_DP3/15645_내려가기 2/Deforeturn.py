from sys import stdin
import sys
sys.setrecursionlimit(200000)

# min 찾는 함수.
def recursion_min(index_1, index_2):
    if index_1 < 0:
        return 0
    global memo
    key = str(index_1)+"|"+str(index_2)
    if key in memo:
        return memo[key]
    if index_2 == 0:
        memo[key] = min(recursion_min(index_1-1, index_2), recursion_min(index_1-1, index_2+1)) + matrix[index_1][index_2]
        return memo[key]

    if index_2 == 1:
        memo[key] = min(recursion_min(index_1-1, index_2-1), recursion_min(index_1-1, index_2), recursion_min(index_1-1, index_2+1)) + matrix[index_1][index_2]
        return memo[key]

    if index_2 == 2:
        memo[key] = min(recursion_min(index_1-1, index_2-1), recursion_min(index_1-1, index_2)) + matrix[index_1][index_2]
        return memo[key]

# max 찾는 함수.
def recursion_max(index_1, index_2):
    if index_1 < 0:
        return 0
    global memo
    key = str(index_1)+"|"+str(index_2)
    if key in memo:
        return memo[key]
    if index_2 == 0:
        memo[key] = max(recursion_max(index_1-1, index_2), recursion_max(index_1-1, index_2+1)) + matrix[index_1][index_2]
        return memo[key]

    if index_2 == 1:
        memo[key] = max(recursion_max(index_1-1, index_2-1), recursion_max(index_1-1, index_2), recursion_max(index_1-1, index_2+1)) + matrix[index_1][index_2]
        return memo[key]

    if index_2 == 2:
        memo[key] = max(recursion_max(index_1-1, index_2-1), recursion_max(index_1-1, index_2)) + matrix[index_1][index_2]
        return memo[key]

# 입력.
n = int(stdin.readline())
matrix = list(list(map(int, stdin.readline().split(" "))) for _ in range(n))
memo = dict() # 메모이제이션 용.

_min = min(recursion_min(n-1, 0), recursion_min(n-1, 1), recursion_min(n-1, 2))
memo.clear() # 메모이제이션 초기화.
_max = max(recursion_max(n-1, 0), recursion_max(n-1, 1), recursion_max(n-1, 2))

# 출력.
print(_max, _min)
