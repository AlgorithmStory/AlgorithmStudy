import sys
N = int(sys.stdin.readline())

result = []
for i in range(N):
    input_0 = int(sys.stdin.readline())
    result.append(input_0) # 입력값 받아오는 순간 result에 저장

# result.sort() # 오름차순 정렬
# for i in result:
#     print(i)

prt = []
for a in range(N): # a는 N만큼 돌고
    for i in result: # i는 result값 받아옴
        if i == min(result): # 만약에 i가 result 최소값이면
            prt.append(i) # prt list에 result최소값인 i저장후
            result.remove(i) # result list에서 result최소값인 i제거
            break # for i 문 멈춤

for i in prt:
    print(i)