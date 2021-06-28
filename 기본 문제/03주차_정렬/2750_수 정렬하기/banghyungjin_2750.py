import sys

length_of_list = int(sys.stdin.readline().split()[0])
numbers = []

for i in range(length_of_list):                                         # 숫자 배열 읽어옴
    numbers.append(int(sys.stdin.readline().split()[0]))

for i in range(length_of_list - 1, 0, -1):                              # 버블 sort 사용
    for j in range(0, i):                                               # --
        if numbers[j] > numbers[j + 1]:                                 # 뒤의 숫자 보다 크면
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]     # 두 숫자를 swap

for i in numbers:                                                       # 정답 출력
    print(i)
