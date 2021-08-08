# 입력.
n = int(input())
n_arr = list(map(int, input().split(" ")))
n_set = set(n_arr)
m = int(input())
m_arr = list(map(int, input().split(" ")))

# 출력.
for crnt in m_arr:
    if crnt in n_set:
        print(1)
    else:
        print(0)
