from sys import stdin

n = int(stdin.readline())
memo = [0 for _ in range(10000)] # 입력되는 수의 범위가 10000이하의 자연수이고, 수의 값을 인덱스로 활용 하기위해, 수가 들어오는 최대 값만큼 배열 생성.

# n개의 수를 입력 받자마자, 방금 위에서 생성한 배열의 인덱스에 값으로써 1씩 증가 시킴.
for _ in range(n):
    memo[int(stdin.readline())-1] += 1

# memo 배열 전체를 한번 훑어야됨.
for i in range(1, 10001):
    if memo[i-1] != 0: # memo 배열의 현재 위치가 0이라는건 이 값이 한번도 입력이 되지 않았다는거임.
        for _ in range(memo[i-1]): # 현재 위치의 값의 크기는, 현재 인덱스의 값이 몇번 입력으로 들어왔냐를 나타냄.
            print(i) # 그 값 만큼 출력 하면 됨.
