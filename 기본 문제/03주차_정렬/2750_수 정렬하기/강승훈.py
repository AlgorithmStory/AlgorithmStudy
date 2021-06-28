from sys import stdin

# 입력
n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]

# 버블정렬
for i in range(n-1): # 조건식에서 +1 시키기 때문에, n-1 까지만 반복.
    for j in range(n-1):
        if arr[j] > arr[j+1]: # 만약 현재 요소가, 바로 다음 요소보다 크면, 두개의 위치를 바꿔줌.
            tmp_1 = arr[j]; tmp_2 = arr[j+1]  # tmp_1에 앞에 요소, tmp_2에 바로 다음 요소를 저장.
            arr[j] = tmp_2; arr[j+1] = tmp_1 # 그리고 반대로 다시 재할당 시킴.


# 출력
for crnt in arr:
    print(crnt)
