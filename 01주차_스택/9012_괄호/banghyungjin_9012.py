import sys

count = int(input())
is_true = True
for i in range(count):
    input_string = sys.stdin.readline().split()
    string_list = []
    for j in input_string[0]: # ( 이 들어오면 stack에 넣고, ) 이 들어오면 stack에 있는 ( 하나를 빼서 없앰,  뺄 ( 이 없으면 NO로
        if j == '(':
            string_list.append(j)
        elif len(string_list) == 0:
            is_true = False
            break
        else: 
            del string_list[-1]
    if is_true and len(string_list) == 0:
        print('YES')
    else:
        print('NO')
    is_true = True
