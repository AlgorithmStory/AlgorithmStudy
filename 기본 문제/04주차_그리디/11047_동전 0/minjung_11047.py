from sys import stdin

n, price = map(int, stdin.readline().split()) # 동전죵류갯수와 동전조합으로 만들 가격을 입력받는다
w = [0]*n # 동전종류들을 저장할 리스트 초기화
i = len(w)-1 # 리스트'w'를 핸들링할 인덱스 초기화
c = 0 # 최소한의 필요로하는 동전 갯수 초기화

for i in range(n):
    w[i] = int(stdin.readline()) # 동전 종류들 저장

while price > 0: # 가격이 0이상일때만 (아래 code 14 줄에서 price 가격을 coin 갯수 연산을위해 갱신할 예정 )

        c += price//w[i] # 동전종류가 w[i]일때 동전 갯수 저장 ex) 가격이 4200이고 20000일떄 4200//20000 = 0 이므로 c는 0 
        price = price - ((price//w[i]) * w[i])# 그다음 동전갯수를 연산하기위해 현재 동전갯수 * 동전가격 만큼 price 에서 뺸값 갱신
        i -= 1 # 위와 같은 이유로 w[i] 의 인덱스 i 갱신

print(c)# 최종 동전갯수 출력
