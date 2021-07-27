import sys


class Node:                                                     # 각 컴퓨터를 나타내는 Node 클래스
    name: int                                                   # 컴퓨터의 이름
    connection = []                                             # 이 컴퓨터와 이어진 컴퓨터 리스트

    def __init__(self, name):                                   # 생성자
        self.name = name                                        # 이 컴퓨터의 이름 정해줌
        self.connection = []                                    # 이어진 컴퓨터 리스트 초기화

    def add_connect(self, connect):                             # 이어진 컴퓨터 추가
        self.connection.append(connect)                         # -

    def get_name(self):                                         # 이 컴퓨터 이름 전달하는 메소드
        return self.name                                        # -


def infect(input_node: Node):                                   # 감염시키기
    input_node.name = -1                                        # 해당 컴퓨터는 감염되었다는 뜻으로 이름을 -1로 변경
    for i in input_node.connection:                             # 해당 컴퓨터와 이어진 컴퓨터 확인
        if i.name != -1:                                        # 이어진 컴퓨터가 아직 감염되지 않았으면
            infect(i)                                           # 이어진 컴퓨터로 이동해서 감염


num_of_computers = int(sys.stdin.readline().split()[0])         # 컴퓨터 개수 읽어옴
num_of_links = int(sys.stdin.readline().split()[0])             # 연결 개수 읽어옴
answer = 0                                                      # 정답
computers = [Node(x) for x in range(1, num_of_computers + 1)]   # 컴퓨터 개수만큼 Node로 이루어진 리스트 생성

for i in range(num_of_links):                                   # 연결 개수 만큼 반복
    start, end = map(int, sys.stdin.readline().split())         # 연결된 두 개의 컴퓨터 이름 읽어옴
    computers[start - 1].add_connect(computers[end - 1])        # 두 개의 컴퓨터 Node에 이어진 리스트 원소 추가
    computers[end - 1].add_connect(computers[start - 1])        # -

infect(computers[0])                                            # 감염시키기

for i in computers:                                             # 컴퓨터 리스트 순회
    if i.get_name() == -1:                                      # 감염되었으면
        answer += 1                                             # 정답 증가

print(answer - 1)                                               # 1번 컴퓨터는 이미 감염된 채로 시작하므로 정답에서 제외

