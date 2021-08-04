from sys import stdin

# 2차원 배열의 위치 값인 인덱스 2개를 파라매터로 받는 bfs 함수.
def my_bfs(index_1, index_2):
    global visited
    global que
    key = str(index_1)+"|"+str(index_2) # 바로 키값 구하고.
    visited[key] = 1 # 딕셔너리에 체크용으로 넣어줌.

    # 상하좌우의 값을 보고 큐에 넣을지 말지 판단하고 넣음.
    if index_1-1 >= 0:
        if area_arr[index_1-1][index_2] > i:
            que.append([index_1-1, index_2])
    if index_1+1 < n:
        if area_arr[index_1+1][index_2] > i:
            que.append([index_1+1, index_2])
    if index_2-1 >= 0:
        if area_arr[index_1][index_2-1] > i:
            que.append([index_1, index_2-1])
    if index_2+1 < n:
        if area_arr[index_1][index_2+1] > i:
            que.append([index_1, index_2+1])

# 입력.
n = int(stdin.readline())
area_arr = [list(map(int, stdin.readline().split(" "))) for _ in range(n)]

# 결과 변수.
result = 1

# 지역의 최저높이와 최대높이는 각각 1과 100이므로, 0~100에 대한 강우량의 경우만 확인 하면 됨.
for i in range(0, 101):
    sub_result = 0 # 강우량 x에 대한 안정 영역 변수.
    visited = {} # 방문 체크 딕셔너리.

    # 2차원 배열 탐색 포문.
    for j in range(n):
        for k in range(n):
            if area_arr[j][k] > i and str(j)+"|"+str(k) not in visited: # 물에 잠기지 않고, 방문 하지 않았으면,
                sub_result += 1 # 안전 영역 카운트.
                que = [[j, k]] # 처음엔 [j,k]만 큐에 들어가서, 밑에 while 실행함.
                while len(que) > 0:
                    indexs = que.pop(0) # 왼쪽꺼 팝 해주고.
                    key = str(indexs[0]) + "|" + str(indexs[1]) # 팝된 키값 구한다음,
                    if key not in visited: # 방문하지 않았으면, bfs 함수에 넣음.
                        my_bfs(indexs[0], indexs[1])

    # sub_result를 최종적으로 result와 비교함으로써 최대값 구함.
    if sub_result > result:
        result = sub_result

# 출력.
print(result)
