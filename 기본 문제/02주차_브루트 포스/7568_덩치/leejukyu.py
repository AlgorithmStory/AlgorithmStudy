import sys

N = int(sys.stdin.readline())                               # 사람 수 입력받기 
lst = []                                                    # 몸무게, 키가 들어갈 빈 리스트
for _ in range(N):                                          # 사람 수 만큼 입력받은 데이터 리스트에 넣기
    k = list(map(int, sys.stdin.readline().split()))
    lst.append(k)

num = []                                                    # 등수가 들어갈 빈 리스트
 
for i in range(N):                                          
    cnt = 1                                                 
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]: # 몸무게랑 키 둘 다 비교 대상보다 작으면
            cnt +=1                                         # 한 등수 내려가기
    num.append(cnt)
print(*num)