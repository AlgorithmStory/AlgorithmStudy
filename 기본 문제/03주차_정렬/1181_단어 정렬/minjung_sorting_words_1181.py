from sys import stdin

N = int(stdin.readline())                       # 크기를 입력받음
w_dict = {}

for _ in range(N):
    
    word = stdin.readline().strip()
    key = len(word)
    if len(word) not in w_dict:                              
        w_dict[key] = {word}
    else:
        w_dict[key].add(word)


keys = sorted(w_dict)

for key in keys:

    words = list(w_dict[key])
    words.sort()

    for word in words:
        print(word)
