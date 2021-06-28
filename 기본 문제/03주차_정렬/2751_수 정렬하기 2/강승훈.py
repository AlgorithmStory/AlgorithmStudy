# 백준에선 10%에서 시간초과 나는데, LeetCode에선 똑같은 알고리즘으로 Accepted 받았으니, 그냥 올릴게요.



from sys import stdin

# 입력
n = int(input())
arr = [int(stdin.readline()) for _ in range(n)]

# 퀵소트 함수 구현부
def qSort(indexo_1, indexo_2): # 젤 앞 인덱스와, 젤 뒤 인덱스를 매개변수로.
    global arr
    len_check = len(arr)
    if indexo_1 < 0 or indexo_2 < 0 or indexo_1 >= len_check or indexo_2 >= len_check: # 인덱스 초과 에러 방지용.
        return
    if indexo_2-indexo_1 <= 1: # 비교할 요소가 2개일때 앞에것이 크면 바꿔주고 리턴, 아니면 그냥 리턴.
        if arr[indexo_1] > arr[indexo_2]:
            tmp = arr[indexo_1]
            arr[indexo_1] = arr[indexo_2]
            arr[indexo_2] = tmp
        return

    # 인덱스를 가지고 while loop 안에서 계속 연산을 할것이기 때문에, 처음 받은 오리지날 인덱스는 따로 살려둠(나중에 써야함).
    index_1 = indexo_1; index_2 = indexo_2

    # 피봇하나를 정하는데, 입력받은 가운데 위치로 택함. 만약 입력 어레이가 5,4,3,2,1 일때, 젤 뒤에 인덱스를 피봇으로 잡으면, 최악의 시간복잡도가 됨.
    pivot_index = indexo_1+int((indexo_2-indexo_1)/2)

    # 이렇게 피봇을 정해주면, 제일 뒤로 보내줌(바꿔치기).
    pivot = arr[pivot_index]
    arr[pivot_index] = arr[indexo_2]
    arr[indexo_2] = pivot
    index_2 -= 1 # 피봇 앞에 있는거 부터 비교할려고, 인덱스 하나 빼줌

    while True:
        if arr[index_1] > pivot and arr[index_2] < pivot: # 앞에 요소는 피봇보다 크고, 뒤에 요소는 피봇보다 작으면, 두개 자리 바꾸고 인덱스 갱신.
            tmp = arr[index_1]
            arr[index_1] = arr[index_2]
            arr[index_2] = tmp
            index_1 += 1; index_2 -= 1
        elif arr[index_1] < pivot and arr[index_2] > pivot: # 만약 위의 조건식의 반대라면, 다음 껄 탐색 하기위해서, 인덱스 갱신.
            index_1 += 1; index_2 -= 1
        elif arr[index_1] < pivot: # 여기 까지 왔다는건, "and" 둘중 하나는 성립 된 상황이란거임. 그렇다면 조건 하나식 따로주면서, 인덱스 갱신해주면됨.
            index_1 += 1
        elif arr[index_2] > pivot:
            index_2 -= 1
        if index_1 > index_2: # 초기 인덱스의 위치가 역전되면 while loop 빠져나감.
            break

    # 그리고 피봇인 제일 마지막 위치와 index_1의 위치랑 바꿔주면, 피봇을 기준으로 젤 왼쪽은 피봇보다 작게, 젤 오른쪽은 피봇보다 크게 셋팅됨.
    arr[indexo_2] = arr[index_1]
    arr[index_1] = pivot

    # 이제 위의 연산을 재귀로 반복 할건데,
    qSort(indexo_1, index_1) # 처음 오리지날 젤 첫 인덱스와, 중간 쯤 되는 index_1을 마지막 인덱스인마냥 매개변수로 넣어줌. (딱 피봇을 기준으로 왼쪽 부분 넣는거.)
    qSort(index_1, indexo_2) # 이건 index_1을 젤 첫 인덱스로, 처음 오리지날 젤 마지막 인덱스를 마지막 인덱스인마냥 매개변수로 넣어줌. (딱 피봇을 기준으로 오른쪽 부분 넣는거.)

# 실제 함수 실행
qSort(0, len(arr)-1)

# 출력
for crnt in arr:
    print(crnt)
