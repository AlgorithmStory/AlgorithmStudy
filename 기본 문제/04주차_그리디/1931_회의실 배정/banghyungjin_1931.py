import sys

num_of_meetings = int(sys.stdin.readline().split()[0])                  # 회의 수
meeting_list = []                                                       # 회의 리스트

for i in range(num_of_meetings):                                        # 회의 수 만큼
    meeting_list.append(list(map(int, sys.stdin.readline().split())))   # 회의 리스트에 회의 추가

meeting_list = sorted(meeting_list, key=lambda x: (x[1], x[0]))         # 회의 리스트를 회의 끝나는 순서 -> 회의 시작하는 순서로 정렬
now_meeting = meeting_list[0]                                           # 현재 진행중인 회의 == 맨 처음 회의
answer = 1                                                              # 정답
for i in range(1, len(meeting_list)):                                   # 두 번째 회의 부터 루프
    if meeting_list[i][0] >= now_meeting[1]:                            # 해당 회의가 현재 진행중인 회의가 끝나고 시작되면
        answer += 1                                                     # 정답 + 1
        now_meeting = meeting_list[i]                                   # 해당 회의를 현재 회의로 변경

print(answer)                                                           # 정답 출력
