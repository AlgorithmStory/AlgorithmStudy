import sys

n = int(input())
a = [int(x) for x in sys.stdin.readline().split()]      # 검사 리스트 입력
a.sort()                                                # 오름차순으로 정렬
m = int(input())
b = [int(x) for x in sys.stdin.readline().split()]      # 비교 리스트 입력

def search(a, i, start, end):
    while start <= end:                                 # 분할이 가능하면 반복
        mid = (start+end)//2                            # 중앙값을 기준으로
        if a[mid] == i:                                 # 해당 값이 비교값이면
            return 1                                    # 존재하니까 1 리턴
        elif a[mid] > i:                                # 중앙값이 비교값보다 크면
            end = mid-1                                 # 중앙값보다 작은수가 있는 범위만 탐색
        else:                                           # 중앙값이 비교값보다 작으면
            start = mid + 1                             # 중앙값 보다 큰 수가 있는 범위만 탐색
    return 0                                            # 없으면 0 리턴

for i in b:
    print(search(a, i, 0, n-1))                         # 비교 리스트 하나씩 넣어서 함수 실행
