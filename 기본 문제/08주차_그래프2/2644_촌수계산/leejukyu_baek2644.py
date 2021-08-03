import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

x, y = map(int, input().split())

m = int(input())

a = [[] for _ in range(n+1)]

for _ in range(m):                          # 부모 자식 관계 리스트에 저장
    i,j = map(int, input().split())     
    a[i].append(j)
    a[j].append(i)

cnt = 0
visit = [0]*(n+1)

def dfs(a,x,visit,cnt):
    cnt += 1                                # 촌수가 늘어나면 1 추가
    visit[x] = cnt                          # 해당 번호에 촌수 저장
    
    for i in a[x]:                          # 
        if visit[i] == 0:                   # 방문 안했으면
            dfs(a,i,visit,cnt)              # 함수 실행
    return visit                            # 촌수 리스트 출력

result = dfs(a,x,visit,cnt)

print(result[y]-1)                          # x의 촌수 중 y와의 관계 출력