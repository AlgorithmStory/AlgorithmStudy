# 환경 설정.
import sys
sys.setrecursionlimit(100000)
from sys import stdin

# 입력 받은 배열의 양 끝부터 가운데를 제외한 요소까지 탐색하면서 모두 비대칭이면 True.
# True라면 재귀적으로 분할해서 반복함.
# 도중에 한번이라도 False 나오면, 종료 하고 False 출력.
def recursion(info_sub):
    if len(info_sub) < 3:
        return True
    info_sub = info_sub.copy()
    next_sub_1 = []
    next_sub_2 = []
    for i in range((len(info_sub)//2)):
        if info_sub[i] == info_sub[-(i+1)]:
            return False
        else:
            next_sub_1.append(info_sub[i])
            next_sub_2.insert(0, info_sub[-(i+1)])
    if recursion(next_sub_1) and recursion(next_sub_2):
        return True
    return False

# 입력.
test_case = int(stdin.readline())

for _ in range(test_case):
    # 입력.
    info = list(stdin.readline().strip())
    if recursion(info):
        print("YES")
    else:
        print("NO")
