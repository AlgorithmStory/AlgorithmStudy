# 입력.
n = int(input())
n_arr = list(map(int, input().split(" ")))
m = int(input())
m_arr = list(map(int, input().split(" ")))
n_dict = {}

# 첫번째 배열의 키 값과, 그 갯수를 밸류로해서 딕셔너리로 저장.
for crnt in n_arr:
    if crnt in n_dict:
        n_dict[crnt] += 1
    else:
        n_dict[crnt] = 1

# 두번째 배열을 하나씩 딕셔너리에 몇개 있는지 확인 하면서 출력.
for i in range(m):
    if m_arr[i] in n_dict:
        print(n_dict[m_arr[i]], end=" ")
    else:
        print(0, end=" ")
