from sys import stdin

# 입력
n = int(input())
city_diff = list(map(int, stdin.readline().split(" ")))
cost_arr = list(map(int, stdin.readline().split(" ")))

result_cost_sum = 0 # 정답.
index = 0 # 도시랑 거리 찍을 인덱스.
while index < n-1:
    sum = 0 # 이동할 도시까지의 누적 거리.
    for j in range(index+1, n): # 현재 도시의 다음 도시부터 확인.
        sum += city_diff[j - 1] # 일단 현재 도시에서 바로 다음 도시까지 이동할 거리 입력.
        if cost_arr[index] >= cost_arr[j] or j == n-1: # 현재 도시의 기름값이 더 비싸면, 딱 그 구간 까지만 이동 함.
            result_cost_sum += cost_arr[index] * sum
            index = j-1
            break # 이동 했으면 index 갱신해줌.
    index += 1

# 출력.
print(result_cost_sum)
