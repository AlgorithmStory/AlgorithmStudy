import sys
n = int(input())
tree = {}
for _ in range(n):
    x = sys.stdin.readline().split()
    tree[x[0]] = [x[1],x[2]]                    # 딕셔너리 형태로 저장

def pre(a):                                     # 전위순회
    if a == '.':                                # 노드가 없으면 끝냄
        return
    print(a, end="")                            # 들어온 문자를 출력
    pre(tree[a][0])                             # 왼쪽부터 재귀
    pre(tree[a][1])                             # 오른쪽 재귀

def inor(a):                                    # 중위순회
    if a == '.':                                # 노드가 없으면 끝냄
        return
    inor(tree[a][0])                            # 왼쪽부터 재귀
    print(a, end='')                            # 노드 끝에서 부터 프린트
    inor(tree[a][1])                            # 다하면 오른쪽 재귀

def post(a):                                    # 후위순회
    if a == '.':                                # 노드가 없으면 끝냄
        return
    post(tree[a][0])                            # 왼쪽 노드 끝까지 내려가고
    post(tree[a][1])                            # 오른쪽 노드 끝까지 내려간 후 
    print(a, end='')                            # 문자 출력

pre('A')
print()
inor('A')
print()
post('A')