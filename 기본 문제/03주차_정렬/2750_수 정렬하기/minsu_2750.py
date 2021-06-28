n = int(input())                                              # 수의 개수
array=[]
for i in range(n):
    array.append(int(input()))                               # 입력 값으로 배열만들기


for i in range(len(array)): 
    min_index = i                                            # 가장 작은 값 인덱스
    for j in range(i+1, len(array)):                         # for문을 돌리면서 가장 작은 값의 인덱스를 찾기
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 실행하는 자리 인덱스와 가장 작은 값의 인덱스를 바꿈

for k in array:
    print(k)