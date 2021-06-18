import sys

count = int(input())
number_list = []
input_counter = 1
is_true = True
answer_list = []

for i in range(count):
    input_number = sys.stdin.readline().split()
    number = int(input_number[0])
    
    if len(number_list) == 0:
         number_list.append(input_counter)
         answer_list.append('+')
         input_counter += 1

    if number_list[-1] == number:
        del number_list[-1]
        answer_list.append('-')

    elif number_list[-1] < number:
        while input_counter < number:
            number_list.append(input_counter)
            input_counter += 1
            answer_list.append('+')
        input_counter += 1
        answer_list.append('+')
        answer_list.append('-')
    
    else:
        is_true = False
        break

if is_true:
    for i in answer_list:
        print(i)
else:
    print("NO")