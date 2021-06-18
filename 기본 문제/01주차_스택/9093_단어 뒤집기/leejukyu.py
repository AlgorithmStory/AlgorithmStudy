T = int(input())
for i in range(T):
    a = input().split()
    for j in a:
        for k in j[::-1]:
            print(k, end="")
        print(end = " ")