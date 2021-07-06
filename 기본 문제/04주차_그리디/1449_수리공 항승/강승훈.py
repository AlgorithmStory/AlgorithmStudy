# 입력
n, l = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr.sort()

cnt = 0 # 테이프 사용 횟수.
index_1 = n-1 # 물이 새는 곳을 가리킬 인덱스1.
index_2 = 1 # 물이 새는 곳을 가리킬 인덱스2.

# 오른쪽에서부터 왼쪽으로 탐색함.
while True:
    if (index_1-index_2) < 0: # 왼쪽 테이프를 가리키는 위치 값이, 0보다 작으면 cnt+=1 해주고 빠져나감.
        cnt += 1
        break
    sub = arr[index_1] - (arr[index_1 - index_2]) # 오른쪽과 왼쪽 거리 차이.
    if sub >= l: # 그 차이 값이 테이프 길이 이상이면, 더 이상 테이프를 늘릴 수 없으니, 카운트 처리.
        cnt += 1
        index_1 -= index_2 # 인덱스 갱신.
        index_2 = 1
    else:
        index_2 += 1 # 계속 테이프를 늘림.

# 출력.
print(cnt)
