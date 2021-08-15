import sys
n = int(input())
a = [int(x) for x in sys.stdin.readline().split()]
m = int(input())
start = 1
end = max(a)

if sum(a) <= m:                                             # 모든 요청의 합이 예산보다 작다면
    result = max(a)                                         # 배정된 예산들 중 최댓값 출력
else:                                                       # 아니면 상한액 찾기
    while start <= end:
        cost = 0
        mid = (start + end) //2                             # 중앙값 계산
        for i in a:                                         # 리스트 하나씩 탐색
            if i <= mid:                                    # 요청이 중앙값 보다 작으면
                cost += i                                   # 요청 금액 그대로 배정
            else:                                           # 중앙값 보다 크면
                cost += mid                                 # 중앙값 만큼만 저장
        if cost > m:                                        # 총 예산 보다 요청 금액이 크면
            end = mid -1                                    # 금액 줄여서 다시 탐색
        else:                                               # 요청 금액이 총 예산보다 적으면
            result = mid                                    # 중앙값 저장
            start = mid + 1                                 # 금액 늘려서 다시 탐색
print(result)