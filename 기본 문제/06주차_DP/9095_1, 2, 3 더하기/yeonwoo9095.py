import sys
T = int(sys.stdin.readline())

# n = 1 출력 1 # n = 2 출력 2 # n = 2 출력 2 # n = 3 출력 4 # n = 4 출력 7 
# 위의 결과로 보면 출력은 = n-1출력 + n-2출력 + n-3출력인것 같다.
# 밑에서 코드로 만들어서 확인해보겠다.

output_base = [0, 1, 2, 4] 
# output_base의 인덱스 값이 각각의 출력값이 된다.
# 0, 1, 2, 4를 기본으로 주고 시작한다.

for i in range(4, 11): 
    # 문제에 보면 n이 11보다 작다고 주어져 있다. 
    output_base.append(sum(output_base[-3:])) # n-1출력 + n-2출력 + n-3출력

output_result = []
for i in range(T): # 테스트 케이스 입력
    output_result.append(int(sys.stdin.readline()))

for i in output_result: # 결과
    print(output_base[i])
