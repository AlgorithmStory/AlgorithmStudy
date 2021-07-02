import sys
from collections import Counter

length_of_list = int(sys.stdin.readline().split()[0])                               # 읽어올 리스트의 길이
numbers = [int(sys.stdin.readline().split()[0]) for _ in range(length_of_list)]     # 리스트 읽어옴
numbers.sort()                                                                      # 리스트 정렬
cnt = Counter(numbers).most_common()                                                # 최빈값을 찾기 위해 Counter 사용

print(round(sum(numbers) / length_of_list))                                         # 평균값 출력
print(numbers[length_of_list // 2])                                                 # 정렬된 리스트로 중앙값 출력

if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:                                         # 최빈값 출력 (최빈값이 2개 이상일 경우)
    print(cnt[1][0])                                                                # 두 번째 최빈값 출력
else:                                                                               # 최빈값이 하나일 경우
    print(cnt[0][0])                                                                # 최빈값 출력

print(max(numbers) - min(numbers))                                                  # 범위 출력
