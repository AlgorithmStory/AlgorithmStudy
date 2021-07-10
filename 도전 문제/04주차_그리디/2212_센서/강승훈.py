# 입력
n = int(input())
k = int(input())
n_arr = list(map(int, input().split(" ")))

result = 0 # 정답.

# 센서의 개수가 지어야할 집중국의 개수보다 작거나 같으면, 모든 부분을 커버 가능하기 때문에, 바로 0 반환.
if n <= k:
    # 결과_1.
    print(result)
else: # 그게 아니라면,
    n_arr.sort() # 일단 받은 arr에 대해서 오름차순 정렬.

    # 정렬된 arr에 대해서, 서로의 차이 값을 구할 변수와 로직.
    n_diff_arr = []
    for i in range(0, n - 1):
        first_number = n_arr[i]
        second_number = n_arr[i + 1]
        if first_number != second_number:
            n_diff_arr.append(second_number - first_number)
    n_diff_arr.sort(reverse=True) # 차이 값을 내림차순으로 정렬.

    # 지어야 할 집중국이 많아질수록, 비용은 낮아짐.
    # 항상 최적의 위치에 집중국을 지으므로, 집중국 수에 비례해서, 비용이 큰 순으로 계산에서 제외함.
    for i in range(k-1, len(n_diff_arr)):
        result += n_diff_arr[i]

    # 결과_2.
    print(result)
