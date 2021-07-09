import sys

num_of_cities = int(sys.stdin.readline().split()[0])        # 도시 개수 입력
roads = list(map(int, sys.stdin.readline().split()))        # 도로 길이 입력
cities = list(map(int, sys.stdin.readline().split()))       # 도시 유가 입력
now_city = cities[0]                                        # 현재 도시 유가 = 시작 도시 유가
answer = 0                                                  # 정답 = 총 유가

for i in range(1, num_of_cities):                           # 2번 째 도시부터 루프
    answer += roads[i - 1] * now_city                       # 일단 현재 도시 유가로 온만큼 더해줌
    if cities[i] < now_city:                                # 해당 도시 유가가 현재 도시 유가보다 싸면
        now_city = cities[i]                                # 현재 도시 유가를 해당 도시 유가로 변경

print(answer)                                               # 정답 출력
