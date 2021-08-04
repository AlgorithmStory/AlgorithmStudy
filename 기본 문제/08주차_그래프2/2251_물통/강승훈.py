# bfs 함수.
def my_bfs(bottles):

    # 일단 필요한거 글로벌 선언.
    global visited
    global que

    # 키 값 구하고, visited에 넣음.
    key = str(bottles)
    visited[key] = 1

    # 초기엔 파라미터로 들어온 값 sub_status에 카피해서 잠시 저장.
    sub_status = bottles.copy()

    # 첫번째 비커가 비어있지 않다면,
    if bottles[0] > 0:

        # 비커간의 관계에 대해서 분기해주고, 계산한 새로운 비커를 sub_status에 갱신.
        if bottles[0] < (b-bottles[1]):
            sub_status = [0, bottles[0]+bottles[1], bottles[2]]
        elif bottles[0] >= (b-bottles[1]):
            sub_status = [bottles[0]-(b-bottles[1]), b, bottles[2]]

        # 갱신된 비커에 대한 키 값 구하고,
        sub_key = str(sub_status)

        # 이미 구했던 조합이 아니라면, global로 선언된 큐에 append해주고, visited에 방금 구한 키 값 넣어줌.
        if sub_key not in visited:
            que.append(sub_status)
            visited[sub_key] = 1

        # ------- 마찮가지.
        if bottles[0] < (c-bottles[2]):
            sub_status = [0, bottles[1], bottles[0]+bottles[2]]
        elif bottles[0] >= (c-bottles[2]):
            sub_status = [bottles[0]-(c-bottles[2]), bottles[1], c]
        sub_key = str(sub_status)
        if sub_key not in visited:
            que.append(sub_status)
            visited[sub_key] = 1

    # ------- 여기서부턴 위와 로직이 같음.
    # 두번째 비커가 비어있지 않다면,
    if bottles[1] > 0:
        if bottles[1] < (a-bottles[0]):
            sub_status = [bottles[0]+bottles[1], 0, bottles[2]]
        elif bottles[1] >= (a-bottles[0]):
            sub_status = [a, bottles[1]-(a-bottles[0]), bottles[2]]
        sub_key = str(sub_status)
        if sub_key not in visited:
            que.append(sub_status)
            visited[sub_key] = 1

        if bottles[1] < (c-bottles[2]):
            sub_status = [bottles[0], 0, bottles[1]+bottles[2]]
        elif bottles[1] >= (c-bottles[2]):
            sub_status = [bottles[0], bottles[1]-(c-bottles[2]), c]
        sub_key = str(sub_status)
        if sub_key not in visited:
            que.append(sub_status)
            visited[sub_key] = 1

    # 세번째 비커가 비어있지 않다면,
    if bottles[2] > 0:
        if bottles[2] < (a-bottles[0]):
            sub_status = [bottles[2]+bottles[0], bottles[1], 0]
        elif bottles[2] >= (a-bottles[0]):
            sub_status = [a, bottles[1], bottles[2]-(a-bottles[0])]
        sub_key = str(sub_status)
        if sub_key not in visited:
            que.append(sub_status)
            visited[sub_key] = 1

        if bottles[2] < (b-bottles[1]):
            sub_status = [bottles[0], bottles[2]+bottles[1], 0]
        elif bottles[2] >= (b-bottles[1]):
            sub_status = [bottles[0], b, bottles[2]-(b-bottles[1])]
        sub_key = str(sub_status)
        if sub_key not in visited:
            que.append(sub_status)
            visited[sub_key] = 1

# 입력.
a, b, c = map(int, input().split(" "))

# 결과.
result_arr = []

# 종복 조합 체크 딕셔너리.
visited = {}

# 탐색 할 경우의 수.
que = [[0,0,c]] # 처음엔 0,0,c 인 경우 밖에 없으므로.

# que가 비어질때까지 돔.
while len(que) > 0:
    status = que.pop(0) # 앞에꺼 pop.
    if status[0] == 0: # 젤 왼쪽 비커가 0이면, 결과 변수에 값 넣어줌.
        result_arr.append(status[2])

    # bfs 실행.
    my_bfs(status)

# 정렬.
result_arr.sort()

# 출력.
print(*result_arr)
