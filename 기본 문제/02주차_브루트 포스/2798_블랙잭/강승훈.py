# 5 21
# 5 6 7 8 9

from sys import stdin
n, m = map(int, input().split(" "))
arr = list(map(int, stdin.readline().split(" ")))
memo = {} # 체크 할때마다 인덱스 3개의 조합을 딕셔너리에 키 값으로 저장.
arr.sort() # 왼쪽부터 체크 하기 위해서 오름 차순으로 정렬.
max_check = 0 # 확인하면서 지금 까지 나온 조합보다 큰 조합이 나올때마다, 저장.

def recursion(index_a,index_b,index_c):
    # 인덱스 범위 벗어나면 함수 종료.
    if index_a >= n or index_b >= n or index_c >= n:
        return

    # 지금 확인하려는 조합이 이전에 확인 했던 조합이면 함수 종료.
    key = str(index_a) + "|" + str(index_b) + "|" + str(index_c)
    if key in memo:
        return

    # 지금 확인하는 조합이 목표 값을 초과하면, 더 이상 진행 할 필요가 없으므로, 함수 종료.
    sum = arr[index_a] + arr[index_b] + arr[index_c]
    if sum > m:
        return

    # 지금 확인하는 조합이 가장 큰 값이라면, max_check 업데이트 해줌.
    global max_check
    if sum > max_check:
        max_check = sum

    # 재귀함수 계속 진행.
    recursion(index_a + 1, index_b + 1, index_c + 1)
    recursion(index_a, index_b + 1, index_c + 1)
    recursion(index_a, index_b, index_c + 1)
    memo[key] = 1

recursion(0,1,2)
print(max_check)
