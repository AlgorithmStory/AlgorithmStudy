from sys import stdin

# 입력.
n,m = map(int, stdin.readline().split(" "))
arr = list()
start_point = []

# 목표지점과 인접한 위치 값 셋에 저장 해두는 변수.
end_check = set()
for i in range(n):
    arr.append(list(map(int, stdin.readline().split(" "))))
    if len(start_point) == 0:
        for j in range(m):
            if arr[i][j] == 2:
                start_point.append(i); start_point.append(j)
                start_point.append(-1)
                arr[i][j] = 1
                end_check.add(str(i + 1)+"|"+str(j)); end_check.add(str(i - 1)+"|"+str(j));
                end_check.add(str(i) + "|" + str(j + 1)); end_check.add(str(i)+"|"+str(j - 1));
                break

# 거리 구할때 쓰는 방문체크 셋.
visited = set()

# q에 목표지점 초기값 셋팅해주고, pop 하면서 인접 위치 넣어줌.
q = [start_point]
while len(q) > 0:
    point = q.pop(0)
    key = str(point[0])+"|"+str(point[1])
    if key not in visited:
        visited.add(key)
        if arr[point[0]][point[1]] == 1:
            crntValue = point[2]+1
            arr[point[0]][point[1]] = crntValue
            if point[0] > 0:
                q.append([point[0]-1, point[1], crntValue])
            if point[1] > 0:
                q.append([point[0], point[1]-1, crntValue])
            if point[0] < n-1:
                q.append([point[0]+1, point[1], crntValue])
            if point[1] < m-1:
                q.append([point[0], point[1]+1, crntValue])

# 연산 끝난뒤에 값이 1이면서, 목표지점과 인접하지 않으면 -1로 출력.
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            key = str(i)+"|"+str(j)
            if key not in end_check:
                print("-1", end=" ")
            else:
                print(str(arr[i][j]), end=" ")
        else:
            print(str(arr[i][j]), end=" ")
    print()
