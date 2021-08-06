from sys import stdin

def my_bfs(indexs):
    global visited

    # 지금 받은 위치의 집 개수 체크 변수.
    houses_number = 0
    que = [indexs]
    while len(que) > 0:
        houses_number += 1
        indexs = que.pop(0)
        key = str(indexs[0]) + "|" + str(indexs[1])
        visited[key] = 1
        if indexs[0] + 1 < n and city_arr[indexs[0] + 1][indexs[1]] == 1:
            key = str(indexs[0]+1) + "|" + str(indexs[1])
            if key not in visited:
                que.append([indexs[0] + 1, indexs[1]])
                visited[key] = 1
        if indexs[0] - 1 >= 0 and city_arr[indexs[0] - 1][indexs[1]] == 1:
            key = str(indexs[0]-1) + "|" + str(indexs[1])
            if key not in visited:
                que.append([indexs[0] - 1, indexs[1]])
                visited[key] = 1

        if indexs[1] + 1 < n and city_arr[indexs[0]][indexs[1] + 1] == 1:
            key = str(indexs[0]) + "|" + str(indexs[1] + 1)
            if key not in visited:
                que.append([indexs[0], indexs[1] + 1])
                visited[key] = 1

        if indexs[1] - 1 >= 0 and city_arr[indexs[0]][indexs[1] - 1] == 1:
            key = str(indexs[0]) + "|" + str(indexs[1] - 1)
            if key not in visited:
                que.append([indexs[0], indexs[1] - 1])
                visited[key] = 1
    global result_arr
    result_arr.append(houses_number)

# 입력.
n = int(stdin.readline())
city_arr = []
for _ in range(n):
    sub_arr = []
    for crnt in stdin.readline().strip():
        sub_arr.append(int(crnt))
    city_arr.append(sub_arr)

# 방문 체크 딕셔너리.
visited = {}

# 여기에 초기 탐색할 위치 값 입력.
next_arr = []
for i in range(n):
    for j in range(n):
        if city_arr[i][j] == 1:
            next_arr.append([i,j])

# 결과 변수.
result_arr = []
result_cnt = 0

# 팝하면서, 탐색.
while len(next_arr) > 0:
    indexs = next_arr.pop(0)
    key = str(indexs[0])+"|"+str(indexs[1])

    # 팝으로 받은 위치에 방문한적이 없으면,
    # my_bfs를 활용하여 그와 관련된 인접 하우스 체크.
    if key not in visited:
        my_bfs(indexs)
        result_cnt += 1

# 오름차순 정렬.
result_arr.sort()

# 출력.
print(result_cnt)
for crnt in result_arr:
    print(crnt)
