n = int(input())
stack = []  # 스택
ans = []  # +, -를 넣을 리스트
ls = [int(input()) for _ in range(n)]
idx = 0  # ls의 확인 인덱스
top = -1
yes = True
i = 1
while idx < len(ls):
    if top == -1:
        stack.append(i)  # 숫자가 들어간다.
        ans.append("+")
        top += 1
        i += 1
    if stack[top] == ls[idx]:
        stack.pop()
        ans.append("-")
        top -= 1
        idx += 1
    elif stack[top] < ls[idx]:
        stack.append(i)  # 숫자가 들어간다.
        ans.append("+")
        top += 1
        i += 1
    else:
        yes = False
        break
if yes:
    for i in ans:
        print(i)
else:
    print("NO")
