import sys

T = int(input())

for j in range(T):
    a = sys.stdin.readline()
    b = []
    c = 0

    for i in a:
        if i == "(":
            b.append(i)

        elif i == ")":
            try: b.pop()

            # 예외 처리, 오류가 나면 (b 리스트 안에 "("가 없으면) c =1 
            except: 
                c = 1
                break

    # "(" 가 남으면 c = 1
    if len(b) >= 1:
        c = 1

    if c == 1:
        print("NO")
    else: print("YES")
