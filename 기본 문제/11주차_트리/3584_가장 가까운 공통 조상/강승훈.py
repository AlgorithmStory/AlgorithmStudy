import sys
sys.setrecursionlimit(50000)
from sys import stdin

# 트리 탐색 재귀.
def recursion(node):
    global tree_dict
    global result

    # 들어온 노드가 끝이면 바로 리턴.
    if node not in tree_dict:
        return node

    # 들어온 노드가, 입력으로 지정된 후손 중 하나이면 바로 리턴하는데,
    if node == descen_1 or node == descen_2:

        # 현재 노드의 리프 노드 중에, 우리가 찾고자 하는 후손이 더 있을 가능성이 있기 때문에, 여기서 한번더 재귀 돌려야됨.
        for i in range(len(tree_dict[node])):
            recive = recursion(tree_dict[node][i])
            if recive == descen_1 or recive == descen_2:
                result = node
                break
        return node

    # 재귀 탐색 포문.
    global visited
    des_1 = -1
    des_2 = -1
    for crnt in tree_dict[node]:
        if crnt not in visited:
            recive = recursion(crnt)
            visited.update([crnt])
            if recive == descen_1 or recive == descen_2:
                if des_1 == -1:
                    des_1 = recive
                elif des_2 == -1:
                    des_2 = recive
                    break

    # des_2가 -1이 아니라는건, 현재 노드의 리프노드에 우리가 찾고자하는 후손들이 다 있다는 의미임.
    if des_2 != -1:
        result = node
        return des_2
    return des_1

  
  
#  --------------- 여기서부터 입력과 함수 실행.
# 딕셔너리에 대해서 포문으로 재귀를 다 돌리는 이유는,
# 설계한 트리 자료구조의 형태가
# {1: [14, 13], 8: [5, 4, 1], 10: [16, 11, 2], 5: [9], 4: [6, 10], 6: [15, 7], 16: [3, 12]} 이런식의 인트:배열 구조라,
# 어디가 최 상단 노드인지 모르기 때문임.

# 입력.
test_case = int(stdin.readline())

# 테스트 케이스 만큼 돔.
for _ in range(test_case):

    # 입력과, 트리 자료구조 형성.
    n = int(stdin.readline())
    tree_dict = {}
    for _ in range(n-1):
        a,b = map(int, stdin.readline().split(" "))
        if a in tree_dict:
            tree_dict[a].append(b)
        else:
            tree_dict[a] = [b]

    # 각종 변수, 함수 실행과 조건에 의한 출력 탈출.
    des_1 = -1
    des_2 = -1
    descen_1, descen_2 = map(int, stdin.readline().split(" "))
    result = -1
    for node in tree_dict.keys():
        visited = set()
        recive = recursion(node)
        
        # result의 값이 -1이 아니라는건 방금 들어간 재귀에서 값을 찾았다는거임.
        if result != -1:
            print(result)
            break
        
        # 만약 리턴으로 받은 값이, 우리가 찾고자 하는 값 중 하나라면,
        if recive == descen_1 or recive == descen_2:
            if des_1 == -1:
                des_1 = recive
            elif des_2 == -1:
                print(node)
                break
