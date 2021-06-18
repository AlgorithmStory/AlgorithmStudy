import sys

count = int(input())
list_input = []
for i in range(count):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        list_input.append(int(command[1]))

    elif command[0] == 'top':
        if (len(list_input) != 0):
            print(list_input[-1])
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(list_input))

    elif command[0] == 'empty':
        if(len(list_input) == 0):
            print(1)
        else:
            print(0)

    elif command[0] == 'pop':
        if (len(list_input) != 0):
            print(list_input[-1])
            del list_input[-1]
        else:
            print(-1)