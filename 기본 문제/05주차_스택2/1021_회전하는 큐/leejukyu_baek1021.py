import sys
N , M = map(int,input().split())
a = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in range(1, N+1)]                   # 1부터 N까지 리스트

cnt = 0

for k in a:
    while True:
        if arr[0] == k:                                 # 리스트의 첫번째가 a와 같으면
            arr.pop(0)                                  # 리스트에서 뽑아냄
            break                                       # 다음 수 찾으러 가자

        elif arr.index(k) > (len(arr)//2):              # 찾으려는 수의 인덱스가 리스트의 절반보다 크면
            arr.insert(0, arr[-1])                      # 오른쪽으로 한 칸 이동
            arr.pop()
            cnt += 1                                    # 카운트
                 
        else:                                           # 인덱스가 리스트의 반보다 짧으면
            arr.append(arr[0])                          # 왼쪽으로 한 칸 이동              
            arr.pop(0)
            cnt += 1                                    # 카운트
            
print(cnt)