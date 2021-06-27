import sys
N = int(sys.stdin.readline())

result = []
for i in range(N):
    input_0 = int(sys.stdin.readline())
    result.append(input_0) # 입력값 받아오는 순간 result에 저장

result.sort() # 오름차순 정렬
for i in result:
    print(i)