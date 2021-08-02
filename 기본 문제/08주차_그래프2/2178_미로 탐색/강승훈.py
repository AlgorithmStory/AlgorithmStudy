from sys import stdin

# 입력.
n,m = map(int, stdin.readline().split(" "))
maze_arr = [stdin.readline().strip() for _ in range(n)]

# 이동하면서 체크 할 맵.
move_arr = list([0 for _ in range(m)] for _ in range(n))
move_arr[0][0] = 1

# 상하좌우 체크하면서, 갱신하는 함수.
def my_bfs(index_arr, value):
    if index_arr[0] < 0 or index_arr[1] < 0 or index_arr[0] >= n or index_arr[1] >= m: # 인덱스 초과 방지.
        return 0

    if index_arr[0]+1 < n and maze_arr[index_arr[0]+1][index_arr[1]] == "1" and move_arr[index_arr[0]+1][index_arr[1]] == 0: # 아래 방향으로 갈 수 있으면,
        move_arr[index_arr[0]+1][index_arr[1]] = value + 1 # 그 위치에 move값 넣어주고,
        q.append([index_arr[0]+1, index_arr[1]]) # 함수 밖에 있는 q에 위치값을 넣어줌.

    if index_arr[0]-1 >= 0 and maze_arr[index_arr[0]-1][index_arr[1]] == "1" and move_arr[index_arr[0]-1][index_arr[1]] == 0: # 마찮가지 (위).
        move_arr[index_arr[0]-1][index_arr[1]] = value + 1
        q.append([index_arr[0]-1, index_arr[1]])

    if index_arr[1]+1 < m and maze_arr[index_arr[0]][index_arr[1]+1] == "1" and move_arr[index_arr[0]][index_arr[1]+1] == 0: # 마찮가지 (오른).
        move_arr[index_arr[0]][index_arr[1]+1] = value + 1
        q.append([index_arr[0], index_arr[1]+1])

    if index_arr[1]-1 >= 0 and maze_arr[index_arr[0]][index_arr[1]-1] == "1" and move_arr[index_arr[0]][index_arr[1]-1] == 0: # 마찮가지 (왼).
        move_arr[index_arr[0]][index_arr[1]-1] = value + 1
        q.append([index_arr[0], index_arr[1]-1])

# 0,0 위치 값을 우선 q에 넣음.
q = [[0,0]]

# q에 아무것도 없을때까지 계속 돔.
while len(q) != 0:
    index_arr = q.pop(0) # 제일 앞에 부터 위치 값 빼주고,
    my_bfs(index_arr, move_arr[index_arr[0]][index_arr[1]]) # 위치 값이랑, 그 위치의 move_arr 밸류 값 넣어줌.

# 출력.
print(move_arr[n-1][m-1])
