# **************bar********************
# 문제 https://www.acmicpc.net/problem/17608
#
# context
#   1.사용자로부터 바 몇개 받을지 입력받고 그 갯수만큼 바 길이 bar_list에 초기화
#   2.보이는 막대기 갯수 세기
#   3.보이는지 여부를 역순으로 판별하자
#       # 3.1.가장큰 길이와 비교하여 더크면 can_see_count값 증가 
#   4.보이는 갯수 출력
#

import sys

def do_calculate_veiw_count():
    # 변수 초기화    
    bar_list = []
    can_see_count = 1 # 몇개가 보일지 저장할 변수 - 최소 1개는 보일테니 1로 초기화

    # 1.사용자로부터 바 몇개 받을지 입력받고 그 갯수만큼 바 길이 bar_list에 초기화
    
    for _ in range(int(sys.stdin.readline())):
        bar_list.append(int(sys.stdin.readline()))

    # print('bar_list',bar_list)


    # 2.보이는 막대기 갯수 세기
    max_h = bar_list[-1] # 막대기 최대길이 처음엔 무조건 맨마지막요소 길이일테니 그값으로 초기화
    # print('max_h',max_h)
    

    # 3.보이는지 여부를 역순으로 판별하자
    for i in reversed(bar_list[:-1]):
        # print(i,end="")
        # 3.1.가장큰 길이와 비교하여 더크면 can_see_count값 증가 
        if i > max_h:
            can_see_count += 1
            max_h = i


    # 4.보이는 갯수 출력
    print(can_see_count)


if __name__ == '__main__':
    do_calculate_veiw_count()