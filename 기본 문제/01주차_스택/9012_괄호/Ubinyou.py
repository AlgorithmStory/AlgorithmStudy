import sys
n = int(sys.stdin.readline().split(" ")[0])
for i in range(n):
    paren = input()
    check = 0
    for crnt in paren:
        if crnt == "(":
            check += 1
        else:
            check -= 1
        if check < 0:
            break
    if check == 0:
        print("YES")
    else:
        print("NO")
