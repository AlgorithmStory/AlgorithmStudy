from sys import stdin
# ********************** 함수들 **************************

# 평균
def mean(i_list):
    return round(sum(i_list)/len(i_list))


# 중앙값
def median(i_list):
    m = int(len(i_list)/2)
    return i_list[m]


# 최빈값
def mode(i_list):
    c_mode = {} # key : 숫자, value: 빈도수 쌍으로 저장할 딕셔너리 선언
    m_mode = 0 # 최대 빈도수 저장할 변수 선언
    n_mode = [] # 최빈값 저장할 변수 선언(2번쨰 큰수 가져올떄 핸들링하기위해 선언)


    # c_mode 저장
    for n in i_list:
        
        if n not in c_mode:                                     # 만약 처음 들어오는 수라면
            c_mode[n] = 0                                       # key :수 ,value:0 으로 저장

        c_mode[n] += 1                                          # value 1 증가

        if c_mode[n] > m_mode:                                  # 빈도수가 저장된 최대 빈도수보다 크다면
            m_mode = c_mode[n]                                  # 최대 빈도수 갱신


    # 최빈값 n_mode에 저장
    for n, b in c_mode.items():

        if m_mode == b:
            n_mode.append(n)


    # 최빈값 여러개면 2번째 큰수 출력
    if len(n_mode) > 1:
        return n_mode[1]
    else:
        return n_mode[0]

     

# 범위
def max_differ_min(i_list):
    n = i_list[-1] - i_list[0]
    return n


# ********************* 필요 변수 입력 및 전처리 **********************
N = int(stdin.readline())
i_list = []

for i in range(N):
    i_list.append(int(stdin.readline()))


i_list.sort()


# ********************* 결과 출력하는 부분 *********************
print(mean(i_list))
print(median(i_list))
print(mode(i_list))
print(max_differ_min(i_list))
