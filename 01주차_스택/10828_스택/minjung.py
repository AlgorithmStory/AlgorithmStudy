import sys

stack = []
top_v = -1

def pop():
    global stack, top_v
    if top_v == -1:
        print(top_v)
    else:
        print(stack[top_v])
        del stack[top_v]
        top_v -= 1  

def push(n):
    global top_v
    stack.append(n)
    top_v += 1

def size():
    global top_v
    print(top_v + 1)

def empty():
    global top_v
    if top_v == -1:
        print(1)
    else:
        print(0)

def top():
    global stack, top_v
    if top_v == -1:
        print(top_v)
    else:
        print(stack[top_v])


# 코드 시작문
if __name__ == '__main__':
    loop = int(sys.stdin.readline())
    for i in range(loop):
        full_statement = sys.stdin.readline().split()
        if len(full_statement) == 2:
            statement, num = full_statement[0], full_statement[1]
            num = int(num)    
            push(num)
        else:
            statement = full_statement[0]
            if statement == 'pop':
                pop()
            elif statement == 'size':
                size()
            elif statement == 'empty':
                empty()  
            elif statement == 'top':
                top()