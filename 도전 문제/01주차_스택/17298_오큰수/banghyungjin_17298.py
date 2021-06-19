import sys

count = int(input())                                    # 배열의 길이를 읽어오는데 쓸일은 없음
left = sys.stdin.readline().split()                     # 실제 배열 값을 읽어서 저장 (아직은 string 형식이라 int로 바꿔줘야 함)
right = []                                              # 오큰수를 찾는 스택 (left의 마지막 원소와 비교해서 answer에 들어갈 값을 계산)
answer = []                                             # 정답
for i in range(count):                                  # string 값이던 left를 int 값으로 변경
    left[i] = int(left[i])                              # --

while len(left) != 0:                                   # 기본적으로 left의 길이 만큼 while 문 실행
    while len(right) != 0 and right[-1] <= left[-1]:    # right에 값이 남아있을 때 right의 맨 윗 값이 left의 맨 윗 값보다 커질 때까지 (오큰수)
        right.pop()                                     # right 값을 버림 (right값이 left 값보다 작으면 필요없음)
    if len(right) == 0:                                 # right에 남은 값이 없으면
        answer.append(-1)                               # 오큰수가 없으니까 answer에 -1 추가
    else:                                               # 오큰수를 찾으면
        answer.append(right[-1])                        # answer에 오큰수 추가
    right.append(left.pop())                            # left의 마지막 값을 추후 오큰수 찾기에 써먹을려고 right 맨 뒤에 추가
answer.reverse()                                        # 위의 식으로는 정답이 뒤집어 져서 나오기 때문에 역순 정렬
print(*answer)                                          # 정답 출력 (이렇게 해야 답에서 원하는 대로 공백으로 나눠진 한 줄로 출력됨)