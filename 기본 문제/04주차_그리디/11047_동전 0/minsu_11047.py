from sys import stdin

N, K  = stdin.readline().split()
N = int(N)
K = int(K)

money_list = []
for _ in range(N):
    money_list.append(int(stdin.readline()))

money_list.sort(reverse=True)

num = 0

for i in money_list:  
    if i <= K:                                  # K보다 작은 값 중 가장 큰 값부터 계산
        a = K//i                                # a는 i동전의 개수
        K = K - i * a 
        num += a                                # num에 동전의 개수를 더해준다.


print(num)