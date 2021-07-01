import sys
N = int(sys.stdin.readline())

word = {} # word 딕셔너리 만듦
result = [] 
for i in range(N):
    word_input = sys.stdin.readline()
    if len(word_input) not in word: 
        # 입력으로 받아온 단어의 길이가 word의 키에 없을때
        word[len(word_input)] = [word_input]
        # word의 key값으론 입력으로 받아온 단어의 길이를 넣고
        # 입력 단어를 리스트 형식으로 넣는다.
        # key값을 리스트로 보고 value를 그 리스트에 대한 값으로 받아오기위함
    
    else: # 입력으로 받아온 단어의 길이가 word의 키에 있으면
        if word_input not in word[len(word_input)]: 
            # 입력받은 단어가 word.key값에 없으면
            word[len(word_input)].append(word_input)
            # word.key값의 리스트에 입력단어 추가

for i in sorted(word.keys()): # 키값을 길이별로 정렬후
    result = result + sorted(word[i]) # 길이별로 들고온 단어 result에 순서대로 넣어줌

for i in result:
    a = i.split('\n') 
    # 앞에서 처리한대로 들고오면 단어에\n이 생긴다.
    # 그 부분을 따로 리스트로 나눠서 받아온 후 단어 값만 받아오게 설정
    print(a[0])
        