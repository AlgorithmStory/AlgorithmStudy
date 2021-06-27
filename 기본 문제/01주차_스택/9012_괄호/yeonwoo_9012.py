'''
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 
‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 
구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 
만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 
그 결과를 YES 와 NO 로 나타내어야 한다. 
'''
import sys
T = int(sys.stdin.readline())

prt = []
for i in range(T):
    input_0 = sys.stdin.readline()
    result = list(input_0)
    sum = 0

    for j in result:
        if j == '(': # 연산이 올바르게 작용하려면 (로 시작하여야 함
            sum = sum + 1 # sum이 1 증가

        if j == ')': # 연산이 올바르게 작용하려면 )로 끝나야함
            sum = sum - 1 # sum이 1 감소

        if sum < 0: 
            # sum 이 0보다 작으면 no출력하고 for j문 빠져나감
            # 이유는 sum이 -1일때 연산이 ())처럼 되면 이미 잘못된 연산
            # (() 는 ) 가 올수 있어서 지켜봐야함
            prt.append('NO')
            break
    
    # sum이 -되는 값은 이미 위에서 break로 해결하여
    # sum이 +되는 값이나 0값인 경우 밖에 안남음
    if sum > 0: # sum이 1이면 ((()) 처럼 괄호가 )가 하나 빔
        prt.append('NO')

    if sum == 0: # 0 이면 ()()()든 ((()))든 (()())든 다 맞음
        prt.append('YES')

    

for i in prt:
    print(i)