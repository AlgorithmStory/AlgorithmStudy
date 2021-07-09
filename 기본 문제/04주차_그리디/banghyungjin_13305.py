import sys

num_of_cities = int(sys.stdin.readline().split()[0])        # 도시 개수 입력
roads = list(map(int, sys.stdin.readline().split()))        # 도로 길이 입력
cities = list(map(int, sys.stdin.readline().split()))       # 도시 유가 입력
now_city = cities[0]                                        # 현재 도시 유가 = 시작 도시 유가
answer = 0                                                  # 정답 = 총 유가
distance = 0                                                # 현재 유가로 이동할 거리

for i in range(1, num_of_cities):                           # 2번 째 도시부터 루프
    if cities[i] < now_city:                                # 해당 도시 유가가 현재 도시 유가보다 싸면
        answer += (roads[i - 1] + distance) * now_city      # (현재까지 더한 거리 + 바로 이전 거리) * 현재 도시 유가
        now_city = cities[i]                                # 현재 도시 유가를 해당 도시 유가로 변경
        distance = 0                                        # 이동할 거리 초기화
    else:                                                   # 해당 도시 유가가 현재 도시 유가보다 비싸면
        distance += roads[i - 1]                            # 거기서 기름을 사면 안되니까 이동할 거리를 늘림

answer += distance * now_city                               # 루프만 하면 마지막 거리가 정답에 추가 안되므로 직접 추가
print(answer)                                               # 정답 출력
