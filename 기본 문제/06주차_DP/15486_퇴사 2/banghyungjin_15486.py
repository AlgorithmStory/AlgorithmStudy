from sys import *

N = int(stdin.readline().split()[0])    # N 읽어옴
counseling = [list(map(int, stdin.readline().split())) for _ in range(N)]   # 각 상담의 소요시간, 보수
answer = [0 for _ in range(N + 1)]      # 정답 리스트

for i in range(N):                      # N 만큼 반복
    if answer[i] < answer[i-1]:         # 만약 전날 까지 벌 수 있는 돈이 더 많으면
        answer[i] = answer[i-1]         # 오늘 날짜 벌 수 있는 돈을 바꿔줌
    if i + counseling[i][0] < N + 1:    # 오늘 상담이 퇴사 전에 끝나면
        answer[i + counseling[i][0]] = max(answer[i + counseling[i][0]], counseling[i][1] + answer[i])
                                        # 해당 끝나는 날짜의 보수, (오늘 날짜 벌수있는 돈 + 오늘 일 보수) 중 큰 거 선택해서 넣어줌
print(max(answer))                      # 정답 출력
