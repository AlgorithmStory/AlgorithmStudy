import sys

N = int(sys.stdin.readline().rstrip()) 


for i in range(1, N + 1):
    result = list(map(int, str(i))) 
    # i값을 string값으로 들고와서 나눠줌
    # 그러면  i 가 123일시 result는 [1, 2, 3]
    number = i + sum(result)
    # 위의 i가 123일때 result가 [1, 2, 3]이여서
    # 3개의 합은 6 
    # 123 + 6 = 129
    # 즉 i가 생성자 number는 분해합
    if number == N: # 분해합이 N가 같아지면
        print(i) # 생성자 출력후
        break #  for문 탈출

    if i == N: # 생성자가 없는 경우에는 0
        print(0)
