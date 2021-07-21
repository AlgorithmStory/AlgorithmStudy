n = int(input()) # 입력.
dp_arr = [0,1,1] # 초기 값.
for _ in range(2, n):
    dp_arr[0] = dp_arr[1] # 매번 인덱스 3개의 값을 갱신해 주면서, 답을 찾아 나감 (메모리 절약).
    dp_arr[1] = dp_arr[2]
    dp_arr[2] = dp_arr[0] + dp_arr[1]
print(dp_arr[-1]) # 출력.
