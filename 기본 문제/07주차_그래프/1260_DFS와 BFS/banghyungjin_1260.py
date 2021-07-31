import sys
from collections import deque
# 클래스 만든거 계속 쓸려다 코드가 쓸데없이 길어졌습니다. ㅠㅠ

class Node:                                                     # 각 노드를 나타내는 클래스
    name: int                                                   # 노드의 이름
    connection = []                                             # 이 노드와 이어진 노드 리스트

    def __init__(self, name):                                   # 생성자
        self.name = name                                        # -
        self.connection = []                                    # -

    def add_connect(self, connect):                             # 이어진 노드 추가
        self.connection.append(connect)                         # -

    def get_name(self):                                         # 이 노드 이름 전달하는 메소드
        return self.name                                        # -

    def get_connection(self):                                   # 이 노드와 이어진 노드 리스트를 전달하는 메소드
        return self.connection                                  # -

    def do_sort(self):                                          # 이 노드와 이어진 노드 리스트를 정렬하는 메소드
        self.connection = sorted(self.connection,               # -
                                 key=lambda node: node.name)    # -

    def do_reverse_sort(self):                                  # 이 노드와 이어진 노드 리스트를 역정렬하는 메소드
        self.connection = sorted(self.connection,               # -
                                 key=lambda node: node.name, reverse=True)


def DFS(input_node: Node):                                      # DFS
    stack = deque([input_node])                                 # 스택을 사용
    answer = []                                                 # 반환할 정답
    while stack:                                                # 스택에 노드가 있는 동안
        first = stack.popleft()                                 # 스택 맨 앞 노드 가져오기
        if first.get_name() not in answer:                      # 만약 해당 노드를 방문하지 않았으면
            answer.append(first.get_name())                     # 정답 리스트에 추가
            for i in first.connection:                          # 해당 노드의 이어진 노드를 탐색
                if i.get_name() not in answer:                  # 이어진 노드를 방문하지 않았으면
                    stack.appendleft(i)                         # 스택에 추가해서 다음에 바로 방문
    return answer                                               # 정답 반환


def BFS(input_node: Node):                                      # BFS
    queue = deque([input_node])                                 # 큐를 사용
    answer = []                                                 # 반환할 정답
    while queue:                                                # 큐에 노드가 있는 동안
        first = queue.popleft()                                 # 큐의 맨 앞 노드 가져오기
        if first.get_name() not in answer:                      # 만약 해당 노드를 방문하지 않았으면
            answer.append(first.get_name())                     # 정답 리스트에 추가
            for i in first.connection:                          # 해당 노드의 이어진 노드를 탐색
                if i.get_name() not in answer:                  # 이어진 노드를 방문하지 않았으면
                    queue.append(i)                             # 큐에 추가해서 해당 깊이의 노드를 모두 방문한 뒤 방문
    return answer                                               # 정답 반환


N, M, V = map(int, sys.stdin.readline().split())                # 노드 개수 N, 연결 개수 M, 시작 노드 V 읽어오기
nodes = [Node(x) for x in range(1, N + 1)]                      # 노드의 리스트

for i in range(M):                                              # 노드의 리스트에 있는 노드들의 연결 상태를 반영해줌
    start, end = map(int, sys.stdin.readline().split())         # -
    nodes[start - 1].add_connect(nodes[end - 1])                # -
    nodes[end - 1].add_connect(nodes[start - 1])                # -

for i in nodes:                                                 # DFS를 위해
    i.do_reverse_sort()                                         # 이어진 노드 리스트를 역순 정렬 : 이래야 DFS에서 스택에 넣을 때 작은 순으로 들어감

print(*DFS(nodes[V - 1]))                                       # DFS 실행 후 결과 출력

for i in nodes:                                                 # BFS를 위해
    i.do_sort()                                                 # 이어진 노드 리스트를 정렬

print(*BFS(nodes[V - 1]))                                       # BFS 실행 후 결과 출력
