import sys

n = int(sys.stdin.readline())

for _ in range(n):
  words = sys.stdin.readline().rstrip().split()  # 맨 끝의 개행문자 제거, 공백을 기준으로 split

  for word in words:
    print(word[::-1], end=' ')  # 슬라이스로 단어 역순 출력
  print()