from sys import stdin

n = int(stdin.readline()) # 들어올 단어 수 n 입력 받음.
dict = {} # 키와 밸류로 저장가능한 딕셔너리 일단 생성.

for _ in range(n): # n 횟수 만큼 입력을 받는데,
    word = stdin.readline().strip() # 이건 그냥 단어
    key = str(len(word)) # 이건 받은 단어에 대해서 길이를 잰다음, 그걸 다시 string 값으로 바꿔서 키로 활용할거임. 예) "1", "2", "7" 등등
    if key in dict: # 위에서 입력받은 키(단어길이) 값이 딕셔너리에 존재한다면, 배열 값으로 append 해줌. 예) {"key":["word","word2","word3"]}
        dict[key].append(word)
    else: # 만약 키 값이 없으면, 그러니까 처음들어오는 단어길이라면, 해당 키값에 대해서, 딕셔너리에 배열 타입으로, 단어 하나 넣어줌. 예) {"key":["word"]}
        dict[key] = [word]

for i in range(51): #  문제 입력 조건으로, 단어길이가 1부터 최대 50까지라고 했음. 그래서 1~50 까지의 숫자에 대해서 string으로 바꿔주면서 딕셔너리 탐색하면됨.
    key = str(i) # 키값 만들어주고
    if key in dict: # 해당 키 값이 딕셔너리에 존재하면,
        sub = set(dict[key]) # 우선 키 값에 들은 배열을 set으로 형변환 시킴. (여기서 그럼 자동으로 중복 제거됨. set자료구조 특성상)
        sub_arr = [] # 배열의 sort 함수를 활용하기 위해서, 다시 배열에다가 담을려고 배열하나 생성해줌.
        for crnt in sub: # 중복이 제거된 set값의 요소를, 방금 만든 배열에다가 다 담음.
            sub_arr.append(crnt)
        sub_arr.sort() # 정렬.
        for crnt in sub_arr: # 바로 출력.
            print(crnt)
