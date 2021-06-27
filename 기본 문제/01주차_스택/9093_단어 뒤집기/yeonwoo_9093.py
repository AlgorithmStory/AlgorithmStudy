import sys
N = int(sys.stdin.readline())


for i in range(N):
    input_0 = list(sys.stdin.readline().rstrip().split())

    result = []
    for j in input_0:
        result.append(j[::-1]) # 입력받은 값 값을 거꾸로 해줌

    print(*result) # 가변인자로 받아와서 입력 받은 값 끝까지 출력

