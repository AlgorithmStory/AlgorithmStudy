from sys import stdin
n = int(stdin.readline()) # 입력.
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp_arr = [0 for _ in range(n+1)] # dp배열 초기화.
for i in range(n): # 끝까지 한번씩 돔.
    if dp_arr[i] < dp_arr[i - 1]: # 만약 현재 dp배열의 값이, 이전 인덱스의 값 보다 작다면, 큰 값을 원하므로, 갱신 시킴.
        dp_arr[i] = dp_arr[i - 1]
    if i+arr[i][0] > n: # 인덱스 범위 초과 방지.
        continue
    if dp_arr[i+arr[i][0]] < dp_arr[i]+arr[i][1]: # 다른 상담을 거친 경로의 값이 이미 dp배열에 존재할 수 있으므로, 비교하여.
        dp_arr[i+arr[i][0]] = dp_arr[i]+arr[i][1] # 현재까지 벌어들인 총 소득과, 오늘 날짜에 배정된 상담 업무를 수행 했을때 얻을 수 있는 수입의 합한 값을 dp배열에 업로드.
print(max(dp_arr)) # 결과.
