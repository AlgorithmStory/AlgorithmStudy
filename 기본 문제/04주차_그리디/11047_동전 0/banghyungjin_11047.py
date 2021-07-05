import sys

input_list = list(map(int, sys.stdin.readline().split()))                       # 읽어올 리스트의 길이
numbers = [int(sys.stdin.readline().split()[0]) for _ in range(input_list[0])]  # 돈 리스트 읽어옴
answer = 0                                                                      # 정답

for i in reversed(numbers):                                                     # 돈 리스트 역순 순회
    if i <= input_list[1]:                                                      # 현재 돈으로 뺄 수 있으면
        answer += input_list[1] // i                                            # 정답 갯수 추가
        input_list[1] %= i                                                      # 뺌
    if input_list[1] == 0:                                                      # 남은 돈이 없으면
        break                                                                   # 나감

print(answer)                                                                   # 정답 출력
