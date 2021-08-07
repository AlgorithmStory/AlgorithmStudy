from sys import stdin

# 입력.
n = int(stdin.readline())
m = int(stdin.readline())
nodes_edg_arr = []
for _ in range(m):
    a,b,c = map(int, stdin.readline().split(" "))
    nodes_edg_arr.append([a,b,c])

# 비용을 기준으로 오름차순 정렬.
nodes_edg_arr = sorted(nodes_edg_arr, key=lambda x:x[2])

# 연결된 컴퓨터 조합을 담을 딕셔너리.
main_visited = {}

# 연결된 컴퓨터 담을 딕셔너리.
visited = {nodes_edg_arr[0][0]:1}

# 결과.
result_pay = 0

# visited에 다 담을때까지,
while len(visited) != n:

    # 두개의 노드와 비용을 a,b,c로 꺼냄.
    for a, b, c in nodes_edg_arr:

        # 키 값 구하고.
        key = str(a) + "|" + str(b)

        # 담지 않은 조합일때만.
        if key not in main_visited:

            # 컴퓨터 두개를 모두 연결했다면 무시.
            if a in visited and b in visited:
                continue

            # 두개의 컴퓨터중 하나만 연결되있다면,
            if a in visited or b in visited:

                # 조합 딕셔너리에 담아주고,
                main_visited[key] = 1
                # 컴퓨터 두개도 각각 visited에 담아줌.
                visited[a] = 1
                visited[b] = 1

                # 비용 갱신.
                result_pay += c
                break

# 출력.
print(result_pay)
