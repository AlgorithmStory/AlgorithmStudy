n = int(input())
m = int(input())

result = [0 for _ in range(n+1)]            # 관계 없음 = 0 으로 초기화
a = [[] for _ in range(n+1)]

for _ in range(m):                      
    x,y = map(int, input().split())
    a[x].append(y)                          # 친구 관계 쌍을 해당 리스트에 저장  
    a[y].append(x)                          # 반대 상황도 저장

for i in a[1]:                              # 상근이 1이니까 인덱스 1 리스트는 상근이 친구
    result[i] = 1
    for j in a[i]:                          # 친구의 친구도 친구
        if result[j] == 0 and j != 1:       # 결과값에 없고 1은 상근이니까 제외하면
            result[j] = 1                   # 친구 = 1

print(sum(result))                          # 1을 다 합해줌