def do_something(input_number, count, max_number):
    if count == max_number:
        return 1
    elif input_number == 0:
        return do_something(0, count + 1, max_number) + do_something(1, count + 1, max_number)
    else:
        return do_something(0, count + 1, max_number)
# 재귀 함수로 만든 건데 시간 초과 뜸


N = int(input())                                    # N 읽어옴
answer = [1, 1]                                     # 정답 리스트 시작 부분

for i in range(2, N):                               # N 까지 반복
    answer.append(answer[i - 2] + answer[i - 1])    # 피보나치 수열 만듬 : 앞의 두 원소의 합이 현재 값

print(answer[N - 1])                                # 정답 출력
