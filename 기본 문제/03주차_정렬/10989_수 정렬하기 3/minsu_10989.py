# 배열 만들기
N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

# 카운팅 알고리즘
count = [0] * (max(array)+1)           # list의 요소들을 카운팅하기 위해 0으로 된 list 만들기

for i in range(len(array)):            # array의 요소를 count의 index로 받아서 +1씩 하기
    count[array[i]] += 1

# 출력
for i in range(len(count)):            # count의 길이의 범위 = array에서 최소값에서 최대값까지 범위
    for _ in range(count[i]):          # count의 i번째 있는 요소값 만큼 i를 print
        print(i)



# 백준용
from sys import stdin                  # 시간 초과를 막기 위해 input 대신 readline을 사용

N= int(stdin.readline())
count = [0] * 10001                    # 최대값이 10000이기 때문에 10001를 곱하여 0 ~ 10000까지 카운트 할 수 있는 count를 만듦

for i in range(N):
    count[int(stdin.readline())] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i)