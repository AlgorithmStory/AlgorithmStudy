import sys

T = int(sys.stdin.readline().split()[0])                                        # T 읽어옴

for i in range(T):                                                              # T 만큼 반복
    n = int(sys.stdin.readline().split()[0])                                    # n 읽어옴
    numbers = [0, 1, 2, 4]                                                      # 정답 계산용 리스트 : n이 3일 때 까지 넣어줌

    if n < 4:                                                                   # n 이 4미만이면
        print(numbers[n])                                                       # 리스트에서 바로 찾아 정답 출력
    else:                                                                       # n 이 4이상이면
        for j in range(4, n + 1):                                               # 4부터 n까지 반복
            numbers.append(numbers[j - 3] + numbers[j - 2] + numbers[j - 1])    # 해당 칸의 앞의 3칸의 숫자를 더해서 해당 칸에 넣음
        print(numbers[-1])                                                      # 정답 출력
