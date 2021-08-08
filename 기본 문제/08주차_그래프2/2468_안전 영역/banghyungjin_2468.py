import sys
import copy
sys.setrecursionlimit(10**6)


def do_something(temp_province, x, y, height):                              # 현재 침수되지 않은 지역들의 개수 구하는 메소드
    temp_province[x][y] = -1                                                # 현재 좌표의 지역은 방문했다고 체크
                                                                            # 인접한 4개 지역에 대해 방문여부와 침수여부를 체크
    if x > 0 and temp_province[x - 1][y] > height:                          # 방문하지 않았고 침수되지 않았으면
        do_something(temp_province, x - 1, y, height)                       # 해당 부분에 대해 재귀 메소드 실행
    if x < len(temp_province) - 1 and temp_province[x + 1][y] > height:     # -
        do_something(temp_province, x + 1, y, height)                       # -
    if y > 0 and temp_province[x][y - 1] > height:                          # -
        do_something(temp_province, x, y - 1, height)                       # -
    if y < len(temp_province[1]) - 1 and temp_province[x][y + 1] > height:  # -
        do_something(temp_province, x, y + 1, height)


N = int(sys.stdin.readline().split()[0])                                    # 지역의 가로 세로 길이 읽어옴
province = []                                                               # 지역의 높이를 나타낼 리스트
answer = []                                                                 # 각 침수높이에 대해 남은 지역 개수 리스트

for _ in range(N):                                                          # N만큼 반복
    province.append(list(map(int, sys.stdin.readline().split())))           # 지역 리스트 내용 읽어옴

for i in range(max(max(province))):                                         # 0부터 가장 높은 지역의 높이 까지 침수 시작
    temp_province = copy.deepcopy(province)                                 # 계산에 쓸 지역 리스트 복사판
    count = 0                                                               # 남아있는 지역 개수
    for x in range(N):                                                      # 지역 리스트 순회
        for y in range(N):                                                  # -
            if temp_province[x][y] > i:                                     # 아직 침수되지 않았고 방문하지 않았으면
                count += 1                                                  # 지역 개수 + 1
                do_something(temp_province, x, y, i)                        # 메소드 실행
    answer.append(count)                                                    # 해당 침수에서 남은 지역들 개수 리스트에 추가

print(max(answer))                                                          # 정답 출력
