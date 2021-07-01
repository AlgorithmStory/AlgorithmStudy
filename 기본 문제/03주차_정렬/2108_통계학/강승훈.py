from sys import stdin

# 입력 받고 바로 정렬.
n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]
arr.sort()

max_value = arr[n-1] # 젤 큰 값.
min_value = arr[0] # 젤 작은 값.
center_value = arr[int(n/2)] # 중앙 값.
mean_value = int(round(sum(arr)/n, 0)) # 평균 값.
range_value = max_value-min_value # 범위 값.

# ------------------------------- 최빈 값 구하는 구문.
# 딕셔너리에 빈도 저장함.
dict = {}
for crnt in arr:
    key = crnt
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

# 그리고 딕셔너리를 탐색할 키 값 구함.
keys = list(set(arr))

# 딕셔너리에서 빈도수가 가장 많은 것이 여러개라면, 그 여러개에 대한 키 값만 빼올거임.
min_arr = [] # 가장 큰 값들의 키값 숫자 담는 배열.
fre_max = 0 # 지금 까지 탐색한것 중에서 가장 큰 값 저장 (가장 큰 값 = 가장 빈도가 많은 수)
for key in keys:
    if key in dict:
        sub = dict[key]
        if sub > fre_max:
            min_arr.clear()
            min_arr.append(key)
            fre_max = sub
        elif sub == fre_max:
            min_arr.append(key)

# 실제로 딕셔너리에 빈도수가 가장 많은게 여러개라면, 정렬해서 두번째 값 가져옴.
if len(min_arr) > 1:
    min_arr.sort()
    fre_value = min_arr[1]
else: # 아니면 걍 첫번째 ㄱ-
    fre_value = min_arr[0]
# ------------------------------- 최빈 값 구하는 구문 끝.

# 출력
print(mean_value)
print(center_value)
print(fre_value)
print(range_value)
