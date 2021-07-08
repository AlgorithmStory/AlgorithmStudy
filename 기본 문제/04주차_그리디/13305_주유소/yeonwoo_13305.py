import sys

N = int(sys.stdin.readline().rstrip()) # 백준 제출용

distance = list(map(int, sys.stdin.readline().split()))
distance.append(0) 
# 거리는 오일보다 인풋값이 하나가 작기 때문에 
# 비교용으로 0을 마지막에 하나 추가 시켜주고 index길이를 맞춰줌

oil_price = list(map(int, sys.stdin.readline().split()))

total_oil_price = oil_price[0] * distance[0]
# 처음 주유소에서 무조건 충전시키고 가야함
# 5 * 2 = 10

min_oil_price = oil_price[0]
# 첫주유소의 기름 가격을 default값으로 설정하고 함
# 5

for i in range(1, N): 
# 이미 충전시키고 가서 2번째 주유소부터 구하면됨
    if oil_price[i] < min_oil_price:
        # 주유소의 기름이 전에 주유소 보다 싸면 
        # 2 < 5, 4 < 2 X, 1 < 2
        min_oil_price = oil_price[i] 
        # print(min_oil_price)
        # 2, 1
        
    
    total_oil_price = total_oil_price + (min_oil_price * distance[i])
    # print(total_oil_price)
    # 10 + (2 * 3) = 16, 16 + (2 * 1) = 18, 18 + (2 * 0) = 18
    

print(total_oil_price)