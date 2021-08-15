import sys
n, m = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.readline().split()]
start = 0
end = max(a)

if sum(a) >= n:                                         # 길이 1이라도 과자를 나눠줄 수 있는 경우
    while start <= end:
        cnt = 0                                         
        mid = (start+end)//2                            # 중앙값 구해서
        for i in a:                                     # 리스트 하나씩
            cnt += i//mid                               # 줄 수 있는 과자 개수 카운트
        if cnt < n:                                     # 조카 수 보다 적으면
            end = mid - 1                               # 길이 줄여서 탐색
        else:                                           # 조카 수 보다 많으면
            result = mid                                # 중앙값 저장
            start = mid + 1                             # 길이 늘려서 탐색
else:                                                   # 과자를 나눠 줄 수 없는 경우
    result = 0                                          # 0 반환

print(result)                                      
        