import sys

N = int(sys.stdin.readline().rstrip()) # 백준 제출용

meet = []


for i in range(N):
    start_input, end_input = map(int ,input().split())
    meet.append([start_input, end_input]) 
    # meet에 start, end로 받아옴

# 참고 사이트 https://blankspace-dev.tistory.com/357
meet.sort(key = lambda x : x[0]) 
# meet의 start부분으로 먼저 sort한다
# 그러면 start가 작은것이 먼저 입력받은 대로 정렬됨
# print(meet)
meet.sort(key = lambda x : x[1])
# meet의 end부분으로 2차 sort한다.
# 위에서 이미 1차로 start로 정렬해서
# start 정렬된 순서로 입력 받으면서 end가 작은것이 먼저 정렬됨
# print(meet)

# 최종 meet의 첫번째 값에는 두번 정렬한 것을 다 만족하는 작은 값이 들어올거임
meet_max = 0
start_time = 0

for meet_time in meet: 
    if meet_time[0] >= start_time: # 시작 시간이 전에 끝난 시간보다 크거나 같으면
    # [1, 4] 1>=0, [5, 7] 5 >= 4, [8, 11] 8 >= 7, [12, 14] 12 >= 11
        start_time = meet_time[1] # start_time은 끝나는 시간으로 맞춰줌
        # 4, 7, 11, 14
        meet_max = meet_max + 1 # 1, 2, 3, 4

print(meet_max)