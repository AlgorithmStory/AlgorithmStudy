import sys


def isMax(num):
  global maX
  if num <= m and num > maX:
    maX = num


def dfs(v, cnt):
  if cnt >= 3:  # 플레이어가 3장을 고른 경우
    isMax(sum(lst))
    return
  if v >= len(cards):  # 모든 카드를 확인한 경우
    return

  lst.append(cards[v])
  dfs(v+1, cnt+1)  # v번째 카드를 고른 경우
  lst.pop()
  dfs(v+1, cnt)  # v번째 카드를 고르지 않은 경우


if __name__ == "__main__":
  n, m = map(int, sys.stdin.readline().rstrip().split())
  cards = list(map(int, sys.stdin.readline().rstrip().split()))

  lst = []  # 플레이어가 고른 카드
  maX = 0  # M을 넘지 않으면서 M과 최대한 가까운 카드의 합

  dfs(0, 0)
  print(maX)
