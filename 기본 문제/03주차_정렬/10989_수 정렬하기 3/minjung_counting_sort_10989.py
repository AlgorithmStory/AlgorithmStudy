import sys
c_dict = {}                                                           # 카운팅 계수 저장할 딕셔너리 선언

N = int(sys.stdin.readline())                                         # 정렬할 데이터들 크기 입력받음

for i in range(N):
    value = int(sys.stdin.readline())                                 # 정렬할 데이터 입력받기
    
    if value not in c_dict:                                           # 처음들어오는 데이터 value 0 으로 선언
        c_dict[value] = 0                                             
            
    c_dict[value] += 1                                                # 입력받은 데이터를 key로 하는 value 1증가
    
keys = sorted(c_dict)                                                 # dict keys 기준으로 정렬
    
for key in keys:
    print(f'{key}\n'*c_dict[key],end = "")                            # 각각의 key를 values 만큼 
