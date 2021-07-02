import sys
N = int(sys.stdin.readline())                       # 크기를 입력받음
words = []

for _ in range(N):
    input = sys.stdin.readline()[:-1]
    

    if input in words:                              # 중복된 단어는 추가하지 않습니다
        continue
    
    words.append(input)

words.sort()

c_dict = {}                                         # 각요소의 길이 카운팅 계수 저장할 딕셔너리 선언

for word in words:

    if len(word) not in c_dict:                     # 들어온적없는 길이는 새로 선언 
        c_dict[len(word)] = 0
            
    c_dict[len(word)] += 1                           # 각 해당하는 길이에 해당하는 value 1증가시킴
    
keys = sorted(c_dict)                                # 키 값에 대하여 오름차순으로 정렬시켜줌

for key in keys:                                        
    for word in words:
        if key == len(word):
            print(word)                              # 출력부분
