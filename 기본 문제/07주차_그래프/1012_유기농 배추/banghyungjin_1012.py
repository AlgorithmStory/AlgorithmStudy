import sys
sys.setrecursionlimit(10**6)                            # 결국 서로 이어진 덩어리가 몇 개인지 찾아내는것


def do_something(land, cabbage):                        # 이어진 덩어리가 몇 개인지 찾는 메소드
    x = cabbage[0]                                      # 현재 배추가 있는 곳의 x 축 좌표
    y = cabbage[1]                                      # 현재 배추가 있는 곳의 y 축 좌표
    land[x][y] = -1                                     # 현재 배추가 있는 곳을 -1 로 체크 함
    # 아래 if 문 4개는 현재 배추가 있는 곳에서 사방으로 배추가 있는지 검사한 후 있으면 거기에 대해 현재 메소드를 다시 실행
    if x > 0 and land[x - 1][y] == 1:
        do_something(land, [x - 1, y])
    if x < len(land) - 1 and land[x + 1][y] == 1:
        do_something(land, [x + 1, y])
    if y > 0 and land[x][y - 1] == 1:
        do_something(land, [x, y - 1])
    if y < len(land[1]) - 1 and land[x][y + 1] == 1:
        do_something(land, [x, y + 1])


T = int(sys.stdin.readline().split()[0])                # 테스트 케이스 개수 T 읽어옴

for t in range(T):                                      # T 만큼 반복
    M, N, K = map(int, sys.stdin.readline().split())    # 가로 M, 세로 N, 배추 개수 K 읽어옴
    land = []                                           # 배추밭을 나타내는 리스트
    cabbages = []                                       # 배추가 있는 좌표를 나타내는 리스트
    count = 0                                           # 덩어리의 개수
    for i in range(N):                                  # 배추밭 리스트를 일단 0으로 전부 채움
        land.append([0 for x in range(M)])              # -

    for i in range(K):                                  # K 만큼
        x, y = map(int, sys.stdin.readline().split())   # 배추 위치 좌표 읽어옴
        cabbages.append([y, x])                         # 배추 좌표 리스트에 채워 줌
        land[y][x] = 1                                  # 배추밭 리스트의 해당 좌표를 1로 바꿈

    for i in cabbages:                                  # 배추 좌표 리스트 순회
        if land[i[0]][i[1]] == 1:                       # 만약 해당 배추 좌표가 가리키는 곳에 배추가 아직 1이면
            count += 1                                  # 덩어리 개수 추가
            do_something(land, i)                       # 이어진 배추 전부 -1로 바꿈

    print(count)                                        # 덩어리 개수 출력
