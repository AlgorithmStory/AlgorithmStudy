import sys
n, m = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.readline().split()]
start = 0
end = max(a)

while start <= end:
    sum = 0
    mid = (start + end) // 2                            # 중앙값 구하기
    for i in a:     
        if i > mid:                                     # 나무의 높이가 중앙값보다 크다면
            sum += i-mid                                # 큰 길이만큼 가져감
        if sum >= m:                                    # 다 더한게 m보다 크면
            break                                       # 더이상 계산 할 필요없음
    if sum < m:                                         # m보다 작으면
        end = mid - 1                                   # 왼쪽탐색
    else:                                               # m보다 크다면
        result = mid                                    # result에 저장
        start = mid + 1                                 # 오른쪽 탐색
print(result)                                           # 최종적으로 가장 큰 값이 저장됨