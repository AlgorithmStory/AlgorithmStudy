import sys

length_of_list = int(sys.stdin.readline().split()[0])       # 리스트 길이 읽어옴
numbers = [0] * 10001                                       # 원소의 갯수를 카운팅할 리스트

for i in range(length_of_list):                             # 리스트 길이 만큼 루프
    numbers[int(sys.stdin.readline().split()[0])] += 1      # 리스트의 값을 읽어오면서 카운팅 리스트의 해당하는 인덱스에 값을 추가해줌

for i in range(len(numbers)):                               # 카운팅한 리스트 루프
    for j in range(numbers[i]):                             # 나온 횟수 만큼
            print(i)                                        # 출력 해줌
