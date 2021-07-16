from collections import deque

# 입력.
n,m = map(int, input().split(" "))
target_arr = list(map(int, input().split(" ")))

# 입력에 대한 정보대로, 탐색 데큐 생성.
arr = deque(i for i in range(1,n+1))

# 결과.
result_check = 0

# 타겟 지정 인덱스.
target_index = 0

# 타겟을 다 뺄때까지.
while target_index < m:

    # 타겟을 뺄때마다, 타겟 값의 위치가 바뀌기 때문에, 매번 가져옴.
    sub_index = arr.index(target_arr[target_index])

    # 가져온 타겟의 위치가 제일 앞이면, 없애주고, target_index 증가.
    if sub_index == 0:
        arr.popleft()
        target_index += 1

    # 가져온 타겟의 위치가 제일 앞이 아니면,
    else:
        # 앞에서 가까운지, 뒤에서 가까운지 계산하고,
        if sub_index < len(arr) - sub_index:
            # 앞에서 가깝다면, 뺄 수 있을때까지, 뒤로 보내줌.
            while arr[0] != target_arr[target_index]:
                arr.append(arr.popleft())
                result_check += 1
        else:
            # 뒤에서 가깝다면, 뺄 수 있을때까지, 앞으로 보내줌.
            while arr[0] != target_arr[target_index]:
                arr.appendleft(arr.pop())
                result_check += 1

# 출력.
print(result_check)
