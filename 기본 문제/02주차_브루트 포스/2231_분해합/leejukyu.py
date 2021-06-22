N = int(input())
cnt = []
num = []

for enu, i in enumerate(range(N)):  # 생성자 리스트 만들기(+인데스번호)
    for j in str(i):                
        i += int(j)
    cnt.append(i)

    if i == N:                      # 분해합이 자연수와 같으면 인덱스번호 리스트에 넣기
        num.append(enu)             # 분해합의 인덱스 번호 == 생성자 값
    
if len(num) == 0:                   # 생성자가 없으면 0 프린트
    print(0)
else: 
    print(min(num))                 # 생성자가 있으면 가장 작은 값 프린트