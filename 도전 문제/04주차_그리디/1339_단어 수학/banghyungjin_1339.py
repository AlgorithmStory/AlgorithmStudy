import sys

num_of_letters = int(sys.stdin.readline().split()[0])                                   # 단어의 개수
letters = {}                                                                            # 알파벳과 그 알파벳이 나온 숫자 딕셔너리
answer = 0                                                                              # 정답

for i in range(num_of_letters):                                                         # 단어의 개수 만큼
    input_letter = sys.stdin.readline().split()[0]                                      # 단어들을 읽어옴
    for letter in range(len(input_letter)):                                             # 각 읽어온 단어들을 알파벳 하나씩 나눔
        if not(input_letter[letter] in letters):                                        # letters에 해당 알파벳이 없으면
            letters[input_letter[letter]] = 10 ** (len(input_letter) - letter - 1)      # 새로 넣음 이때 key는 알파벳, value는 해당 알파벳이 가리키는 자리수
        else:                                                                           # letters에 해당 알파벳이 있으면
            letters[input_letter[letter]] += 10 ** (len(input_letter) - letter - 1)     # 해당 원소의 value에 해당 알파벳이 가리키는 자리수 더해줌

letters = sorted(letters.items(), reverse=True, key=lambda x: (x[1]))                   # letters를 각 원소의 value 값으로 정렬

for i in range(len(letters)):                                                           # letters를 처음부터 탐색
    answer += letters[i][1] * (9 - i)                                                   # 순서대로 9부터 역순으로 대입 후 value에 곱해서 answer에 더함

print(answer)                                                                           # 정답 출력
