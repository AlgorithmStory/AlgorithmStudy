# 첨엔, 질문 자체가 길어서 겁먹었는데 읽어보니까, 단순히 탐색만하면 되는 문제였다.
# 문제에서도 나왔다시피, 오른쪽에서 봤을때, 보이는 막대의 수를 반환하는건데,
# 직관적으로 오른쪽에서 순차적으로 탐색하면서, 이전에 나왔던 막대보다 큰 막대면 count 해주고,
# 마지막에 count 자체를 반환 해줌.

from sys import stdin

n = int(input())
sticks = [int(stdin.readline()) for _ in range(n)]

height_save = sticks[-1]
cnt = 1

for crnt in reversed(sticks):
    if crnt > height_save:
        cnt += 1
        height_save = crnt

print(cnt)
