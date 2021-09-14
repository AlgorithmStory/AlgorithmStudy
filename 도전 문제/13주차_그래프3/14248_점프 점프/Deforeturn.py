# 첨엔 왼쪽 아니면 오른쪽으로만 이동해서 가능한 수를 찾는줄 알았는데,
# 문제에서 요구하는건 분신술 써서 가능한 돌덩이 다 찾는 거였음.
# 문제 안좋은거같음.
def my_bfs(point, visited):
    global visited_main
    visited_main.add(point)
    if len(visited_main) == n:
        print(n)
        exit(0)
    visited.add(point)
    left_move = point-arr[point]
    if left_move >= 0:
        if left_move not in visited:
            my_bfs(left_move, visited)

    right_move = point+arr[point]
    if right_move < n:
        if right_move not in visited:
            my_bfs(right_move, visited)

# 입력.
n = int(input())
arr = list(map(int, input().strip().split(" ")))
start_point = int(input())

# 방문 체크.
visited_main = set()
my_bfs(start_point-1, set())

# 출력.
print(len(visited_main))
