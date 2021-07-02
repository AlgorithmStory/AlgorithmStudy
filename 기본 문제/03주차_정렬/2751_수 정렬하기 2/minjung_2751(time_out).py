import sys
# ****************필요한변수설정******************
N = int(sys.stdin.readline())
input_list = []

for i in range(N):
    input_list.append(int(sys.stdin.readline()))

# ******** merge sorting(오름차순) 함수 선언 *****
def merge(left,right):
    
    sN = len(left)+len(right)
    s_list = [-1]*sN # 정렬된후의 리스트

    # 분할 정렬된 list의 합병
    
    s = 0 # s_list의 인덱스
    r = 0 # right_list 의 인덱스
    l = 0 # letf_list 의 인덱스
    
    
    while (l < len(left)) and (r < len(right)):
        
        if (left[l] <= right[r]):
            
            s_list[s] = left[l]
            l += 1
            s += 1
            
        else:
            
            s_list[s] = right[r]
            r += 1
            s += 1
    
    # 남아 있는 값들을 일괄 복사

    while l < len(left):

        s_list[s] = left[l]
        s += 1
        l += 1
    
    while r < len(right):

        s_list[s] = right[r]
        s += 1
        r += 1

    return s_list
# ********************** 나누는 함수 선언 **********************
def d_list(input_list):

    # basement 유무 검사 
    if len(input_list) > 1 :        
        mid = int(len(input_list)/2)
        left = input_list[:mid]
        right = input_list[mid:]
       
        
        left = d_list(left)
        right = d_list(right)
        input_list = merge(left,right)

    return input_list
            
# ************* 함수실행 및 출력******************

output_list = d_list(input_list)

for i in output_list:
    print(i)
