# 입력.
n,m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

# 카운트.
result_cnt = 0

# 재귀 포문 안에서 값을 넣었다 뺐다 하면서 합 체크함.
def recursion(arr_sub, index):
    print(arr_sub)
    if sum(arr_sub) == m and len(arr_sub) > 0:
        global result_cnt
        result_cnt += 1
    if index >= n-1:
        return

    for i in range(index+1, n):
        arr_sub.append(arr[i])
        recursion(arr_sub, i)
        arr_sub.pop()

# 함수 실행.
recursion([], -1)

# 출력.
print(result_cnt)
