import sys

n, m = map(int, input().split())                                                # N, M 입력

lst = [sys.stdin.readline() for _ in range(n)]                                  # 입력값 리스트로 생성

num_1 = []
num_2 = []

for x in range(n-7):                                                            # 8개씩 묶어주는 박스 왼쪽 x 기준
    for y in range(m-7):                                                        # 8개씩 묶어주는 박스 윗쪽 y 기준
        cnt_1 = 0                                                               # 다시 칠해야하는 수 카운트
        for i in range(x, x+8):                                                 # 박스 x축 한 칸씩 이동
            for j in range(y, y+8):                                             # 박스 y축 한 칸씩 이동
                if (i-x) % 2 == 0 and (j-y) % 2 == 0 and lst[i][j] != 'W':      # i, j 에 x축 y축 값을 빼줘서 박스 가장 위 왼쪽을 0,0으로
                    cnt_1 += 1                                                  # 첫 번째 칸이 W 일 경우 W가 아니면 카운트
                elif (i-x) % 2 != 0 and (j-y) % 2 == 0 and lst[i][j] != 'B':    # 순서대로 인덱스 x축이 짝 이고 y축이 짝 인 경우 W가 아니면 카운트
                    cnt_1 += 1                                                  # x축이 홀 이고 y축이 짝 인 경우 B가 아니면 카운트
                elif (i-x) % 2 != 0 and (j-y) % 2 != 0 and lst[i][j] != 'W':    # x축이 홀 이고 y축이 홀 인 경우 W가 아니면 카운트
                    cnt_1 += 1
                elif (i-x) % 2 == 0 and (j-y) % 2 != 0 and lst[i][j] != 'B':    # x축이 짝 이고 y축이 홀 인 경우 B가 아니면 카운트
                    cnt_1 += 1
        num_1.append(cnt_1)                                                     # 8X8 박스가 움직일때마다 카운트 한거 리스트에 넣기

        cnt_2 = 0
        for i in range(x, x+8):                                                 # 첫 번째 칸이 B일 경우 위와 같이 카운트
            for j in range(y, y+8):
                if (i-x) % 2 == 0 and (j-y) % 2 == 0 and lst[i][j] != 'B':
                    cnt_2 += 1
                elif (i-x) % 2 != 0 and (j-y) % 2 == 0 and lst[i][j] != 'W':
                    cnt_2 += 1
                elif (i-x) % 2 != 0 and (j-y) % 2 != 0 and lst[i][j] != 'B':
                    cnt_2 += 1
                elif (i-x) % 2 == 0 and (j-y) % 2 != 0 and lst[i][j] != 'W':
                    cnt_2 += 1

        num_2.append(cnt_2)
num = num_1 + num_2                                                             # W로 시작한 경우와 B로 시작한 경우를 다 비교 하기 위해 합쳐줌

print(min(num))                                                                 # 가장 적은 수를 프린트