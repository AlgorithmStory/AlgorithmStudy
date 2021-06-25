import sys


def go_right(x, y, input_go_board, count) -> bool:                                                  # 오목판에서 오른쪽으로 5개가 있는지 확인, 아래 3개 함수도 동일
    if count == 4 and (y == 18 or input_go_board[x][y] != input_go_board[x][y + 1]):                # 현재 칸 시점에서 5개 충족이 되면 다음 칸이 달라서 오목을 만족하는 지 확인
        return True                                                                                 # 만족하면 True
    if y != 18 and input_go_board[x][y] == input_go_board[x][y + 1]:                                # 다섯 개 이하면 다음 칸 있는지 확인
        return go_right(x, y + 1, input_go_board, count + 1)                                        # 다음 칸 있으면 다음 칸 이동
    else:                                                                                           # 다음 칸 없으면
        return False                                                                                # False


def go_right_up(x, y, input_go_board, count) -> bool:                                               # 오목판에서 오른쪽 대각선 위로 5개가 있는지 확인
    if count == 4 and (x == 0 or y == 18 or input_go_board[x][y] != input_go_board[x - 1][y + 1]):
        return True
    if x != 0 and y != 18 and input_go_board[x][y] == input_go_board[x - 1][y + 1]:
        return go_right_up(x - 1, y + 1, input_go_board, count + 1)
    else:
        return False


def go_down(x, y, input_go_board, count) -> bool:                                                   # 오목판에서 아래로 5개가 있는지 확인
    if count == 4 and (x == 18 or input_go_board[x][y] != input_go_board[x + 1][y]):
        return True
    if x != 18 and input_go_board[x][y] == input_go_board[x + 1][y]:
        return go_down(x + 1, y, input_go_board, count + 1)
    else:
        return False


def go_right_down(x, y, input_go_board, count) -> bool:                                             # 오목판에서 오른쪽 대각선 아래로 5개가 있는지 확인
    if count == 4 and (x == 18 or y == 18 or input_go_board[x][y] != input_go_board[x + 1][y + 1]):
        return True
    if y != 18 and x != 18 and input_go_board[x][y] == input_go_board[x + 1][y + 1]:
        return go_right_down(x + 1, y + 1, input_go_board, count + 1)
    else:
        return False


def solve(input_go_board):                                                                          # 문제 해결용 함수
    for i in range(19):                                                                             # 오목판 19 X 19 루프
        for j in range(19):                                                                         # --
            if input_go_board[i][j] != '0' and go_right(i, j, input_go_board, 0):                   # 오른쪽으로 5개를 충족하는 지 확인, 아래 3개도 동일
                if j == 0 or input_go_board[i][j] != input_go_board[i][j - 1]:                      # 충족되면 왼쪽 칸이 달라서 6개 이상 연속이 아닌지 확인
                    print(input_go_board[i][j])                                                     # 맞으면 흑백 출력
                    print(i + 1, j + 1)                                                             # 제일 왼쪽 칸 출력
                    return 0                                                                        # 함수 끝
            elif input_go_board[i][j] != '0' and go_right_up(i, j, input_go_board, 0):              # 오른쪽 위로 5개를 충족하는 지 확인
                if i == 18 or j == 0 or input_go_board[i][j] != input_go_board[i + 1][j - 1]:
                    print(input_go_board[i][j])
                    print(i + 1, j + 1)
                    return 0
            elif input_go_board[i][j] != '0' and go_down(i, j, input_go_board, 0):                  # 아래로 5개를 충족하는 지 확인
                if i == 0 or input_go_board[i][j] != input_go_board[i - 1][j]:
                    print(input_go_board[i][j])
                    print(i + 1, j + 1)
                    return 0
            elif input_go_board[i][j] != '0' and go_right_down(i, j, input_go_board, 0):            # 오른쪽 아래로 5개를 충족하는 지 확인
                if i == 0 or j == 0 or input_go_board[i][j] != input_go_board[i - 1][j - 1]:
                    print(input_go_board[i][j])
                    print(i + 1, j + 1)
                    return 0
    print(0)                                                                                        # 만족하는게 없으면 0출력
    return 0                                                                                        # 함수 끝


go_board = []                                                                                       # 오목판
for i in range(19):                                                                                 # 오목판에 오목 채우기
    go_board.append(sys.stdin.readline().split())                                                   # --

solve(go_board)                                                                                     # 정답 찾는거 실행
