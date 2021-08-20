# 입력.
n = int(input())

# 투에모스 공식을 그대로 구현한 재귀 함수.
def recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2:
        return 1 - recursion(n // 2)
    else:
        return recursion(n // 2)

# 출력.
print(recursion(n - 1))
