import sys

hv = sys.stdin.readline().split()                                   # 문제의 판때기 크기 읽어옴
horizontal = int(hv[0])                                             # 판때기 크기 가로
vertical = int(hv[1])                                               # 판때기 크기 세로
chess_board = []                                                    # 판때기를 잘라서 만들 체스판
answer = []                                                         # 정답 배열
white_board = []                                                    # 비교용 체스판 (하얀칸 부터 시작)
black_board = []                                                    # 비교용 체스판 (검은칸 부터 시작)
letter = ['W', 'B']                                                 # 비교용 체스판에 넣을 색 배열
counter = 0                                                         # 비교용 체스판에 넣을 색 카운터

for i in range(horizontal):                                         # 문제의 판때기를 읽어와서 체스판에 저장
    chess_board.append(list(sys.stdin.readline().split()[0]))       # --

for i in range(8):                                                  # 비교용 체스판 배열을 만듬
    white_temp = []                                                 # 하얀 체스판에 넣을 거
    black_temp = []                                                 # 검은 체스판에 넣을 거
    for j in range(8):                                              # 총 64번 반복
        white_temp.append(letter[counter])                          # 색 배열과 색 카운터를 사용해서 번갈아가며
        counter = (counter + 1) % 2                                 # 두 개의 체스판에 색을 알맞게 넣음
        black_temp.append(letter[counter])                          # --
    white_board.append(white_temp)                                  # 8번 반복마다 한 줄이 완성되서 체스판 배열에 넣음
    black_board.append(black_temp)                                  # --
    counter = (counter + 1) % 2                                     # 다음줄에 들어갈 색을 위해 카운터 재배치

for x in range(horizontal - 7):                                     # 판때기를 8X8로 전부 잘라봄 (가로 - 7) X (세로 - 7) 만큼 나옴
    for y in range(vertical - 7):                                   # --
        white_count = 0                                             # 하얀 체스판과 틀린 부분 갯수
        black_count = 0                                             # 검은 체스판과 틀린 부분 갯수
        for z in range(8):                                          # 비교용 체스판 만들때 처럼 8 X 8로 잘라 배열로 변환
            print_list = []                                         # --
            for w in range(8):                                      # 64번 반복
                if chess_board[x + z][y + w] != black_board[z][w]:  # 판때기 체스판 칸이 검은 체스판 칸과 다르면
                    black_count += 1                                # black_count 하나 추가
                if chess_board[x + z][y + w] != white_board[z][w]:  # 판때기 체스판 칸이 하얀 체스판 칸과 다르면
                    white_count += 1                                # white_count 하나 추가
        answer.append(min(white_count, black_count))                # 둘 중 작은 걸 answer 에 넣음

print(min(answer))                                                  # answer 에서 젤 작은 거 출력
