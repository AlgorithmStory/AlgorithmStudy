'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys
n = int(sys.stdin.readline())

stack=[]
result = []
for i in range(n):
    input_a = sys.stdin.readline().split()

    if input_a[0] == 'push': 
        # input_a가 스페이스를 눌려서 값이 두개되면 첫번째 입력값 을 들고와 비교
        # 예시 push 0 이면 push만 가져와서 비교
        stack.append(int(input_a[1])) # 여기선 두번째 입력값인 0을 int값으로 stack에 넣음

    if input_a[0] == 'pop':
        if len(stack) == 0:
            result.append(-1) # stack이 비어있으면 -1
        else:
            result.append(stack.pop()) # stack이 비어있지 않으면 마지막 push값 제거

    if input_a[0] == 'size':
        result.append(len(stack)) # 스택의 길이

    if input_a[0] == 'empty':
        if len(stack) == 0:
            result.append(1) # stack이 비어있으면 1
        else:
            result.append(0) # stack이 비어있지 않으면 0

    if input_a[0] == 'top':
        if len(stack) == 0:
            result.append(-1) # stack이 비어있으면 -1
        else:
            result.append(stack[-1]) # stack이 비어있지 않으면 stack의 가장 마지막값 

for j in range(len(result)):
    print(result[j])