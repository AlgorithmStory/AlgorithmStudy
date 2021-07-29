from sys import stdin

# 입력.
n = int(stdin.readline())
m = int(stdin.readline())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, stdin.readline().split(" "))
    arr[a].append(b)
    arr[b].append(a)

# 방문 체크 딕셔너리.
alr_visited = {}

# 결과 저장 변수.
result_cnt = 0

# 1번째 친구와 연결된 노드만 체크하면 되서, 재귀함수 필요 없어서 포문으로 함.
for node in arr[1]: # 1번의 친구 하나씩 다 꺼내는데,
    if node not in alr_visited: # 1번의 친구가 딕셔너리에 없으면, 결과 카운트 해주고, 딕셔너리 체크.
        alr_visited[node] = 1
        result_cnt += 1
    for node2 in arr[node]: # 1번의 친구를 방문 했든 안했든, 그와 관련된 친구는 탐색 해줘야 됨.
        if node2 not in alr_visited: # 딕셔너리에 없으면, 넣어주고 체크.
            alr_visited[node2] = 1
            result_cnt += 1

# 결과.
if result_cnt == 0:
    print(0)
else:
    print(result_cnt - 1)
