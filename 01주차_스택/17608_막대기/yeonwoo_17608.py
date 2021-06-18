import sys

N = int(input("막대기 개수 입력 : "))
# N = int(sys.stdin.readline().rstrip()) # 백준 제출용

result = []

for i in range(N):
    height = int(input("{}번 막대기 길이 입력 : ".format(i+1)))
    # height = int(sys.stdin.readline().rstrip()) # 백준 제출용
    result.append(height)

count = 0
final = 0
for j in range(1, N+1):
    prt = result[-j]
    if prt > final: 
        # final 처음 값은 0이고 prt의 맨마지막 값이 final값이 되고
        # final이 계속 다음 큰 값으로 대체됨
        # 중간에 final보다 작은 값 있으면 무시
        # count 값은 if 가 true일때 + 1 이됨
        count = count + 1
        final = prt

print("{}개의 막대기중 오른쪽에서 보이는 막대기 개수는 ? {}개".format(N, count))
# print(count) # 백준 제출용