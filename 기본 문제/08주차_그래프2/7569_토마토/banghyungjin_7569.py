import sys
from collections import deque
sys.setrecursionlimit(10**6)


def do_something(input_tomatoes, x, y, z, input_riped):                     # 토마토 익게 하는 BFS 메소드
    if x > 0 and input_tomatoes[x - 1][y][z] == 0:                          # 6방향으로 있는 토마토가 안익었으면
        input_tomatoes[x - 1][y][z] = input_tomatoes[x][y][z] + 1           # 현재 토마토의 숫자 + 1을 넣어줌
        input_riped.append([x - 1, y, z])                                   # BFS queue에 추가

    if x < H - 1 and input_tomatoes[x + 1][y][z] == 0:                      # 2
        input_tomatoes[x + 1][y][z] = input_tomatoes[x][y][z] + 1           # -
        input_riped.append([x + 1, y, z])                                   # -

    if y > 0 and input_tomatoes[x][y - 1][z] == 0:                          # 3
        input_tomatoes[x][y - 1][z] = input_tomatoes[x][y][z] + 1           # -
        input_riped.append([x, y - 1, z])                                   # -

    if y < N - 1 and input_tomatoes[x][y + 1][z] == 0:                      # 4
        input_tomatoes[x][y + 1][z] = input_tomatoes[x][y][z] + 1           # -
        input_riped.append([x, y + 1, z])                                   # -

    if z > 0 and input_tomatoes[x][y][z - 1] == 0:                          # 5
        input_tomatoes[x][y][z - 1] = input_tomatoes[x][y][z] + 1           # -
        input_riped.append([x, y, z - 1])                                   # -

    if z < M - 1 and input_tomatoes[x][y][z + 1] == 0:                      # 6
        input_tomatoes[x][y][z + 1] = input_tomatoes[x][y][z] + 1           # -
        input_riped.append([x, y, z + 1])                                   # -


def print_answer(input_tomatoes):                                           # 정답 함수
    answer = 0                                                              # 정답 0으로 초기화
    for i in input_tomatoes:                                                # 3차원 리스트 순회
        for j in i:                                                         # -
            for k in j:                                                     # -
                if k == 0:                                                  # 안 익은 토마토가 있으면
                    return -1                                               # -1 반환 후 메소드 종료
                elif k - 1 > answer:                                        # 익은 토마토이면
                    answer = k - 1                                          # 정답을 최대값으로 갱신
    return answer                                                           # 정답 반환


M, N, H = map(int, sys.stdin.readline().split())                            # 상자의 크기와 쌓인 상자의 개수 읽어옴
tomatoes = []                                                               # 토마토를 나타낼 3차원 리스트
riped_tomatoes = deque([])                                                  # BFS를 위한 queue

for height in range(H):                                                     # 토마토 3차원 리스트 내용 읽어옴
    tomato_box = []                                                         # 토마토 리스트에 들어갈 2차원 리스트
    for vertical in range(N):                                               # 2차원 리스트 내용 읽어옴
        input_tomato_box = list(map(int, sys.stdin.readline().split()))     # 2차원 리스트에 들아갈 1차원 리스트
        tomato_box.append(input_tomato_box)                                 # 2차원 리스트에 추가
        for horizontal in range(M):                                         # 1차원 리스트에서 이미 익은 토마토 위치 읽어옴
            if input_tomato_box[horizontal] == 1:                           # -
                riped_tomatoes.append([height, vertical, horizontal])       # BFS용 queue에 익은 토마토 위치 넣어줌
    tomatoes.append(tomato_box)                                             # 3차원 리스트에 2차원 리스트 추가

while riped_tomatoes:                                                       # queue에 원소가 남아있으면
    coord = riped_tomatoes.popleft()                                        # 남은 원소 중 제일 처음 거 뽑아옴
    do_something(tomatoes, coord[0], coord[1], coord[2], riped_tomatoes)    # BFS 실행

print(print_answer(tomatoes))                                               # 정답 함수 실행
