from sys import stdin

N = int(stdin.readline())                           # 크기를 입력받음
w_dict = {}                                         # key : 단어길이, value : 단어의집합 으로 저장할 딕셔너리 선언

for _ in range(N):                                  # 정렬할 데이터 갯수만큼
    
    word = stdin.readline().strip()                 # 단어를 입력받습니다.

    if len(word) not in w_dict:                     # 처음들어오는 단어의 길이는 
        w_dict[len(word)] = {word}                  # key : 길이, {단어} 로 추가
    else:                                           # 이미 있던 길이는
        w_dict[len(word)].add(word)                 # add 로 단어 추가


keys = sorted(w_dict)                               # key 값들에 대하여 정렬한 리스트 keys 에 저장

for key in keys:                                    # 각각의 길이에 대해

    words = list(w_dict[key])                       # 단어의집합을 알파벳 순으로 정렬하기 위해 list로 바꿔주고
    words.sort()                                    # 알파벳순으로 정렬해준다음

    for word in words:                              # 각각의 단어모두를
        print(word)                                 # 출력한다
