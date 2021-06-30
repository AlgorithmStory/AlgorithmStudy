import sys
# ****************필요한변수설정******************
N = int(sys.stdin.readline())
input_list = []
for i in range(N):
    input_list.append(int(sys.stdin.readline()))

sorted_list = [-1] * N
# ******** merge sorting(오름차순) 함수 선언 *****
    
def merge(temp_list, left, mid, right):
    global sorted_list
#    global deep, sorted_list
#     print('\t'*deep,'merge!! deep : ',deep,'list : ',temp_list,'left:',left,'mid',mid,'right:',right)
    i = left
    j = mid+1
    k = left
    # 분할 정렬된 list의 합병
    while (i<=mid) and (j<=right):
        if (temp_list[i] <= temp_list[j]):
            sorted_list[k] = temp_list[i]
            k += 1
            i += 1
        else:
            sorted_list[k] = temp_list[j]
            k += 1
            j += 1
            
#     print('\t'*deep,'after while sorted_list : ',sorted_list)
    # 남아 있는 값들을 일괄 복사 (오른쪽 리스트)
    if i > mid:
        for l in range(j,right+1):
            sorted_list[k] = temp_list[l]
            k += 1
    # 남아 있는 값들을 일괄 복사 (왼쪽 리스트)
    else:
        for l in range(i,mid+1):
            sorted_list[k] = temp_list[l]
            k += 1
#     print('\t'*deep,'after while sorted_list : ',sorted_list)        
    # 배열 sorted_list(임시 정렬)의 리스트를 배열 list로 재복사
    for l in range(left,right+1):
        temp_list[l] = sorted_list[l]
    
#     print('\t'*deep,'after merge : ',temp_list)
    return temp_list

# ********************** 나누는 함수 선언 **********************
def divise_list(temp_list,left,right):
    global deep
#    deep += 1
#     print('\t'*deep,'deep : ',deep)
#     print('\t'*deep,'temp_list :',temp_list,'left :',left,'right :',right)
    # basement 유무 검사 
    if left<right :
        mid = int((left + right)/2)
        divise_list(temp_list, left, mid)
        divise_list(temp_list, mid+1, right)
        temp_list = merge(temp_list, left, mid, right)
#    else:
#         print('\t'*deep,'basement')
              
#    deep =  deep - 1
    return temp_list

# ************* 함수실행 및 출력******************

output_list = divise_list(input_list,0,N-1)

for i in output_list:
    print(i)
