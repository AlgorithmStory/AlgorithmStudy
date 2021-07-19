import sys
X = int(sys.stdin.readline())

min_count_1 = [0] * (X + 1)
 
min_count_index = 0
while True:
    if min_count_index > X:
        break
 
    if min_count_index <= 1: # 0, 1까지는 연산횟수가  0이므로 0으로 설정
        min_count_1[min_count_index] = 0

    else: # 미리 계산한 인덱스 값에 대한 최댓값 구하는 방식
        result = X + 1
        if min_count_index % 3 == 0: 
            result = min(result, min_count_1[min_count_index // 3])

        if min_count_index % 2 == 0:
            result = min(result, min_count_1[min_count_index // 2])
 
        result = min(result, min_count_1[min_count_index-1])

        min_count_1[min_count_index] = int(result + 1)
    min_count_index = min_count_index + 1
    
print(min_count_1[X])