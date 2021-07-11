import operator
from sys import stdin

# 입력
n = int(input())
word_arr = [stdin.readline().strip() for _ in range(n)]

# 각 알파벳에 자릿수따른 가중치를 줌.
alpabet_dict = {} # 그걸 딕셔너리에, 키와 밸류로 저장.
for crnt_1 in word_arr:
    sub_len = len(crnt_1)
    for i in range(sub_len):
        if crnt_1[i] not in alpabet_dict:
            alpabet_dict[crnt_1[i]] = 10**(sub_len-i-1)
        else:
            alpabet_dict[crnt_1[i]] += 10 ** (sub_len - i - 1)

alpabet_arr = sorted(alpabet_dict.items(), key=operator.itemgetter(1), reverse=True) # 가중치를 기준으로 내림차순 정렬.
alpabet_dict = {}
for i in range(len(alpabet_arr)):
    alpabet_dict[alpabet_arr[i][0]] = 9-i # 앞에서부터, 9 8 7 6 .... 하나씩 줄여 가면서 정수 정해줌.

# 그걸 입력 받은 알파벳에 대입해서, 계산함.
result_sum = 0
for word in word_arr:
    sub = ""
    for j in range(len(word)):
        sub += str(alpabet_dict[word[j]])
    result_sum += int(sub)

# 출력
print(result_sum)
