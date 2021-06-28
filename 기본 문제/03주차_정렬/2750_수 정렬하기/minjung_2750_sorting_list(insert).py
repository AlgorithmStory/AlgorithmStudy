# 문제 :  https://www.acmicpc.net/problem/2750

import sys

# ******** 입력 ***********
N = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(N)]

# N = 6
# n_list = [5, 6, 4, 3, 1, 7]
# # print('n_list : ',n_list)

# ******** insert sort ***********
# n_list[1] 부터 수행
for i in range(1,N) :
    # print('\t i : ',i)
    insert = n_list[i] # 삽입할 요소 선택
    j =  i - 1
    # 조건에 따른 삽입할 요소 삽입위치 설정
    while j >= 0 :
        compare = n_list[j]
        if compare > insert:
            n_list.remove(insert) # 먼저 있던 삽입요소와 같은 값 삭제
            n_list.insert(j, insert) # 알맞은 위치에 삽입
        # print('\t\t',n_list)
        j = j - 1 # 삽입 여부 검사할 인덱스 위치 옮김


# ******** 출력 ***********
for i in n_list:
    print(i)

