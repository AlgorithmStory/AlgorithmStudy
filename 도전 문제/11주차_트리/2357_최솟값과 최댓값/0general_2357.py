'''
https://www.acmicpc.net/problem/2357
'''
import sys
import math

# 세그먼트 트리 min값 초기화


def initMin(arr, tree, node, start, end):  # start는 범위 시작, end는 범위 마지막
    if start == end:  # 리프 노드
        tree[node] = arr[start]  # 초기화하려는 tree의 node
    else:  # 리프 노드가 아닐 때
        tree[node] = min(initMin(arr, tree, node*2+1, start, (start + end)//2),
                         initMin(arr, tree, node*2+2, (start + end)//2+1, end))
    return tree[node]

# 세그먼트 트리 max값 초기화


def initMax(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        tree[node] = max(initMax(arr, tree, node*2+1, start, (start + end)//2),
                         initMax(arr, tree, node*2+2, (start + end)//2+1, end))
    return tree[node]


def findMin(mintree, node, start, end, l, r):
    if start > r or end < l:
        return 1000000001
    elif l <= start and end <= r:
        return mintree[node]
    else:
        return min(findMin(mintree, node*2+1, start, (start+end)//2, l, r),
                   findMin(mintree, node*2+2, (start+end)//2+1, end, l, r))


def findMax(maxtree, node, start, end, l, r):
    if start > r or end < l:
        return 0
    elif l <= start and end <= r:
        return maxtree[node]
    else:
        return max(findMax(maxtree, node*2+1, start, (start+end)//2, l, r),
                   findMax(maxtree, node*2+2, (start+end)//2+1, end, l, r))


# main
n, m = list(map(int, sys.stdin.readline().split()))
arr = [int(sys.stdin.readline()) for _ in range(n)]
height = int(math.ceil(math.log2(n)))

mintree = [0] * (pow(2, height+1)-1)
maxtree = [0] * (pow(2, height+1)-1)

initMin(arr, mintree, 0, 0, n-1)
initMax(arr, maxtree, 0, 0, n-1)

for _ in range(m):
    l, r = list(map(int, sys.stdin.readline().split()))
    print(findMin(mintree, 0, 0, n-1, l-1, r-1), end=' ')
    print(findMax(maxtree, 0, 0, n-1, l-1, r-1))
