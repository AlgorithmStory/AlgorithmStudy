import sys

N = int(input())
cnt = [0]*10001                             # 카운트할 리스트 만들어주기 10000보다 작다하니 이만큼 배정

for i in range(N):                          # 입력된 수를 cnt의 인덱스에 추가해주기
    cnt[int(sys.stdin.readline())] +=1  

for i in range(len(cnt)):                   
    for j in range(cnt[i]):                 # cnt에 적혀있는 수 만큼 해당 인덱스 출력
        print(i)