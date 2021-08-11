import sys
n, m = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
start = 0
end = max(a)

while start <= end:
    cnt = 0                                         # 랜선 길이
    mid = (start+end)//2                            # 중앙값 구하기
    for i in a:                                     # 랜선들을
        cnt += i//mid                               # 중앙값으로 나눈 몫을 다 더하면 랜선 길이
    if cnt < m:                                     # 필요 랜선 수 보다 작으면
        end = mid - 1                               # 왼쪽에서 탐색
    else:                                           # 랜선 수보다 크거나 같으면
        result = mid                                # 일단 중앙값 저장
        start = mid + 1                             # 오른쪽도 탐색

print(result)                                       # 최종적으로 랜선의 최대 길이가 저장됨
        