n = int(input())                                              # 수의 개수
array=[]
for i in range(n):
    array.append(int(input()))                               # 입력 값으로 배열만들기

# 선택 정렬
for i in range(len(array)): 
    min_index = i                                            # 가장 작은 값 인덱스
    for j in range(i+1, len(array)):                         # for문을 돌리면서 가장 작은 값의 인덱스를 찾기
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 실행하는 자리 인덱스와 가장 작은 값의 인덱스를 바꿈

# 삽입 정렬
for i in range(1, len(array)):                               # 두번째 값부터 앞의 값들과 비교하기 때문에 range(1, len(array))로 설정
    for j in range(i, 0, -1):                                # range의 세번째 argument를 -1로 하여 역순으로 찾게함
        if array[j] < array[j-1]:                            
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

for k in array:
    print(k)