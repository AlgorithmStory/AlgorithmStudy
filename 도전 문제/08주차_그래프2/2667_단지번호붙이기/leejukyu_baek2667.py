import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

a = []
for _ in range(n):                                                  # 지도 입력
    arr = []
    d = input()
    for i in d:
        i = int(i)
        arr.append(i)
    a.append(arr)    

result = {}
def dfs(x,y):
    if x > -1 and y > -1 and x <= (n-1) and y <= (n-1):             # 지도를 벗어나지 않는다면
        if a[x][y] == 1:                                            # 집이 있을 때
            a[x][y] = cnt                                           # 단지 번호로 바꿔줌
            result[cnt] += 1                                        # 단지 번호에 연결된 집 카운트해서 딕셔너리로 넣기
            dfs(x-1,y)                                              # 4방향 탐색
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)
cnt = 1                                                             # 단지 번호
for i in range(n):      
    for j in range(n):
        if a[i][j] == 1:                                            # 집이 있으면
            cnt += 1                                                # 1로 표시되어있으니까 2부터 단지 번호 시작
            result[cnt] = 0                                         # 단지 번호를 키값으로 딕셔너리 초기화
            dfs(i,j)                                                # 함수 실행

result = sorted(result.items(), key=lambda x : x[1])                # 집 수 오름차순
print(cnt-1)                                                        # 2부터 시작했으니까 -1
for i in range(len(result)):        
    print(result[i][1])                                             # 단지 내 집 수 출력