import sys

N = int(sys.stdin.readline().split()[0])                    # 탑의 개수
towers = list(map(int, sys.stdin.readline().split()))       # 탑의 높이 리스트
stack = [[0, 0]]                                            # 현재 가장 높은 탑의 스택
answer = []                                                 # 정답

for i, height in enumerate(towers):                         # 탑의 높이 리스트 탐색
    if stack[-1][1] < height:                               # 만약 스택의 마지막 탑의 높이가 현재 탑의 높이보다 작으면
        while len(stack) > 0 and stack[-1][1] < height:     # 높아질 때까지
            stack.pop(-1)                                   # 스택에서 하나씩 꺼냄
    if len(stack) == 0:                                     # 전부 꺼내서 스택에 남은게 없으면
        answer.append(0)                                    # 정답에 0 추가
    else:                                                   # 스택에 남은게 있으면
        answer.append(stack[-1][0] + 1)                     # 그거 추가
    stack.append([i, height])                               # 현재 탑을 다음에 올 탑들과 높이 비교를 위해 스택에 추가

print(*answer)                                              # 정답을 문제에서 원하는 형식으로 출력
