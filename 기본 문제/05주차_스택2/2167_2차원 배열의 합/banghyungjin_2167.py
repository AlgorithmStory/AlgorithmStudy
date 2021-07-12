import sys

num_of_row = int(sys.stdin.readline().split()[0])                   # 행렬의 크기 읽어옴 : 열의 수는 딱히 사용하지 않아서 안읽음
matrix = []                                                         # 행렬

for i in range(num_of_row):                                         # 행렬의 크기 만큼
    matrix.append(list(map(int, sys.stdin.readline().split())))     # 행렬에 내용을 저장

num_of_operation = int(sys.stdin.readline().split()[0])             # 총 수행할 작업의 수

for i in range(num_of_operation):                                   # 작업의 수만크 반복
    answer = 0                                                      # 0에서 시작
    operation = list(map(int, sys.stdin.readline().split()))        # 작업할 행렬 좌표 읽어옴
    for x in range(operation[0] - 1, operation[2]):                 # 해당하는 x 좌표
        for y in range(operation[1] - 1, operation[3]):             # 해당하는 y 좌표
            answer += matrix[x][y]                                  # 해당하는 좌표에 있는 원소 값을 answer에 더해줌
    print(answer)                                                   # 정답 출력
# python으로 하면 시간 초과가 나서 pypy3 로 했습니다.
