from sys import stdin

# 입력.
testcase = int(stdin.readline())

# 정답 초기 리스트.
answer_arr = [0,1,2,2]

# N의 범위가 1000까지 이므로,
for i in range(4,1001):

    # 짝수면 n의 절반의 정답 + 바로 이전의 값.
    if i%2 == 0:
        answer_arr.append(answer_arr[i//2]+answer_arr[i-1])

    # 홀수면 바로 이전의 값.
    else:
        answer_arr.append(answer_arr[i-1])

# 출력.
for _ in range(testcase):
    print(answer_arr[int(stdin.readline())])
