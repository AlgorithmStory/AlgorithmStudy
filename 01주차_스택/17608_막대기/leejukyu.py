# a = 오른쪽부터 비교하는 입력 값, b = 비교 기준
# 가장 오른쪽에 있는것과 비교했을때 더 큰 것 만 보이니까 a>b로 비교
# a 가 b 보다 크면 뒤에 있는 것은 b 보다 커도 안보임
# 그래서 더 큰 값으로 b 업데이트

import sys

T = int(input())
a = [int(sys.stdin.readline()) for i in range(T)] # 입력

b = a[-1]
count = 1 # 보이는 갯수 카운트

# b보다 크면 카운트
for n in range(1, len(a)+1):
    if a[-n] > b:
        count += 1

        # b 업데이트
        b = a[-n]
print(count)