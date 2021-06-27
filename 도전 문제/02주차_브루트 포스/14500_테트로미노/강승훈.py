# 7% 에서 틀림. - 포기

from sys import stdin

n,m = map(int, stdin.readline().split(" "))
space = [list(map(int, stdin.readline().split())) for _ in range(n)]

def straight_sum_1(index_1, index_2):
    result = 0
    for i in range(4):
        result += int(space[index_1][index_2+i])
    return result

def straight_sum_2(index_1, index_2):
    result = 0
    for i in range(4):
        result += int(space[index_1+i][index_2])
    return result

def square_sum(index_1, index_2):
    result = 0
    for i in range(2):
        result += int(space[index_1+i][index_2]) + int(space[index_1+i][index_2+1])
    return result

def l_form_sum_1(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1+i][index_2])
        if i == 2:
            result += int(space[index_1+i][index_2+1])
    return result

def l_form_sum_2(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1][index_2+i])
        if i == 2:
            result += int(space[index_1+1][index_2+i])
    return result

def l_form_sum_3(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1 + i][index_2])
        if i == 2:
            result += int(space[index_1+i][index_2-1])
    return result

def l_form_sum_4(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1-i][index_2])
        if i == 2:
            result += int(space[index_1-i][index_2+1])
    return result

def l_form_sum_5(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1][index_2+i])
        if i == 2:
            result += int(space[index_1-1][index_2+i])
    return result

def l_form_sum_6(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1][index_2-i])
        if i == 2:
            result += int(space[index_1+1][index_2-i])
    return result

def l_form_sum_7(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1][index_2-i])
        if i == 2:
            result += int(space[index_1-1][index_2-i])
    return result

def l_form_sum_8(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1][index_2+i])
        if i == 2:
            result += int(space[index_1+1][index_2+i])
    return result

def zigzag_sum_1(index_1, index_2):
    result = 0
    for i in range(2):
        result += int(space[index_1+i][index_2+i]) + int(space[index_1+i+1][index_2+i])
    return result

def zigzag_sum_2(index_1, index_2):
    result = 0
    for i in range(2):
        result += int(space[index_1-i][index_2+i]) + int(space[index_1-i][index_2+i+1])
    return result

def zigzag_sum_3(index_1, index_2):
    result = 0
    for i in range(2):
        result += int(space[index_1+i][index_2+i]) + int(space[index_1+i][index_2+i+1])
    return result

def zigzag_sum_4(index_1, index_2):
    result = 0
    for i in range(2):
        result += int(space[index_1-i][index_2+i]) + int(space[index_1-i-1][index_2+i])
    return result

def last_form_1(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1][index_2+i])
        if i == 1:
            result += int(space[index_1+1][index_2+i])
    return result

def last_form_2(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1+i][index_2])
        if i == 1:
            result += int(space[index_1+i][index_2-1])
    return result

def last_form_3(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1][index_2+i])
        if i == 1:
            result += int(space[index_1-1][index_2+i])
    return result

def last_form_4(index_1, index_2):
    result = 0
    for i in range(3):
        result += int(space[index_1+i][index_2])
        if i == 1:
            result += int(space[index_1+i][index_2+1])
    return result

biggest_sum = -1
for i in range(n):
    for j in range(m - 3):
        number = straight_sum_1(i,j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(n-3):
    for j in range(m):
        number = straight_sum_2(i, j)
        if number > biggest_sum:
            biggest_sum = number
for i in range(n-1):
    for j in range(m-1):
        number = square_sum(i,j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(n-2):
    for j in range(m-1):
        number = l_form_sum_1(i,j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(n-1):
    for j in range(m-2):
        number = l_form_sum_2(i,j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(n - 2):
    for j in range(1, m):
        number = l_form_sum_3(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(2, n):
    for j in range(m-1):
        number = l_form_sum_4(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(1, n):
    for j in range(m-2):
        number = l_form_sum_5(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(n-1):
    for j in range(2, m):
        number = l_form_sum_6(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(1, n):
    for j in range(2, m):
        number = l_form_sum_7(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(n-1):
    for j in range(m-2):
        number = l_form_sum_8(i, j)
        if number > biggest_sum:
            biggest_sum = number


for i in range(n-2):
    for j in range(m-1):
        number = zigzag_sum_1(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(1, n):
    for j in range(m-2):
        number = zigzag_sum_2(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(n-1):
    for j in range(m-2):
        number = zigzag_sum_3(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(2, n):
    for j in range(m-1):
        number = zigzag_sum_4(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(n-1):
    for j in range(m-2):
        number = last_form_1(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(n-2):
    for j in range(1,m):
        number = last_form_2(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(1, n):
    for j in range(m-2):
        number = last_form_3(i, j)
        if number > biggest_sum:
            biggest_sum = number

for i in range(n-2):
    for j in range(m-1):
        number = last_form_4(i, j)
        if number > biggest_sum:
            biggest_sum = number

print(biggest_sum)
