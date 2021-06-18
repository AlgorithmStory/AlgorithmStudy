import sys

n = int(sys.stdin.readline().split(' ')[0])
target_list = [int(sys.stdin.readline().split(' ')[0]) for _ in range(n)]
status_list = [0]
result_str = ""
status_number = 0
index = 0

while True:
    if status_list[-1] < target_list[index]:
        result_str += '+'
        status_number += 1
        status_list.append(status_number)
    else:
        status_list.pop()
        result_str += '-'
        index += 1
        if index == len(target_list):
            for j in result_str:
                print(j)
            break
        elif status_list[-1] > target_list[index]:
            print('NO')
            break
