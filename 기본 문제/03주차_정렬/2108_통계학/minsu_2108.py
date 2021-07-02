from sys import stdin

N = int(stdin.readline())
num = []

for _ in range(N):
    num.append(int(stdin.readline()))
num.sort()

# 산술평균
print("%.f"%(sum(num)/N))  

# 중앙값
print(num[N//2])

# 최빈값
x = {}

for i in num:                                                   # dict에 key값으로 숫자, value값으로 빈도수가 생김
    if i in x:
        x[i] += 1
    else:
        x[i] = 1

x = sorted(x.items(), key = lambda x : x[1], reverse = True)    # items를 이용하여 key값과 value값을 튜플로 묶어 리스트로 만들어 준다.
                                                                # lambda를 이용하여 빈도값을 기준으로 내림차순(reverse = True)으로 정렬

if N != 1:                                                      # 입력값이 1개가 아닐때
    if x[0][1] == x[1][1]:                                      # 첫번째 숫자의 빈도수와 두번째 숫자의 빈도수가 같으면 두번째 숫자를 출력(sort를 했기 때문에 두번째로 작은수 출력)
        print(x[1][0])
    else: print(x[0][0])
else:
    print(x[0][0])

# 범위
print(max(num) - min(num))