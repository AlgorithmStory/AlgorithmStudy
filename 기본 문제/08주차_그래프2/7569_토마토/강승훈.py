from sys import stdin

# 상하좌우 위층 아래층 탐색 함수.
def my_bfs(indexs):
    global sub_arr
    if indexs[0] + 1 < h and space_arr[indexs[0] + 1][indexs[1]][indexs[2]] == 0:
        space_arr[indexs[0]+1][indexs[1]][indexs[2]] = 1
        sub_arr.append([indexs[0]+1, indexs[1], indexs[2]])

    if indexs[0] - 1 >= 0  and space_arr[indexs[0] - 1][indexs[1]][indexs[2]] == 0:
        space_arr[indexs[0]-1][indexs[1]][indexs[2]] = 1
        sub_arr.append([indexs[0]-1, indexs[1], indexs[2]])

    if indexs[1] + 1 < n and space_arr[indexs[0]][indexs[1] + 1][indexs[2]] == 0:
        space_arr[indexs[0]][indexs[1] + 1][indexs[2]] = 1
        sub_arr.append([indexs[0], indexs[1] + 1, indexs[2]])

    if indexs[1] - 1 >= 0 and space_arr[indexs[0]][indexs[1] - 1][indexs[2]] == 0:
        space_arr[indexs[0]][indexs[1] - 1][indexs[2]] = 1
        sub_arr.append([indexs[0], indexs[1] - 1, indexs[2]])

    if indexs[2] + 1 < m and space_arr[indexs[0]][indexs[1]][indexs[2] + 1] == 0:
        space_arr[indexs[0]][indexs[1]][indexs[2] + 1] = 1
        sub_arr.append([indexs[0], indexs[1], indexs[2] + 1])

    if indexs[2] - 1 >= 0 and space_arr[indexs[0]][indexs[1]][indexs[2] - 1] == 0:
        space_arr[indexs[0]][indexs[1]][indexs[2] - 1] = 1
        sub_arr.append([indexs[0], indexs[1], indexs[2] - 1])

# 입력.
m,n,h = map(int, stdin.readline().split(" "))
space_arr = [list(list(map(int,stdin.readline().split(" "))) for _ in range(n)) for _ in range(h)]

# que에 익은 토마토 위치 값을 넣어줌.
que = [[]]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if space_arr[i][j][k] == 1:
                que[0].append([i,j,k])

# 결과 변수.
result_cnt = -1

# que에 아무것도 없을때 까지 while loop 돔.
while len(que) > 0:
    que_poped = que.pop(0)
    sub_arr = []
    for indexs in que_poped:
        my_bfs(indexs)
    if len(sub_arr) > 0:
        que.append(sub_arr)
    result_cnt += 1

# 가능한 모든 토마토에 대해서 연산이 끝났음에도 불구하고,
# 익지 않은 토마토가 있는지 체크 하는 포문.
zero_check = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if space_arr[i][j][k] == 0:
                zero_check = 1
                break

# 출력.
if zero_check == 1:
    print(-1)
else:
    print(result_cnt)
