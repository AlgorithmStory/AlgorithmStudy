import sys
N = int(input())
a = [int(x) for x in sys.stdin.readline().split()]

stack = [a[-1]]
result = [-1]
for i in range(len(a)-2,-1,-1):                             # 리스트에 첫번째는 미리 넣어놨기 때문에 두번째부터 거꾸로 넣어줌
    while len(stack) > 0 and a[i] >= stack[-1]:             # 스택에 1개 이상 수가 들어가 있고 a값이 스택 마지막 보다 크다면
        stack.pop()                                         # 스택의 마지막 수는 필요 없기 때문에 지워줌
            
    if len(stack) == 0:                                     # 스택에 아무것도 남지 않으면
        result.append(-1)                                   # 오른쪽 수보다 큰 수이므로 -1 넣어줌
    else:
        result.append(stack[-1])                            # 리스트의 가장 마지막이 a보다 큰 수
    
    stack.append(a[i])                                      # a를 스택에 넣어줌

for i in result[::-1]:                                      # 오른쪽 부터 계산했기 때문에 결과는 반대로 출력
    print(i , end = ' ')