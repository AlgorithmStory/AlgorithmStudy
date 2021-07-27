import sys
sys.setrecursionlimit(10**6)


class Node:                                                     # Node 클래스
    name: int                                                   # Node의 이름
    connection = []                                             # 이 Node와 이어진 Node 리스트

    def __init__(self, name):                                   # 생성자
        self.name = name                                        # 이 Node의 이름 정해줌
        self.connection = []                                    # 이 Node와 이어진 Node 리스트 초기화

    def add_connect(self, connect):                             # 이어진 Node 추가
        self.connection.append(connect)                         # -

    def get_name(self):                                         # 이 Node 이름 전달하는 메소드
        return self.name                                        # -


def infect(input_node: Node):                                   # 이어진 노드 확인하기
    input_node.name = -1                                        # 해당 Node는 체크되었다는 뜻으로 이름을 -1로 변경
    for i in input_node.connection:                             # 해당 Node와 이어진 Node 확인
        if i.name != -1:                                        # 이어진 Node가 아직 체크되지 않았으면
            infect(i)                                           # 이어진 Node로 이동해서 체크


def is_done(input_list):                                        # Node 리스트가 전부 체크되었는지 확인
    for i in input_list:                                        # Node 리스트 순회
        if i.get_name() != -1:                                  # Node 이름이 -1 이 아니면
            return False                                        # 바로 거짓 반환
    return True                                                 # 전부 -1 이면 참 반환


num_of_nodes, links = map(int, sys.stdin.readline().split())    # Node 개수와 연결 개수 읽어옴
answer = 0                                                      # 정답
nodes = [Node(x) for x in range(1, num_of_nodes + 1)]           # Node로 이루어진 리스트 생성

for i in range(links):                                          # 연결 개수 만큼 반복
    start, end = map(int, sys.stdin.readline().split())         # 연결된 두 개의 Node 이름 읽어옴
    nodes[start - 1].add_connect(nodes[end - 1])                # 두 개의 Node에 이어진 리스트 원소 추가
    nodes[end - 1].add_connect(nodes[start - 1])                # -

for i in nodes:                                                 # Node 리스트 순회
    if i.get_name() != -1:                                      # Node 리스트에 체크 안한게 있으면
        answer += 1                                             # 정답 증가
        infect(i)                                               # 체크 시작


print(answer)                                                   # 정답 출력

