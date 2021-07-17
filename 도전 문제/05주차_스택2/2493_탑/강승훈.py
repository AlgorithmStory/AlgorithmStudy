# 출력.
n = int(input())
arr = list(map(int, input().split(" ")))

# 탐색하면서 요소를 집어넣을 변수들, 제일 왼쪽은 미리 하나 넣어둠.
max_stack = [arr[0]] # 요소의 높이.
max_index = {arr[0]:0} # 요소의 위치.
result_stack = [0] # 결과.

# 왼쪽부터 두번째 요소부터 탐색,
for i in range(1, n):

    # 현재 요소와, max_stack의 마지막 요소와 비교하면서, pop또는 추가 할거임.
    while len(max_stack) > 0:

        # 현재 요소가 max_stack의 마지막 요소보다 크다면,
        # 이후에 나올 요소들은 스택의 마지막요소의 영향을 전혀 받지 않기 때문에 pop하고 다음 스택의 마지막을 보러감.
        if arr[i] > max_stack[-1]:
            del max_index[max_stack.pop()]

        # 만약 현재의 요소가 더 작다면,
        else:
            # 결과로 max_stack의 마지막 요소의 위치 값을 넣어주고,
            result_stack.append(max_index[max_stack[-1]]+1)

            # max_stack과 max_index에 현재의 요소를 넣어주고 break.
            max_stack.append(arr[i])
            max_index[arr[i]] = i
            break

    # 위의 while문이 끝났을때, max_stack에 아무것도 들어있지 않다면, 현재의 요소가 이전(왼쪽)의 요소들 중에,
    # 제일 크다는 의미니까, 현재의 요소를 넣어주고, 계속 진행함.
    if len(max_stack) == 0:
        result_stack.append(0)
        max_stack.append(arr[i])
        max_index[arr[i]] = i

# 출력.
print(*result_stack)
