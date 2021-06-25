# @@ 체스판이 대각선끼리는 색이 같다는 패턴을 이용.

n,m = map(int, input().split())
place = [input() for _ in range(n)]
min = 500

# color에는 "W" 이거나 "B"가 들어감. (체스판의 시작이 "B"이냐 "W"이냐 두가지 경우라서)
def place_checker(color_orig):
    dict = {}
    color = color_orig
    right_check = 0
    left_check = 0

    # 제일 왼쪽 상단부터 오른쪽 방향의 대각선 탐색, 값이 다르면 dict에 해당 인덱스를 키 값으로 저장함.
    for i in range(m):
        if i+1 % 2 == 0:
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
        while True:
            if index >= n or index+i >= m:
                break
            if place[index][index+i] != color:
                key = str(index) + "|" + str(index+i)
                dict[key] = 1
                right_check += 1
            index += 1
    if color_orig == "W":
        color = "B"
    else:
        color = "W"

    # 제일 왼쪽 상단부터, 왼쪽 끝까지의 대각선 탐색, 마찮가지로 기댓값과 다르면 dict에 해당 위치를 키값으로 저장
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
                left_check += 1
            index += 1

    # 왼쪽 상단부터 전체 맵에 대해서, 8x8 크기의 범위에 대한 인덱스를 위에서 저장한 dict에서 찾음.
    # 만약 dict에 해당 위치의 키 값이 존재하는거라면, 지금 탐색하는 범위에 고쳐야 할 값이 있다는것임.
    global min
    for c in range(n - 8+1):
        for k in range(m - 8+1):
            cnt = 0 # 그걸 여기다가 저장함.
            for i in range(c, c + 8):
                for j in range(k, k + 8):
                    key = str(i) + "|" + str(j)
                    if key in dict:
                        cnt += 1
            if cnt < min: # 마지막에 global로 선언된 min 값과 비교하면서, 최소의 값을 계속 찾음.
                min = cnt

# 위에서 만든 함수를 두번 실행 시키는데, [0][0] 번째 위치의 색이 두가지 경우이기 때문.
place_checker("W")
place_checker("B")
print(min)
