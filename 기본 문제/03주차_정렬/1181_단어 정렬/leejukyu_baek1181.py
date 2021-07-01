import sys

N = int(input())
a = [sys.stdin.readline().split()[0] for _ in range(N)] # 입력받기

a = list(set(a))                                        # 겹치는 단어 없애주기
a.sort(key = lambda x:(len(x),x))                       # 글자 수 대로 알파벳 순서대로 정렬

for i in a:                                             
    print(i)