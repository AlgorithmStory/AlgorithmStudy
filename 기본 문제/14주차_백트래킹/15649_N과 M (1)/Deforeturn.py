n,m = map(int, input().split(" "))
arr = []
visitied = [False for _ in range(n)]
def recursion(depth):
    if depth == m:
        print(*arr)
        return
    for i in range(n):
        if not visitied[i]:
            arr.append(i+1)
            visitied[i] = True
            recursion(depth+1)
            visitied[i] = False
            arr.pop()

recursion(0)
