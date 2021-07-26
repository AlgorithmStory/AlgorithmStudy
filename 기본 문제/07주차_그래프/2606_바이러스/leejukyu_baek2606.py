N = int(input())
k = int(input())

arr = []
for i in range(k):                          # 정렬해서 리스트에 넣기
    a = [int(x) for x in input().split()]
    a.sort()
    arr.append(a)

result = []

def graph(i, result):                       # 컴퓨터 번호와 결과를 받는 함수
    result.append(i)                        # 번호가 들어오면 저장
    for k in range(len(arr)):               # 리스트의 길이만큼 반복
        if i in arr[k]:                     # 해당 번호가 있는 리스트면
            for j in arr[k]:                # 리스트 안의 번호를 확인 할 때
                if j not in result:         # 저장되지 않은 번호라면
                    graph(j, result)        # 함수 재귀 실행

graph(1, result)                            # 1번 컴퓨터 부터 시작
print(len(result)-1)                        # 1번은 빼고 감염된 컴퓨터 개수