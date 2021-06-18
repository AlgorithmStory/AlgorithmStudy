import sys

count = int(input())    # 첫줄의 리스트 원소 숫자 읽어옴
list_input = []         # 막대기의 리스트
answer = 0              # 보이는 막대기의 숫자 = 정답
for i in range(count):  
    list_input.append(int(sys.stdin.readline().split()[0])) # 배열에 순서대로 막대기를 넣어줌
prev = 0    # 막대기 길이 비교용 초기값
for i in range(count):  # 배열에 넣은 역순으로 막대기를 뺌
    now = list_input.pop()  # 뺀 막대기 길이
    if now > prev:  # 뺀 막대기가 초기값, 이전에 뺀 막대기 길이보다 길다면?
        prev = now  # 현재 보이는 길이중 제일 긴 길이로 교체
        answer += 1 # 보이는 막대기의 숫자를 1개 올림
print(answer)       # 정답 반환