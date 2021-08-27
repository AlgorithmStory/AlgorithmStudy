import sys
from sys import stdin
sys.setrecursionlimit(50000)

# 입력.
n = int(stdin.readline())

# 트리 구조 딕셔너리.
tree_dict = {}

# 입력.
for _ in range(n-1):
    a,b,c = map(int, stdin.readline().split(" "))
    if a not in tree_dict:
        tree_dict[a] = [[b, c]]
    else:
        tree_dict[a].append([b, c])

# 재귀 함수.
def recursion_tree_search(node):

    # 현재 node가 딕셔너리에 없으면, 끝이라는거임.
    if node not in tree_dict:
        return 0

    # 현재 노드의 리프노드가 1개면 diameter_sub의 값은 0임.
    diameter_main = 0
    diameter_sub = 0
    for crnt in tree_dict[node]: # 현재 노드의 리프노드 횟수만큼 돔.

        # 그걸 재귀하면서 현재 가중치와 누적.
        diameter_crnt = recursion_tree_search(crnt[0]) + crnt[1]

        # 현재 노드를 기준으로 가장 가중치가 긴 서브 리프를 main에 담음.
        if diameter_crnt > diameter_main:
            diameter_sub = diameter_main
            diameter_main = diameter_crnt
        elif diameter_crnt > diameter_sub:
            diameter_sub = diameter_crnt

    # sum은 현재 노드를 기준으로 가장 큰 지름을 나타냄.
    diameter_sum = diameter_main + diameter_sub

    # 그걸 글로벌로 비교해서, 매번 확인 갱신 해줌.
    global diameter_max
    if diameter_sum > diameter_max:
        diameter_max = diameter_sum

    # 현재 노드를 기준으로 가장 큰 가중치의 값을 리턴함.
    return diameter_main

diameter_max = 0
recursion_tree_search(1)

# 출력.
print(diameter_max, end="")
