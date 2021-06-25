# @@ 체스판이 대각선끼리는 색이 같다는 패턴을 이용.

# 입력 받음.
n,m = map(int, input().split())
place = [input() for _ in range(n)]

# N과 M의 최대 크기가 50이기 때문에, 전체 체스판의 칸 수는 최대 250이고,
# if문으로 min 값에 최소 값을 계속 저장 할것이기 때문에, min의 초기 값은 250보다 크게 설정함.
min = 500

# color에는 "W" 이거나 "B"가 들어감. (체스판의 시작이 "B"이냐 "W"이냐 두가지 경우라서)
def place_checker(color_orig):
    dict = {} # 입력으로 주어진 전체 체스판에 틀린 색인 위치의 값을 key값으로 저장할거임.
    color = color_orig # 대각으로 처음에 space[0][0]부터 오른쪽 방향으로 탐색하는데, 왼쪽으로 탐색할때는 space[1][0] 부터 내려 가면서, 정답 색을 반전 시키기 위한 용도로 ,color_orig을 활용하기 위하여, 따로 색 변수를 하나 더 만듬.

    # 제일 왼쪽 상단부터 오른쪽 방향의 대각선 탐색, 값이 다르면 dict에 해당 인덱스를 키 값으로 저장함.
    for i in range(m): # 0번째 부터 오른쪽 ----> 방향의 대각선을 탐색하니까, 체스판의 가로 길이인, m 넣음.
        if i+1 % 2 == 0: # 처음 대각선이 만약에 "W"여야 한다면, 다음 대각선을 탐색할때는 "B"여야함. 그래서 매 턴 마다 색 바꿔주는거.
            if color == "W":
                color = "B"
            else:
                color = "W"
        else:
            if i != 0:
                if color == "B":
                    color = "W"
                else:
                    color = "B"
        index = 0
        while True: #[0][0] -> [1][1] -> [2][2] 식으로 인덱스를 증가 시키면, 대각선으로 탐색이 가능한데, [index][index+i]에서 +i를 더해준 이유는, 오른쪽 방향의 대각선을 탐색하기 위함.
            if index >= n or index+i >= m: # [여기][여기] 두개의 인덱스중 하나라도 체스판의 범위를 초과하면 빠져나감.
                break
            if place[index][index+i] != color: # 기대하는 색과 다르면 이건 바꿔야하는 위치니까, 그 위치를 딕셔너리에 키 값으로 넣음.
                key = str(index) + "|" + str(index+i)
                dict[key] = 1
            index += 1

    # 처음에 [0][0] 위치인 중앙부터 대각 탐색하는데, 이제 밑 대각으로 탐색하기 위해서, color를 바꿔줌.
    if color_orig == "W":
        color = "B"
    else:
        color = "W"

    # 제일 왼쪽 상단부터, 왼쪽 끝까지의 대각선 탐색, 마찮가지로 기댓값과 다르면 dict에 해당 위치를 키값으로 저장
    # 위랑 논리적으로 같아서 주석 생략.
    for i in range(1, n):
        if i % 2 == 0:
            if color == "W":
                color = "B"
            else:
                color = "W"
        else:
            if i != 1:
                if color == "B":
                    color = "W"
                else:
                    color = "B"
        index = 0
        while True:
            if index+i >= n or index >= m:
                break
            if place[index+i][index] != color:
                key = str(index+i) + "|" + str(index)
                dict[key] = 1
            index += 1

    # 왼쪽 상단부터 전체 맵에 대해서, 8x8 크기의 범위에 대한 인덱스를 위에서 저장한 dict에서 찾음.
    # 만약 dict에 해당 위치의 키 값이 존재하는거라면, 지금 탐색하는 범위에 고쳐야 할 값이 있다는것임.
    global min
    for c in range(n - 8+1): # 8*8 탐색의 범위 자체를 아래로 이동시키는 포문.
        for k in range(m - 8+1): # 8*8 탐색의 범위 자체를 오른쪽으로 이동시키는 포문.
            cnt = 0 # 8*8 범위에 고쳐야 할 값이 존재하면 여기다가 1 증가시킴.

            # 8*8 범위에 대해서 탐색하는 이중 포문
            for i in range(c, c + 8):  # 4중 포문중 첫번쨰 포문이 여기의 시작점에 포함됨으로써, 8*8 탐색 범위 자체를 이동시킴
                for j in range(k, k + 8): # 이것도 마찮가지.
                    key = str(i) + "|" + str(j)
                    if key in dict:
                        cnt += 1
            if cnt < min: # 마지막에 global로 선언된 min 값과 비교하면서, 최소의 값을 계속 찾음.
                min = cnt

# 위에서 만든 함수를 두번 실행 시키는데, [0][0] 번째 위치의 색이 두가지 경우이기 때문.
place_checker("W")
place_checker("B")
print(min)
