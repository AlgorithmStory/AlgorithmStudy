# 기본 아이디어는, 칸 하나하나에 대해서 위아래, 좌우, 대각의 모든 방향을 탐색할 필요 없이,
# 1.5시 방향, 3시 방향, 4.5시 방향, 6시 방향만 탐색하면됨.

space = [input() for _ in range(19)] # 데이터 받음

# 어떤 바둑판[인덱스][인덱스] 요소에 대해서 위에 적어놨다시피, 4가지 방향에 대해서 탐색하는 함수임.
def checker(ball_color, index_1, index_2): # 매개변수로는, 바둑 색, 위치 인덱스 2개가 들어옴.

    # 탐색하면서, 인덱스 초과를 방지하기 위해서, 미리 길이 저장함.
    hori_len = len(space[0])
    verti_len = len(space)
    sequen_check = 1 # 연속된 같은 색의 돌맹이 횟수 세는 변수.

    # 1.5시 방향 탐색 (우 상향 대각선)
    if index_1 > 3 and index_2 < hori_len-7: # index_1은 y 축인데, 시작 위치가 인덱스3보다 작으면, 인덱스 0보다 작아질 수가 있어서 조건 미리 준거임. index_2도 마찮가지.
        for i in range(1,6): # 바둑돌이 같은 색으로 5개 연속되면 바로 나가면되지만, 6개 일수도 있는데, 6개면 오목이 성립이 안됨. 그래서 1칸 더 탐색하는거.
            if index_1-i < 0 or index_2+i+i >= hori_len: # 마찮가지로 인덱스에러 방지용 구문.
                break
            if space[index_1-i][index_2+i+i] == ball_color: # 같은 색이면 check 증가.
                sequen_check += 1
            if sequen_check < 5 and space[index_1-i][index_2+i+i] != ball_color: # 연속5개 채우기 전에, 다른 색 나오면 바로 break.
                break
        if sequen_check > 5: # 연속된 돌맹이가 6개면, check변수 1로 바꿔줌. 이건 오목이 아니니까.
            sequen_check = 1
    if sequen_check == 5 and space[index_1+1][index_2-2] != ball_color: # 만약 연속된 돌맹이가 딱 5개 잘 나왔는데, 탐색을 시작하려는 방향의 한칸 반대 돌맹이가 같은 색일 수도 있음.
        # 그래서 다른 색일 경우에만 오목이 성립되기 때문에, 바로 return 해주고 함수 종료됨.
        return sequen_check
    else: # 만약 같은 색이라면 오목이 아니라 육목이 되기때문에, 다시 check 변수 1로 바꿔주고 밑에 구문 똑같이 실행됨.
        sequen_check = 1

    # 3시 방향 탐색
    if index_2 < hori_len-7:   # 여기서부터는 방향만 다르고, 기본 골자는 위랑 같으니, 주석 생략.
        for i in range(1,6):
            if index_2+i+i >= hori_len:
                break
            if space[index_1][index_2+i+i] == ball_color:
                sequen_check += 1
            if sequen_check < 5 and space[index_1][index_2+i+i] != ball_color:
                break
        if sequen_check > 5:
            sequen_check = 1
    if sequen_check == 5 and space[index_1][index_2-2] != ball_color:
        return sequen_check
    else:
        sequen_check = 1
    
    # 4.5시 방향 탐색
    if index_2 < hori_len-7 and index_1 < verti_len-3: # 마찮가지.
        for i in range(1, 6):  
            if index_1+i >= verti_len or index_2+i+i >= hori_len:
                break
            if space[index_1+i][index_2+i+i] == ball_color:
                sequen_check += 1
            if sequen_check < 5 and space[index_1+i][index_2+i+i] != ball_color:
                break
        if sequen_check > 5:
            sequen_check = 1
    if  sequen_check == 5 and space[index_1-1][index_2-2] != ball_color:
        return sequen_check
    else:
        sequen_check = 1

    # 6시 방향 탐색
    if index_1 < verti_len-3: # 마찮가지.
        for i in range(1, 6):
            if index_1+i >= verti_len:
                break
            if space[index_1 + i][index_2] == ball_color:
                sequen_check += 1
            else:
                break
        if sequen_check > 5:
            sequen_check = 1
    if sequen_check == 5 and space[index_1-1][index_2] == ball_color:
        sequen_check = 1

    return sequen_check



break_check = 0
for i in range(19): # 모든 맵의 위치 인덱스를 이중 포문으로 구현해서, 위에 만든 함수에다 집어 넣는거임.
    for j in range(len(space[0])):
        if space[i][j] == "1" or space[i][j] == "2": # 현재 시작 위치가 "1" 또는 "2"라면 함수에다 집어넣음.
            result = checker(space[i][j], i, j)
            if result == 5: # 위 함수 실행 결과로써, 5가 리턴 된다는건, 육목도 아니고, 정확히 딱 오목만 리턴 됬다는 거임.
                result_j = 0 # 이건 j의 위치를 결과로 반환해야하는데, 공백이 숫자 사이에 있기 때문에, 따로 계산 매겨 주는거임.
                if j == 0:
                    result_j = 0
                else:
                    result_j = int(j/2)
                print(space[i][j])
                print(f"{i+1} {result_j+1}")
                break_check = 1  # 결과 값이 리턴됬으면, break_check 이걸 1로 할당 해주면서, 이중 포문을 완벽히 빠져나감.
                break
    if break_check == 1:
        break

# 만약 위의 이중 포문 내에서 오목이 안나왔으면, 이 오목판은 승부가 아직 안낫다는 의미라, 초기 변수 할당 값을 그대로 print 해주면 됨.
if break_check == 0:
    print(break_check)
