import sys

N = int(sys.stdin.readline().split()[0])    # N 읽어옴
answer = [0]                                # 1부터 N까지 숫자들의 연산횟수 리스트 : 0을 넣는거는 for 문에서 인덱스 편하게 쓸려고

for i in range(1, N + 1):                   # 1부터 N까지 루프
    if i == 1:                              # i가 1이면
        answer.append(0)                    # answer에 0추가
    elif i == 2 or i == 3:                  # i가 2나 3이면
        answer.append(1)                    # answer에 1추가
    else:                                   # 그 뒤로는
        temp = []                           # 예비 리스트
        if i % 2 == 0:                      # 현재 숫자가 2로 나눠 떨어지면
            temp.append(answer[i // 2])     # 예비 리스트에 2로 나눈 수의 연산 횟수 추가
        if i % 3 == 0:                      # 현재 숫자가 3으로 나눠 떨어지면
            temp.append(answer[i // 3])     # 예비 리스트에 3으로 나눈 수의 연산 횟수 추가
        temp.append(answer[i - 1])          # 예비 리스트에 1뺀 수의 연산 횟수 추가
        answer.append(min(temp) + 1)        # 예비 리스트 숫자 중 가장 작은 거에 1더한 게 현재 숫자의 연산 횟수

print(answer[-1])                           # 정답 출력
