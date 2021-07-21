import sys

T = int(sys.stdin.readline().split()[0])                                            # T 읽어옴
stairs = []                                                                         # 계단 점수 리스트

for i in range(T):                                                                  # 계단 점수 리스트 읽어옴
    stairs.append(int(sys.stdin.readline().split()[0]))                             # -

costs = []                                                                          # 누적 계단 점수 리스트

for i in range(T):                                                                  # T 만큼 반복
    if i == 0:                                                                      # 1번 째는
        costs.append(stairs[0])                                                     # 그냥 1번 째
    elif i == 1:                                                                    # 2번 째는
        costs.append(sum(stairs[0:2]))                                              # 1번 째 + 2번 째
    elif i == 2:                                                                    # 3번 째는
        costs.append(max(stairs[0], stairs[1]) + stairs[2])                         # 앞의 두 개 중 큰거에 3번 째를 더한 것
    else:                                                                           # 그 이후로는
        costs.append(max(costs[i - 2], costs[i - 3] + stairs[i - 1]) + stairs[i])   # 1, 3, 4 처럼 2칸 1칸 순으로 밟는 것과 1, 3 처럼 바로 전에서 2칸 건넌 경우 2가지 중 큰거에서 현재 칸 더한것

print(costs[-1])                                                                    # 정답 출력
