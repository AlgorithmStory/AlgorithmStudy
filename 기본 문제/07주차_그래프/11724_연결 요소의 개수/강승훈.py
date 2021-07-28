# 재귀 스택 리밋 늘림.
import sys
sys.setrecursionlimit(10 ** 6)

from sys import stdin

# 입력.
n,m = map(int, stdin.readline().split(" "))
arr = [[] for _ in range(n+1)]

# arr 인접 노드 관계 배열 생성.
for i in range(1, m+1):
    a,b = map(int, stdin.readline().split(" "))
    arr[a].append(b)
    arr[b].append(a)

# 방문 체크 딕셔너리.
alr_visited = {i:False for i in range(1,n+1)}

# 그래프 재귀 함수.
def graph_search(node):
    alr_visited[node] = True # 바로 방문 했다는 표시 해줌.
    for node_sub in arr[node]: # 인접 노드 하나씩 탐색하면서,
        if alr_visited[node_sub] == False: # 방문 하지 않았으면 재귀 함수 실행.
            graph_search(node_sub)

# 결과 변수.
result_cnt = 0

# 1번째 노드 부터, n+1번째 노드 까지 탐색.
for i in range(1,n+1):
    if alr_visited[i] == False: # 방문하지 않았으면 result_cnt 증가 해주고, 인접 노드 찾으러 함수 호출.
        result_cnt+=1
        graph_search(i)

# 출력.
print(result_cnt)
