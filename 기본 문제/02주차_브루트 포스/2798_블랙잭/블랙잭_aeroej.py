import sys


def isMax(num):
  global maX
  if num <= m and num > maX:
    maX = num


def dfs(v, cnt):
  if cnt >= 3:
    isMax(sum(lst))
    return
  if v >= len(cards):
    return

  lst.append(cards[v])
  dfs(v+1, cnt+1)
  lst.pop()
  dfs(v+1, cnt)


if __name__ == "__main__":
  n, m = map(int, sys.stdin.readline().rstrip().split())
  cards = list(map(int, sys.stdin.readline().rstrip().split()))

  lst = []
  maX = 0

  dfs(0, 0)
  print(maX)
