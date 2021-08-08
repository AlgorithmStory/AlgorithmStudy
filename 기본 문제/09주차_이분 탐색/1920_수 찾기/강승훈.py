# 입력.
n = int(input())
n_set = set(map(int, input().split(" ")))
m = int(input())
m_arr = list(map(int, input().split(" ")))

# 출력.
for crnt in m_arr:
    if crnt in n_set:
        print(1)
    else:
        print(0)
