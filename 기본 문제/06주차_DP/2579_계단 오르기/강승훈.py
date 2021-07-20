from sys import stdin

# 입력
n = int(stdin.readline())
stairs = [int(stdin.readline()) for _ in range(n)]

# 메모이제이션 변수.
memo = [-1 for _ in range(n)]

# 재귀 함수 (처음 실행시 마지막 위치 값을 넣어줌).
def recursion(index):
    # 첫번째 위치에선, 첫번째 계단이라는 경우밖에 없으니 첫번째 계단 값 리턴.
    if index == 0:
        return stairs[0]

    # 인덱스가 위치를 벗어나면 걍 리턴.
    if index < 0:
        return 0

    # 이미 계산 했던 값이면, 계산 했던 값 리턴.
    if memo[index] != -1:
        return memo[index]

    # n번째 계단은 n-3과 n-1을 거쳐서 오는 경우와, 과 n-2 번째 계단에서 올라오는 두가지 경우만 존재함.
    memo[index] = max(recursion(index - 3) + stairs[index - 1], recursion(index - 2)) + stairs[index]

    # 둘중 큰 값에 현재의 계단 값을 더해서 취하면 됨.
    return memo[index]

# 출력.
print(recursion(n - 1))
