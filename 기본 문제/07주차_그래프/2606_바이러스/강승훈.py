from sys import stdin

# 입력.
n = int(stdin.readline())
k = int(stdin.readline())

# 관계 정보를 담을 2차원 빈 배열.
arr_struct = [[] for _ in range(n+1)]

# 입력 받은 컴퓨터 배열은, 2차원 배열인 연결관계 배열로 만듬.
for i in range(k):

    # 입력.
    n,m = map(int, stdin.readline().split(" "))
    arr_struct[n].append(m)
    arr_struct[m].append(n)

# 초기 값으로, 1번 컴퓨터와 연결된 컴퓨터 번호를 next_visit으로 지정 해둠.
next_visit = [crnt for crnt in arr_struct[1]]

# 이미 한번 들린 번호를 체크할 딕셔너리.
already_visited = {}

# 정답 체크.
result_cnt = -1

# 전파 될 컴퓨터 번호가 담긴 next_visit 배열을 받아서 재귀 할 함수.
def recursion(next_visit):

    # 만약 받은 next_visit의 요소 개수가 0개면 바로 리턴.
    if len(next_visit) == 0:
        return 0
    global already_visited
    global result_cnt
    next_visit = next_visit.copy()

    # 재귀로 넘길 next_visit을 담을 배열.
    sub_next = []

    # 현재 next_visit과 연결된 컴퓨터 번호를 체크.
    for i in next_visit:
        move = arr_struct[i]
        for crnt in move:
            if crnt not in already_visited:
                sub_next.append(crnt)
                already_visited[crnt] = 1
                result_cnt += 1

    # 재귀.
    recursion(sub_next)

# 함수 실행.
recursion(next_visit)

# 출력.
print(result_cnt)
