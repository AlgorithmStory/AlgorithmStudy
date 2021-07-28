import sys


class Person:                                               # 사람 클래스
    name: int                                               # 이름
    connection = []                                         # 친구 리스트

    def __init__(self, name):                               # 클래스 생성자
        self.name = name
        self.connection = []

    def add_connect(self, connect):                         # 친구 리스트 갱신 메소드
        self.connection.append(connect)

    def get_name(self):                                     # 사람 이름 반환 메소드
        return self.name


def invite(input_node: Person, counter):                    # 친구 초대 메소드
    if counter < 3:                                         # 두 다리 초과로 건너지 않았으면
        counter += 1                                        # 건넌 횟수 추가
        input_node.name = -1                                # 초대 했다는 뜻으로 이름을 -1로 바꿈
        for i in input_node.connection:                     # 해당 사람의 친구리스트 순회
            invite(i, counter)                              # 친구 리스트에 있는 다음 사람 초대 시작


num_of_people = int(sys.stdin.readline().split()[0])        # 친구 수 n
num_of_links = int(sys.stdin.readline().split()[0])         # 친구 관계의 수 m
answer = 0                                                  # 정답
people = [Person(x) for x in range(1, num_of_people + 1)]   # 친구 리스트 만듬

for i in range(num_of_links):                               # m 만큼 반복
    start, end = map(int, sys.stdin.readline().split())     # 친구 관계 읽어옴
    people[start - 1].add_connect(people[end - 1])          # 해당 친구 두 명의 친구리스트 갱신
    people[end - 1].add_connect(people[start - 1])          # -

invite(people[0], 0)                                        # 초대 시작

for i in people:                                            # 친구 리스트 순회
    if i.get_name() == -1:                                  # 초대 받았으면
        answer += 1                                         # 정답 추가

print(answer - 1)                                           # 1번은 자기 자신이므로 제거
