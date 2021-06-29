import sys                                                          # 그냥 sort 메소드 쓰면 통과 됨


def quick_sort(input_numbers):
    if len(input_numbers) <= 1:
        return input_numbers
    else:
        pivot = [input_numbers[len(input_numbers) // 2]]            # 중간 부분을 기둥으로 설정
        left, right = [], []
        for i in input_numbers:                                     # 기둥 기준 작으면 왼쪽 배열, 크면 오른쪽 배열
            if i < pivot[0]:
                left.append(i)
            elif i > pivot[0]:
                right.append(i)
        return quick_sort(left) + pivot + quick_sort(right)         # 왼쪽, 오른쪽 배열에 대해 재귀로 다시 quick sort 실행


def merge_sort(input_numbers):
    if len(input_numbers) < 2:
        return input_numbers

    mid = len(input_numbers) // 2                                   # 중간 부분 설정
    left = merge_sort(input_numbers[:mid])                          # 왼쪽 부분 배열
    right = merge_sort(input_numbers[mid:])                         # 오른쪽 부분 배열

    merged_arr = []                                                 # 병합할 배열
    l = r = 0
    while l < len(left) and r < len(right):                         # 왼쪽 오른쪽 배열 차례대로 비교
        if left[l] < right[r]:                                      # 작은 것 부터 순서대로 병합할 배열에 넣음
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
    merged_arr += left[l:]                                          # 하나가 전부 들어가면 나머지도 그 뒤에 넣어줌
    merged_arr += right[r:]
    return merged_arr


length_of_list = int(sys.stdin.readline().split()[0])
numbers = []

for i in range(length_of_list):                                         # 숫자 배열 읽어옴
    numbers.append(int(sys.stdin.readline().split()[0]))

for i in merge_sort(numbers):
    print(i)
