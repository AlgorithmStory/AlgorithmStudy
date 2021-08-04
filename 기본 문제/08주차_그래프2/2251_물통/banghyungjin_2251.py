import sys
from collections import deque


def BFS():                                          # BFS
    queue = deque([[0, 0, C]])                      # 처음 물통 상태
    answers = []                                    # 정답 리스트
    checked = []                                    # 이전에 있었던 물통 상태 체크리스트
    while queue:                                    # 큐에 뭐가 있는 동안
        a, b, c = queue.popleft()                   # 큐 맨처음 물통 상태 읽어옴
        if a == 0 and c not in answers:             # 만약 첫 물통이 비어있고 세 번째 물통의 양이 새로운 숫자면
            answers.append(c)                       # 정답 리스트에 추가
        if [a, b, c] not in checked:                # 만약 현재 물통 상태가 이전에 나온 적 없으면 6 종류의 다음 상태를 전부 queue에 넣음
            if a + b > B:                           # 1: 담을 통에 물이 넘칠 때
                queue.append([a - (B - b), B, c])
            else:                                   # -: 물이 안넘칠 때
                queue.append([0, a + b, c])
            if a + c > C:                           # 2
                queue.append([a - (C - c), b, C])
            else:
                queue.append([0, b, a + c])
            if b + a > A:                           # 3
                queue.append([A, b - (A - a), c])
            else:
                queue.append([a + b, 0, c])
            if b + c > C:                           # 4
                queue.append([a, b - (C - c), C])
            else:
                queue.append([a, 0, b + c])
            if c + a > A:                           # 5
                queue.append([A, b, c - (A - a)])
            else:
                queue.append([a + c, b, 0])
            if c + b > B:                           # 6
                queue.append([a, B, c - (B - b)])
            else:
                queue.append([a, b + c, 0])
            checked.append([a, b, c])               # 해당 물통 상태를 이전에 나온 적 있다고 체크
    return answers                                  # 정답 리스트 반환


A, B, C = map(int, sys.stdin.readline().split())    # 물통 용량 읽어옴
print(*sorted(BFS()))                               # 정답 계산 후 출력
