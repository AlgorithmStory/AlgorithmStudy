from sys import stdin

# 입력.
n = int(stdin.readline())
a,b = map(int, stdin.readline().split(" "))
m = int(stdin.readline())

# 관계 리스트.
relation_arr = [[] for _ in range(n+1)]

# 관계 리스트에 입력.
for _ in range(m):
    first, second = map(int, stdin.readline().split(" "))
    relation_arr[first].append(second)
    relation_arr[second].append(first)

# 방문 체크.
visited = {}

# dfs 함수.
def my_dfs(index, value):
    visited[index] = 1 # 들어오자마자 방문 체크.
    for crnt in relation_arr[index]: # index의 1촌들 crnt로 하나하나 꺼냄.
        if crnt == b: # 꺼낸게 b이면 index의 1촌에 b가 존재하는 것이므로,
            global result # 글로벌로 선언된것에,
            result = value+1 #  값 넣어주고,
            return # 나옴.
        else:
            if crnt not in visited: # 만약 crnt가 b가 아니고, 방문한적도 없다면, 재귀 탐색함.
                my_dfs(crnt, value+1)


# result의 초기 값으로 -1 지정.
result = -1

# a의 1촌들 crnt에 하나하나 꺼냄.
for crnt in relation_arr[a]:
    if crnt == b: # crnt가 b면 1촌이니, result해주고 바로 나옴.
        result = 1
        break
    elif crnt not in visited: # 그게 아니고, 방문하지도 않았으면 crnt에 대하여 dfs 탐색.
        value = my_dfs(crnt, 1)
        if result != -1: # my_dfs 안에서 b를 발견하면 result값이 변하도록 global선언 했는데,
            break # 위의 함수가 끝나고 result의 값이 초기 값인 -1이 아니라는건 답을 구했다는 의미라 더 이상 포문 안돌아도 됨.
        visited[crnt] = 1 # 방문 체크.

# 출력.
print(result)
