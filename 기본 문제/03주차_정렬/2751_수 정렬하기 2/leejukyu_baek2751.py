import sys

def split(a):                               # 분할 함수
    if len(a) <=1:                          # 입력값이 1개 이하면 그대로 반환
        return a

    m = len(a) // 2                         # 인덱스 중앙값
    left = a[:m]                            # 중앙값 기준으로 왼쪽 인덱싱
    right = a[m:]                           # 중앙값 기준으로 오른쪽 인덱싱
    left = split(left)                      # 왼쪽 분할 반복
    right = split(right)                    # 오른쪽 분할 반복
    return merge(left, right)               # 분할이 끝나면 합병 함수 실행

def merge(left, right):
    i = 0
    j = 0
    lst = []
    
    while i < len(left) and j < len(right): # 둘 중 한 길이가 끝날 때까지 합병하는 반복문
        if left[i] >= right[j]:             # 왼쪽 수가 더 크면
            lst.append(right[j])            # 작은 오른쪽 값을 리스트에 넣는다
            j += 1                          # 오른쪽 인덱스를 한칸 옮겨줌

        else:
            lst.append(left[i])             # 작은 왼쪽 값을 리스트에 넣음
            i += 1                          # 인덱스 옮겨줌

    for k in range(i, len(left)):           # 반복문이 돌고 남은 수 합쳐주기
        lst.append(left[k])
    for k in range(j, len(right)):
        lst.append(right[k])
    
    return lst                              # 합병한 리스트 리턴

N = int(input())
a = [int(sys.stdin.readline()) for _ in range(N)] 

for i in split(a):
    print(i)