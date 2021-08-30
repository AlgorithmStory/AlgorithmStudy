import sys


class Trie(object):
    def __init__(self):
        self.head = {}

    def insert(self, food):
        curr = self.head

        for i in food:
            if i not in curr:
                curr[i] = {}
            curr = curr[i]
        curr["end"] = True

    def food_print(self, curr, level):
        if "end" in curr:
            return

        children = sorted(curr)  # 자식들 사전 순 정렬

        for i in children:
            print("--"*level + i)
            self.food_print(curr[i], level+1)


n = int(sys.stdin.readline().rstrip())

trie = Trie()
for _ in range(n):
    trie.insert(list(sys.stdin.readline().rstrip().split())[1:])
trie.food_print(trie.head, 0)
