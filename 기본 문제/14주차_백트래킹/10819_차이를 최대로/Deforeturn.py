# 입력.
n = int(input())
arr = list(map(int, input().split(" ")))

# 방문 체크.
visited = [False] * n

# 결과 변수.
max_check = 0

# 모든 경우의 수를 따져봄.
def recursion(basket, index):
    if len(basket) == n:
        global max_check
        sub_max = max_checker(basket)
        if sub_max > max_check:
            max_check = sub_max
    else:
        global visited
        basket = basket.copy()
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                basket.append(arr[i])
                recursion(basket, i)
                basket.pop()
                visited[i] = False

# 주어진 조건의 배열 sum 계산 해주는 함수.
def max_checker(basket):
    answer_sum = 0
    for i in range(n-1):
        answer_sum += abs(basket[i]-basket[i+1])
    return answer_sum

# 함수 실행.
recursion([], -1)

# 출력.
print(max_check)
