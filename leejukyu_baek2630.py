import sys
n = int(input())
a = []
for _ in range(n):
    a.append([int(x) for x in sys.stdin.readline().split()])

result = []

def div(x, y, n):
    color = a[x][y]                                             # 시작 위치의 컬러를 저장
    for i in range(x, x+n):                                     # 한 변의 길이만큼 탐색
        for j in range(y, y+n):                     
            if a[i][j] != color:                                # 시작 컬러와 색이 다르면
                div(x, y, n//2)                                 # 분할해서 탐색
                div(x, y+n//2, n//2)
                div(x+n//2, y, n//2)
                div(x+n//2, y+n//2, n//2)
                return                                          # return으로 진행을 멈추고 재귀
    if color == 1:                                              # 시작 컬러와 색이 같은데 파란색이면
        result.append(1)                                        # 1 저장
    else:                                                       # 흰색이면
        result.append(0)                                        # 0저장

div(0,0,n)                                                      # 함수 실행
print(result.count(0))                                          # 저장된 흰색 수 프린트
print(result.count(1))                                          # 저장된 파란색 수 프린트