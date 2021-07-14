from sys import stdin

# 테스트 케이스 입력.
test_case = int(stdin.readline())

# 테스트 케이스 만큼 실행됨.
for _ in range(test_case):

    # 입력.
    m,n = map(int, stdin.readline().split(" "))
    arr = list(map(int, stdin.readline().split(" ")))

    # 입력 받은 배열에 대해서, 정렬 버전 하나 더 만듬.
    max_priority_arr = arr.copy()
    max_priority_arr.sort()

    result_check = 0 # 돌리는 횟수 (결과).
    index = 0 # 탐색 인덱스.
    while True:

        # 만약 지금 탐지된 요소가, 가장 우선순위가 높은 요소보다 우선순위가 낮다면,
        if arr[index] < max_priority_arr[-1]:
            arr.append(arr[index]) # 탐지된 요소를, 배열의 젤뒤로 보내줌.
            if index == n: # 만약 탐지된 요소가, 우리가 지정 받은 n 번째 요소라면,
                n = len(arr)-1 # 젤 뒤의 인덱스를 찍어줌.

        # 만약 지금 탐지된 요소의 우선순위가 가장 높거나 같다면,
        else:
            max_priority_arr.pop() # 우선순위 배열에 대해서, 마지막껄 없애줌.
            result_check += 1 # check.
            if index == n: # 만약 탐지된 요소가, 우리가 지정 받은 n 번째 요소라면,
                break # 끝냄.

        # 인덱스는 매번 증가 시킴. 앞에 요소를 없애는게 아니라, 그대로 냅두고, 뒤에 쌓으면서, 탐색하기 때문.
        # 배열의 앞, 중간 요소를 삭제 한다는건 꽤나 비용이 많이 드는 행위임. 그래서 이 방식을 택한거.
        index += 1

    # 출력.
    print(result_check)
