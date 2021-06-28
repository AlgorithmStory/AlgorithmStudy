import sys
N = int(sys.stdin.readline())

result = []
for i in range(N):
    input_0 = int(sys.stdin.readline())
    result.append(input_0) # 입력값 받아오는 순간 result에 저장

# result.sort() # 오름차순 정렬
# for i in result:
#     print(i)

def sort_result(result):
    n = len(result)
    # 정렬할 자료 개수가 한 개 이하면 정렬할 필요 X
    if n <= 1:
        return

    mid = n // 2 # 중간 부분을 기점으로 두 그룹으로 나눈다
    group1 = result[:mid] # group1은 중간 기점으로 앞부분
    group2 = result[mid:] # group2은 중간 기점으로 뒷부분
    
    sort_result(group1) # 재귀함수 이용하여 group1 정렬
    sort_result(group2) # 재귀함수 이용하여 group2 정렬

    group1_index = 0
    group2_index = 0
    result_index = 0
    while group1_index < len(group1) and group2_index < len(group2): # group1, group2에 자료가 남아있는 동안 반복
        # group1 = [2, 5] # group2 = [1, 3, 4] 결과 : result = [1] (group1 = [2, 5] group2 = [3, 4])
        if group1[group1_index] < group2[group2_index]: # group1, group2의 인덱스 값 비교
            # 여기서 result_index와 group1인덱스를 같이 증가시켜 이미 처리한 인덱스 값은 group1에서 없애주는 의미가 됨
            result[result_index] = group1[group1_index]
            group1_index = group1_index + 1
            result_index = result_index + 1
        
        else:
            # 여기서 result_index와 group2인덱스를 같이 증가시켜 이미 처리한 인덱스 값은 group2에서 없애주는 의미가 됨
            result[result_index] = group2[group2_index]
            group2_index = group2_index + 1
            result_index = result_index + 1
        # 반복시 result = [1, 2] (group1 = [5] group2 = [3, 4])
        # 반복시 result = [1, 2, 3] (group1 = [5] group2 = [4])
        # 반복시 result = [1, 2, 3, 4] (group1 = [5] group2 = [])

    # 위처럼 그룹 하나가 무조건 남게되어 밑에서 처리
    # 위에서 group1, group2중 이미 빈 것은 while 지나감
    while group1_index < len(group1):
        result[result_index] = group1[group1_index]
        group1_index = group1_index + 1
        result_index = result_index + 1

    while group2_index < len(group2):
        result[result_index] = group2[group2_index]
        group2_index = group2_index + 1
        result_index = result_index + 1

    return result

sort_result(result)
for i in result:
    print(i)