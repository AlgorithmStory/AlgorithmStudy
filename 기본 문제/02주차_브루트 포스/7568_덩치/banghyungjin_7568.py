import sys

count = int(input())                                                    # 사람 수
people = []                                                             # 사람이 들어갈 배열 [몸무게, 키, 등수]
answer = []                                                             # 정답 배열

for i in range(count):                                                  # 사람 수만큼 사람 배열에 몸무게, 키를 읽어 넣음
    input_person = sys.stdin.readline().split()                         # --
    people.append([int(input_person[0]), int(input_person[1]), 1])      # 값을 int 형으로 변환, 등수를 1로 초기화

for i in people:                                                        # for 문 2번으로 전부 돌아 보며
    for j in people:                                                    # 하나씩 키와 몸무게 비교
        if j[0] > i[0] and j[1] > i[1]:                                 # 키와 몸무게가 전부 크면
            i[2] += 1                                                   # 등수가 하나 커짐

for i in people:                                                        # 등수만 읽어서 정답 배열에 넣음
    answer.append(i[2])                                                 # --

print(*answer)                                                          # 정답 출력
