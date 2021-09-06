import sys
sys.setrecursionlimit(1000000)
from sys import stdin

# 상하좌우 탐색 함수.
def my_dfs(index):
    global visited
    key_sub = str(index)
    if key_sub in visited:
        return
    visited.add(key_sub)
    if index[0]+1 < n and trans_image[index[0]+1][index[1]] == 255:
        my_dfs([index[0]+1, index[1]])
    if index[1]+1 < m and trans_image[index[0]][index[1]+1] == 255:
        my_dfs([index[0], index[1]+1])
    if index[1]-1 >= 0 and trans_image[index[0]][index[1]-1] == 255:
        my_dfs([index[0], index[1]-1])
    if index[0]-1 >= 0 and trans_image[index[0]-1][index[1]] == 255:
        my_dfs([index[0]-1, index[1]])

# 입력.
n,m = map(int, stdin.readline().split(" "))
image = list(list(map(int, stdin.readline().split(" "))) for _ in range(n))
line_number = int(stdin.readline())

# 평균 구하면서 크기 1/3로 줄임
trans_image = []
for row in image:
    sub_row = []
    for i in range(0, m*3, 3):
        sub_sum = (row[i]+row[i+1]+row[i+2])//3
        if sub_sum >= line_number:
            sub_row.append(255)
        else:
            sub_row.append(0)
    trans_image.append(sub_row)

# 탐색하면서 값이 255이고 방문한적이 없으면 결과에 카운트해주고, 인접 요소들 방문 체크 해줌.
result_cnt = 0
visited = set()
for i in range(n):
    for j in range(0, m):
        if trans_image[i][j] == 255:
            key = str([i,j])
            if key not in visited:
                my_dfs([i,j])
                result_cnt += 1

# 출력.
print(result_cnt)
