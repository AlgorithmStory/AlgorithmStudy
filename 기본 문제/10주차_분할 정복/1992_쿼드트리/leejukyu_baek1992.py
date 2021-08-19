import sys

n = int(input())
a = []
for _ in range(n):                                              # 입력받기    
    arr = []
    d = input()
    for i in d:
        arr.append(i)
    a.append(arr)  

result = []                                                     # 결과 저장 리스트

def div(x, y, n):
    color = a[x][y]                                             # 시작 위치 색 저장
    for i in range(x, x+n):                                     
        for j in range(y, y+n):                    
            if a[i][j] != color:                                # 색이 다르면 분할
                result.append('(')                              # 분할 시작할때 '(' 추가
                div(x, y, n//2)                                 # 쿼드분할
                div(x, y+n//2, n//2)
                div(x+n//2, y, n//2)
                div(x+n//2, y+n//2, n//2)
                result.append(')')                              # 분할 끝날때 ')' 추가
                return                                          # 진행 멈춤
    result.append(color)                                        # 색이 같으면 색 추가

div(0,0,n)                                                      # 함수실행

for k in result:
    print(k, end="")                                            # result값 붙여서 출력