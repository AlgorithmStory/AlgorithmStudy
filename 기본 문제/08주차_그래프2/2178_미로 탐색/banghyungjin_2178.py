import sys
from collections import deque
# 클래스를 계속 사용했더니 시간이 많이 느려져서 pypy3로 제출했어요 


class Node:                                                                         # 각 노드를 나타내는 클래스
    name = ""                                                                       # 노드의 이름
    coord = []                                                                      # 노드의 좌표
    connection = []                                                                 # 이 노드와 이어진 노드 리스트
    depth: int                                                                      # 시작 노드에서 해당 노드까지의 거리

    def __init__(self, name, now_coord):                                # 생성자
        self.name = name                                                            # -
        self.connection = []                                                        # -
        self.coord = now_coord                                                      # -
        self.depth = 0                                                              # -

    def add_connect(self, connect):                                                 # 이어진 노드 추가
        self.connection.append(connect)                                             # -

    def set_depth(self, depth):                                                     # 이어진 노드 추가
        self.depth = depth                                                          # -

    def get_name(self):                                                             # 이 노드 이름 전달하는 메소드
        return self.name                                                            # -

    def get_connection(self):                                                       # 이 노드와 이어진 노드 리스트를 전달하는 메소드
        return_connection = [x.coord for x in self.connection]                      # -
        return return_connection                                                    # -

    def get_coord(self):                                                            # 이 노드의 좌표를 전달하는 메소드
        return self.coord                                                           # -

    def get_depth(self):                                                            # 이 노드와 목적지 노드 간의 거리를 전달하는 메소드
        return self.depth                                                           # -


def BFS(input_node, goal_coords):                                                   # BFS
    input_node.set_depth(1)                                                         # 시작 노드의 depth를 1로 맞춤
    queue = deque([input_node])                                                     # 큐를 사용
    answer = []                                                                     # 추후 방문 리스트
    while queue:                                                                    # 큐에 노드가 있는 동안
        first = queue.popleft()                                                     # 큐의 맨 앞 노드 가져오기
        if first not in answer:                                                     # 만약 해당 노드를 방문하지 안았는데
            if first.get_coord() == goal_coords:                                    # 해당 노드가 목적지면
                return first.get_depth()                                            # 해당 노드 depth 반환
            answer.append(first)                                                    # 아니면 추후 방문 리스트에 추가
            for i in first.connection:                                              # 해당 노드의 이어진 노드를 탐색
                if i not in answer:                                                 # 이어진 노드를 방문하지 않았으면
                    if i.get_depth() == 0 or i.get_depth() > first.get_depth():     # 이어진 노드의 depth와 이전 노드의 depth + 1 중 작은 걸
                        i.set_depth(first.get_depth() + 1)                          # 이어진 노드의 depth로 변경
                    queue.append(i)                                                 # 큐에 추가해서 해당 깊이의 노드를 모두 방문한 뒤 방문


N, M = map(int, sys.stdin.readline().split())                                       # 가로 N, 세로 M 읽어옴
maze = []                                                                           # 미로를 나타내는 리스트

for i in range(N):                                                                  # 미로 리스트 읽어옴
    input_line = list(sys.stdin.readline().split()[0])                              # -
    maze.append([Node(input_line[x], [i, x])                                        # -
                 for x in range(len(input_line))])                                  # -

for i in range(len(maze)):                                                          # 미로 리스트 한 번씩 순회
    for j in range(len(maze[i])):                                                   # 각 칸과 이어진 칸을 갱신
        if maze[i][j].get_name() == '1':                                            # -
            if i > 0 and maze[i - 1][j].get_name() == '1':                          # -
                maze[i][j].add_connect(maze[i - 1][j])                              # -
            if i < N - 1 and maze[i + 1][j].get_name() == '1':                      # -
                maze[i][j].add_connect(maze[i + 1][j])                              # -
            if j > 0 and maze[i][j - 1].get_name() == '1':                          # -
                maze[i][j].add_connect(maze[i][j - 1])                              # -
            if j < M - 1 and maze[i][j + 1].get_name() == '1':                      # -
                maze[i][j].add_connect(maze[i][j + 1])                              # -

answer = BFS(maze[0][0], [N - 1, M - 1])                                            # BFS 사용
print(answer)
