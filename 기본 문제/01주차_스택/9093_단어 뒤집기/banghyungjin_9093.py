import sys

count = int(input())

for i in range(count):
    answer = []
    input_string = sys.stdin.readline().split()
    for j in input_string:
        string_list = list(j)
        string_list.reverse()
        string_list.append(' ')
        answer.append(''.join(string_list))
    print(''.join(answer))
