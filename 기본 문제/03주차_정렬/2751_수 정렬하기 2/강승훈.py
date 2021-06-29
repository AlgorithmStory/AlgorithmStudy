from sys import stdin

# 입력
n = int(input())
arr = [int(stdin.readline()) for _ in range(n)]

# 병합정렬 함수 구현부
def mergeSort(indexo_1, indexo_2): # 젤 처음 인덱스와, 제일 마지막 인덱스 받음.

    if indexo_2 == indexo_1: # 요소 1개를 의미하는거면, 해당 요소 바로 리턴 시킴.
        return [arr[indexo_1]]
    if indexo_2 - indexo_1 == 1: # 인덱스로 넘어온 두개가, 배열 요소 2개를 의미하는거면, 두개 만 우선 오름차순 정렬해서 바로 리턴 시킴.
        if arr[indexo_1] > arr[indexo_2]:
            return [arr[indexo_2], arr[indexo_1]]
        else:
            return [arr[indexo_1], arr[indexo_2]]

    index_half = indexo_1+int((indexo_2-indexo_1)/2) # 입력 받은 인덱스 범위 내에서, 가운데 인덱스 추출.

    # 가운데 인덱스를 기준으로 왼쪽, 오른쪽 나눠서 재귀 호출 시킴.
    arr_left = mergeSort(indexo_1, index_half)
    arr_right = mergeSort(index_half+1, indexo_2)

    # 위에 두개에서 재귀 호출 시킨 뒤, 리턴된 배열 2개를 합쳐서 정렬 시킬꺼라, 우선 길이 저장.
    arr_left_len = len(arr_left)
    arr_right_len = len(arr_right)

    result_arr = [] # 최종적으로 여기다 정렬된걸 담아서 리턴 시킬 거임.

    index_left = 0; index_right = 0 # while문으로 두개의 배열에 대해서, 앞에서부터 큰것들부터 담을거기 때문에, 우선 인덱스 2개 설정.
    while True:
        if index_left > arr_left_len-1: # left배열에서 더이상 비교할 요소가 없으면, 남은 right배열 순서대로 다 담아주고 빠져나옴.
            for i in range(index_right, arr_right_len):
                result_arr.append(arr_right[i])
            break
        if index_right > arr_right_len-1: # right배열도 마찮가지.
            for i in range(index_left, arr_left_len):
                result_arr.append(arr_left[i])
            break

        # 두 배열을 result_arr에 비교하면서 작은거부터 담는 구문.
        if arr_left[index_left] < arr_right[index_right]:
            result_arr.append(arr_left[index_left])
            index_left += 1
        else:
            result_arr.append(arr_right[index_right])
            index_right += 1

    # 위의 while문으로 인해서, result_arr에 정렬된 상태로 담김. 이걸 리턴.
    return result_arr

# 출력
for crnt in mergeSort(0, n-1):
    print(crnt)
