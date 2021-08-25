from sys import stdin

# 입력.
n = int(stdin.readline())

# 트리 구조 담을 딕셔너리.
tree_dict = {}

# 입력.
for i in range(n):
    a,b,c = map(str, stdin.readline().strip().split(" "))
    tree_dict[a] = [b,c]

# -------------------
# 재귀적으로.
def preor(node):
    if node != ".":
        print(node, end="")
        preor(tree_dict[node][0])
        preor(tree_dict[node][1])

def inor(node):
    if node != ".":
        inor(tree_dict[node][0])
        print(node, end="")
        inor(tree_dict[node][1])

def postor(node):
    if node != ".":
        postor(tree_dict[node][0])
        postor(tree_dict[node][1])
        print(node, end="")
# -------------------

# 출력.
key = "A"
preor(key)
print()
inor(key)
print()
postor(key)
