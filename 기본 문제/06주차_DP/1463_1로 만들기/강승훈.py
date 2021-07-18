# 입력.
n = int(input())

# n=3 까지의 결과 미리 저장.
dp_arr = [0,1,1]

# n이 3보다 크면, n까지.
for i in range(4, n+1):

    # 일단 현재 구하고자 하는 단계의 바로 전 단계 횟수 저장.
    sub_result = dp_arr[i-2]

    # 현재 숫자가 2로 나눠지고, 현재 단계에서 2를 나눈 단계의 횟수가, 방금 위에서 구한 전 단계 횟수보다 작다면, sub_result 갱신.
    if i % 2 == 0 and dp_arr[int(i / 2)-1] < sub_result:
        sub_result = dp_arr[int(i / 2)-1]

    # 현재 숫자가 3으로 나눠 떨어질때도 마찮가지.
    if i % 3 == 0 and dp_arr[int(i / 3)-1] < sub_result:
        sub_result = dp_arr[int(i / 3)-1]

    # 위의 3단계를 거친 결과에서, 1을 더한 값을 저장.
    dp_arr.append(sub_result+1)

# 출력.
print(dp_arr[n-1])
