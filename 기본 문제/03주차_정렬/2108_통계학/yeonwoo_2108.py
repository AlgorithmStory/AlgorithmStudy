import sys
N = int(sys.stdin.readline())

result = []
for i in range(N):
    result.append(int(sys.stdin.readline())) # 입력값 받아오는 순간 result에 저장

def statistic(result, N):
    # 평균
    print(round(sum(result) / N))

    # 중앙값
    result.sort()
    print(result[N // 2])

    # 최빈값 (시간초과)
    # result_unique = list(set(result)) # 중복제거

    # result_mode = []
    # result_count = 0
    # for i in result_unique:
    #     if result_count == result.count(i):
    #         result_mode.append(i)
        
    #     elif result_count < result.count(i):
    #         result_mode = []
    #         result_mode.append(i)
    #         result_count = result.count(i)

    # if len(result_mode) > 1: # 최빈값이 2개 이상이면
    #     result_mode.sort()
    #     print(result_mode[1])

    # else: # 최빈값이 1개면
    #     print(result_mode[0])

    # 최빈값
    from collections import Counter
    mod_result = Counter(result).most_common()

    # print(mod_result)
    if len(result) > 1: # 입력 값이 하나 이상이면
        if mod_result[0][1] == mod_result[1][1]:
            print(mod_result[1][0]) 
            # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번째로 작은것을 출력

        else : 
            print(mod_result[0][0]) 

    else : #만약 입력값이 하나면 , 그게 최빈값이 되므로 예외처리
        print(result[0]) 

    # 범위 = 최대 - 최소
    print(max(result) - min(result))

statistic(result, N)