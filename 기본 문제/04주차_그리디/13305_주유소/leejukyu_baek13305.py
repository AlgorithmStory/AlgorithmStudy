import sys

N = int(input())
km = [int(x) for x in sys.stdin.readline().split()]
price = [int(x) for x in sys.stdin.readline().split()]

min_p = price[0]                                            # 첫 도시의 리터당 가격을 최소비용에 등록
cost = 0                                                    # 총 비용

for i in range(1, N):
    cost += min_p * km[i-1]                                 # 최소 비용과 가야하는 거리를 곱해서 총 비용에 합해줌

    if min_p > price[i]:                                    # 다음 도시의 가격이 더 저렴하면
        min_p = price[i]                                    # 최소 비용 업데이트

print(cost)