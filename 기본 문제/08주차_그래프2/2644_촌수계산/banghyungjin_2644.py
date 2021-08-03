import sys
from collections import deque


class Person:                                                       # 사람 클래스
    name: int                                                       # 이름
    parent = None                                                   # 부모
    children = []                                                   # 자식

    def __init__(self, name):                                       # 생성자
        self.name = name                                            # -
        self.children = []                                          # -

    def set_parent(self, parent):                                   # 부모 설정 메소드
        self.parent = parent                                        # -

    def add_child(self, child):                                     # 자식 추가 메소드
        self.children.append(child)                                 # -

    def get_name(self):                                             # 사람 이름 반환 메소드
        return self.name                                            # -


def find_ancestor(input_person: Person):                            # 조상을 찾는 메소드
    stack = deque([input_person])                                   # 스택을 사용
    ancestors = []                                                  # 반환할 조상 리스트
    while stack:                                                    # 스택에 남은 사람이 있는 동안
        first = stack.popleft()                                     # 스택 맨 앞 사람 가져오기
        ancestors.append(first.get_name())                          # 해당 사람을 조상 리스트에 추가
        if first.parent is not None:                                # 만약 해당 사람의 부모가 존재하면
            stack.append(first.parent)                              # 다음 스택에 부모를 넣음
    return ancestors                                                # 정답 반환


n = int(sys.stdin.readline().split()[0])                            # 사람 수 읽어옴
people = [Person(x) for x in range(1, n + 1)]                       # 사람 리스트
start, end = map(int, sys.stdin.readline().split())                 # 촌수를 찾을 두 명 읽어옴
m = int(sys.stdin.readline().split()[0])                            # 사람 관계 수


for i in range(m):                                                  # 관계 수 만큼
    parent, child = map(int, sys.stdin.readline().split())          # 부모, 자식 관계 읽어옴
    people[parent - 1].add_child(people[child - 1])                 # 부모에게 자식을 추가
    people[child - 1].set_parent(people[parent - 1])                # 자식에게 부모를 설정

start_ancestor = find_ancestor(people[start - 1])                   # 한 쪽의 조상 리스트
end_ancestor = find_ancestor(people[end - 1])                       # 다른 쪽의 조상 리스트
answer = -1                                                         # 일단 정답을 -1로 초기화

for i in start_ancestor:                                            # 한 쪽의 조상 리스트를 순환
    if i in end_ancestor:                                           # 만약 공통된 조상이 있으면
        answer = start_ancestor.index(i) + end_ancestor.index(i)    # 두 사람에게서 해당 조상까지의 촌수를 구해 더함
        break                                                       # 반복문 탈출

print(answer)                                                       # 정답 출력
