import sys

length_of_list = int(sys.stdin.readline().split()[0])       # 리스트 길이 읽어옴
strings = []

for i in range(length_of_list):                             # 리스트에 단어 추가
    strings.append(sys.stdin.readline().split()[0])

strings_set = set(strings)                                  # 증복값 삭제
strings = list(strings_set)
strings.sort(key=lambda x: (len(x), x))                     # 정렬 (1번째는 길이순, 2번째는 사전순)

for i in strings:                                           # 정답 출력
    print(i)
