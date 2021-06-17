count = int(input())
is_true = True
for i in range(count):
    input_string = input()
    string_list = []
    for j in input_string:
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
