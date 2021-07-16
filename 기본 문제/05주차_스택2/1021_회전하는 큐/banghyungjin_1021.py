import sys

N, M = map(int, sys.stdin.readline().split())                           # N, M 읽어옴
queue = [x for x in range(1, N + 1)]                                    # 1부터 N까지 리스트 생성
wanted_numbers = [x for x in map(int, sys.stdin.readline().split())]    # 뽑아내려는 숫자 위치 읽어옴
answer = 0                                                              # 정답

for i in wanted_numbers:                                                # 뽑아내려는 숫자 개수 만큼 루프
    if queue.index(i) != 0:                                             # 만약 현재 뽑아내려는 숫자가 리스트 맨앞이 아니면
        answer += min(queue.index(i), len(queue) - queue.index(i))      # 왼쪽 오른쪽 이동 중 작은 쪽을 정답에 추가
        queue = queue[queue.index(i):] + queue[:queue.index(i)]         # 리스트를 현재 뽑아내려는 숫자가 맨앞에 오도록 변경
    del queue[0]                                                        # 리스트 맨앞을 제거

print(answer)                                                           # 정답 출력
