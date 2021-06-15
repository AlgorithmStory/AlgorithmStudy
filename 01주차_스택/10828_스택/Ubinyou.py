import sys

test_case = int(input())
stact = list()
for _ in range(test_case):
    enter = sys.stdin.readline()
    if enter[1] == "u":
        number = int(enter[5:])
        stact.insert(0, number)
    elif enter == "pop\n":
        if len(stact) == 0:
            print(-1)
        else:
            print(stact.pop(0))
    elif enter == 'size\n':
        print(len(stact))
    elif enter == "empty\n":
        if len(stact) == 0:
            print(1)
        else:
            print(0)
    elif enter == "top\n":
        if len(stact) == 0:
            print(-1)
        else:
            print(stact[0])
