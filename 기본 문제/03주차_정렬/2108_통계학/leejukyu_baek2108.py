import sys
import collections

N = int(input())
a = [int(sys.stdin.readline().strip()) for _ in range(N)]
a.sort()                                                    # a 정렬

print(round(sum(a)/N))                                      # 평균

print(a[len(a)//2])                                         # 중앙값, N은 홀수라 여기까지만

lst = collections.Counter(a).most_common()                  # collections.Counter -> 문자열:카운팅을 튜플로 반환하는 내장함수, most_common -> 빈도수대로
if len(lst) >= 2:                                           # lst 값이 2개 이상일경우
    if lst[0][1] == lst[1][1]:                              # 첫번째 튜플과 두번째 튜플의 카운팅 수가 같다면
        print(lst[1][0])                                    # 두번째 튜플의 문자열이 최빈값
    else: print(lst[0][0])                                  # 가장 카운팅이 큰 수가 하나라면 첫번째 문자열이 최빈값
else: print(lst[0][0])

print(max(a)-min(a))                                        # 범위