T = int(input())

for _ in range(T):
    n = int(input())
    a = [0,1,2,4]                           # 3까지 정수의 합 리스트
    
    for i in range(4,n+1):
        a.append(a[i-1]+a[i-2]+a[i-3])      # 앞선 세개의 정수 합이 다음 정수의 합이므로 저장
    print(a[n])