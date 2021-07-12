from sys import stdin

# 입력
n,m,r = map(int, input().split(" "))
arr = [list(map(int, stdin.readline().split(" "))) for _ in range(n)]

table_arr = [] # 각각의 테두리에 대한 값을 저장할 2차원 배열 변수.

# 입력받은 2차원 배열에 대해서, 테두리를 1차원 배열로 저장하는 함수.
def arr_get(n,m,bias): # 처음 매개변수로 n과 m을 넣어주지만, 테두리를 안으로 들어가면서 여러번 가져와야 하기 때문에, 함수 실행 구문 보면, b라는 녀석을 추가해줬음.
    table_arr_sub = [] # 일단 함수 내에서 잠시 저장할 배열 변수.
    index_2 = 0
    for i in range((n * m) - ((n - 2) * (m - 2))): # 포문 조건에 들어간건, 가장 바깥쪽의 테두리의 길이 계산한거임. (즉, 예제 1번에서 이게 처음 실행될땐, 12가 되겠죠.)
        # index_1과 index_2 그리고 bias 같은걸 조합해서, 로직 구현함.
        if i > 1 and index_1 == 0: # 위로 탐색이 끝났으면, 다시 왼쪽으로 탐색함.        (순서_4)
            index_2 -= 1
        elif index_2 == m - 1: # 그리고 오른쪽 끝까지 탐색이 됬으면, 다시 위로 탐색함.    (순서_3)
            index_1 -= 1
        elif i <= n - 1: # 처음엔 이게 실행 될텐데, 밑으로 끝까지 탐색.                 (순서_1)
            index_1 = i
        else: # 처음 실행 된것이, 조건이 끝났으면, 이게 실행되면서, 오른쪽으로 탐색함.       (순서_2)
            index_2 += 1
        table_arr_sub.append(arr[index_1+bias][index_2+bias]) # 1차원 임시 배열에, 요소 하나하나 저장함.
    table_arr.append(table_arr_sub) # 그 저장된 1차원 배열을, 배열에다 하나씩 담음.

b = 0
sub_b = 0
while True:
    arr_get(n - b, m - b, sub_b) # 함수 계속 실행함.
    b += 2 # b를 2씩 증가시킬때마다,
    sub_b += 1 # sub_b는 1씩 증가
    if b > n-2 or b > m-2: # b가 n-2 or m-2 보다 커지면 나옴.
        break

# 구한 1차원 배열에 대해서, r만큼 이동시킴.
for i in range(len(table_arr)):
    sub_len = len(table_arr[i])
    for j in range(r):
        tmp = table_arr[i][-1]
        for k in range(sub_len-1):
            table_arr[i][-(k+1)] = table_arr[i][sub_len-(k+2)]
        table_arr[i][0] = tmp

# 출력 하기 위해서 1차원 배열을 다시 형식에 맞게 집어넣어줌.
# 위에서 만든 get 함수를 조금 변형해서, 만든거라 따로 설명은 안하겠습니다.
def arr_push(n,m,bias):
    index_2 = 0
    for i in range((n * m) - ((n - 2) * (m - 2))):
        if i > 1 and index_1 == 0:
            index_2 -= 1
        elif index_2 == m - 1:
            index_1 -= 1
        elif i <= n - 1:
            index_1 = i
        else:
            index_2 += 1
        arr[index_1+bias][index_2+bias] = table_arr[sub_b][i] # 입력으로 받은 arr 배열에 덮어쓰기.

# 위와 똑같이 실행시켜주고.
b = 0
sub_b = 0
while True:
    arr_push(n - b, m - b, sub_b)
    b += 2
    sub_b += 1
    if b > n-2 or b > m-2:
        break

# 출력.
for row in arr:
    print(*row)

# 기본적으로 테두리를 1차원 배열로 다 가져온다음, r 시키고, 다시 집어넣는 순이라고 생각하시면 됨.
