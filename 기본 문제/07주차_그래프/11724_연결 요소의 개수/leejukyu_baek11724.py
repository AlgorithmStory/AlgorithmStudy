import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

a = [[] for _ in range(N+1)]
result = [0] * (N+1)                                    # 요소 번호 0으로 초기화

for _ in range(M):
    x,y = map(int, sys.stdin.readline().split())
    a[x].append(y)                                      # 순서쌍 앞 숫자에 뒷 숫자 저장
    a[y].append(x)                                      # 반대도 저장

cnt = 1                                                 # 요소 번호

def graph(i, result):
    result[i] = cnt                                     # 재귀동안 해당되는 번호는 연결 된 요소라 같은 번호를 부여함
    for j in a[i]:                                      # 해당 인덱스 리스트도 연결 요소
        if result[j] == 0:                              # 번호가 아직 안정해 졌으면
            graph(j, result)                            # 함수 재귀 실행

for i in range(1, N+1):                                 
    if result[i] == 0:                                  # 그룹이 안정해졌으면
        graph(i, result)                                # 함수 실행
        cnt += 1                                        # 다음에 실행되면 1 증가 된 숫자가 결과에 저장
print(max(result))                                      # 가장 큰 수가 총 연결 요소 개수