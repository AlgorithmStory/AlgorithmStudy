from sys import stdin

N = int(stdin.readline())
word = []

for _ in range(N):
    word.append(stdin.readline().strip())               # 문자열의 경우 readline만 쓰면 '\n'도 같이 출력되기 때문에 strip을 사용

word = list(set(word))                                  # set을 이용하면 {}로 바뀌기 때문에 list를 사용하여 []로 바꿔준다.

for i in sorted(word, key = lambda x : (len(x), x)):    # lambda를 사용하여 글자 순, 알파벳 순으로 정렬
    print(i)
